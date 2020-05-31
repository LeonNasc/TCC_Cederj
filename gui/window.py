import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from . import gui_main as gui
import cv2
import numpy as np

class GUI(gui.Ui_GUI):

    def __init__(self):
        app = QApplication(sys.argv)

        #Inicia uma câmera
        self._cap = cv2.VideoCapture(0)

        #Inicia o widget
        self.inicializar_ui()

        sys.exit(app.exec_())


    def inicializar_bindings(self, ui):
        ui.pushButton.clicked.connect(self.realizarAvaliacao)

    def inicializar_ui(self):
        self._window = QMainWindow()
        self._instance = gui.Ui_GUI()
        self._instance.setupUi(self._window)
        self.inicializar_bindings(self._instance)
        self._window.show()

    def realizarAvaliacao(self, feed):
        print("Iniciando Avaliação")
        for n in range(0,101):
            import time
            image = self.converter_imagem(self._cap)
            self._instance.graphicsView.setPixmap(QtGui.QPixmap(image))
            time.sleep(.05)
            self._instance.progressBar.setProperty("value", n)

        print("Avaliação concluída!")


    def converter_imagem(self, cap):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()

