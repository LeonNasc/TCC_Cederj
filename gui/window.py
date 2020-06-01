import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtGui
from . import gui_main as gui_main
from . import lab_gui as lab_gui
import cv2
import numpy as np

class GUI(gui_main.Ui_GUI):

    def __init__(self, labs=[{"nome":"Laboratório Padrão"}]):
        app = QApplication(sys.argv)
        self._labs = labs

        #Inicia uma câmera
        self._cap = cv2.VideoCapture(0)

        #Inicia o widget
        self.inicializar_ui()
        sys.exit(app.exec_())

    def inicializar_bindings(self, ui):
        ui.pushButton.clicked.connect(self.realizarAvaliacao)
        #ui.actionVer_relat_rios.triggered.connect(self.lancar_menu_TODO)
        ui.comboBox.activated.connect(self.alterar_lab)
        ui.actionIniciar_leitura.triggered.connect(self.realizarAvaliacao)
        ui.actionAdicionar_laborat_rio.triggered.connect(self.exibir_laboratorio)

    def inicializar_ui(self):
        self._window = QMainWindow()
        self._instance = gui_main.Ui_GUI()
        self._instance.setupUi(self._window)
        self.carregar_dados(self._labs)
        self._window.show()

    def carregar_dados(self,dados):
        #Lista de laboratórios
        for index,lab in enumerate(dados):
            self._instance.comboBox.insertItem(index, lab.get_nome())

        for index, EPI in enumerate(dados[0].get_epis()):
            self._instance.listWidget.insertItem(index,EPI.get_nome())

        self.inicializar_bindings(self._instance)

    def alterar_lab(self, lab):
        # Definir lab como modelo de referência
        self._curr_lab = lab

        # Exibir nova lista
        self._instance.listWidget.clear() #Limpa lista anterior e coloca nova
        for index, EPI in enumerate(self._labs[lab].get_epis()):
            self._instance.listWidget.insertItem(index,EPI.get_nome())

        return

    def exibir_laboratorio(self):
       print("TODO!")
       dlg = QDialog()
       dialog = lab_gui.Ui_Dialog()
       dialog.setupUi(dlg)
       dlg.setWindowTitle("EPI Check - Adicionar Laboratório")
       dlg.exec_()

    def realizarAvaliacao(self):
        print("Iniciando Avaliação")
        for n in range(0,101):
            image = self.converter_imagem(self._cap)
            import time
            self._instance.graphicsView.setPixmap(QtGui.QPixmap(image))
            time.sleep(.05)
            self._instance.progressBar.setProperty("value", n)

        print("Avaliação concluída!")



    def converter_imagem(self, cap):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()

