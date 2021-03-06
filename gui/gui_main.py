# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GUI(object):

    def setupUi(self, GUI):
        GUI.setObjectName("GUI")
        GUI.resize(634, 524)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GUI.sizePolicy().hasHeightForWidth())
        GUI.setSizePolicy(sizePolicy)
        GUI.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        GUI.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(GUI)
        self.centralwidget.setObjectName("centralwidget")

        #Botão de iniciar leitura
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 430, 391, 27))
        self.pushButton.setObjectName("pushButton")

        # Tela da câmera
        self.graphicsView = QtWidgets.QLabel(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 20, 391, 371))
        self.graphicsView.setObjectName("graphicsView")

        #Separador
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 20, 20, 451))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        #Barra de progresso para leitura
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 400, 391, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 120, 181, 17))
        self.label.setObjectName("label")

        #Lista de EPIs por Lab
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(420, 150, 201, 241))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 30, 91, 17))
        self.label_2.setObjectName("label_2")

        #Lista de labs
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(420, 50, 201, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setItemText(1,"Laboratório 1")
        GUI.setCentralWidget(self.centralwidget)


        #Menus
        self.menubar = QtWidgets.QMenuBar(GUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 22))
        self.menubar.setObjectName("menubar")
        self.menuAvan_ado = QtWidgets.QMenu(self.menubar)
        self.menuAvan_ado.setObjectName("menuAvan_ado")
        self.menuEditar_Laborat_rio = QtWidgets.QMenu(self.menuAvan_ado)
        self.menuEditar_Laborat_rio.setObjectName("menuEditar_Laborat_rio")
        self.menuCadastro_de_EPIs = QtWidgets.QMenu(self.menuAvan_ado)
        self.menuCadastro_de_EPIs.setObjectName("menuCadastro_de_EPIs")
        self.menuBem_vindo = QtWidgets.QMenu(self.menubar)
        self.menuBem_vindo.setObjectName("menuBem_vindo")
        self.menuAvaliar_EPIs = QtWidgets.QMenu(self.menubar)
        self.menuAvaliar_EPIs.setObjectName("menuAvaliar_EPIs")
        GUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GUI)
        self.statusbar.setObjectName("statusbar")
        GUI.setStatusBar(self.statusbar)


        #Ações dos menus
        self.actionRemover_EPIs = QtWidgets.QAction(GUI)
        self.actionRemover_EPIs.setObjectName("actionRemover_EPIs")
        self.actionOrdenar_EPIs = QtWidgets.QAction(GUI)
        self.actionOrdenar_EPIs.setObjectName("actionOrdenar_EPIs")
        self.actionVer_relat_rios = QtWidgets.QAction(GUI)
        self.actionVer_relat_rios.setObjectName("actionVer_relat_rios")
        self.actionSobre_o_laborat_rio = QtWidgets.QAction(GUI)
        self.actionSobre_o_laborat_rio.setObjectName("actionSobre_o_laborat_rio")

        #Iniciar Leitura
        self.actionIniciar_leitura = QtWidgets.QAction(GUI)
        self.actionIniciar_leitura.setObjectName("actionIniciar_leitura")

        #Ver ultima leitura
        self.actionVer_ltima_leitura = QtWidgets.QAction(GUI)
        self.actionVer_ltima_leitura.setObjectName("actionVer_ltima_leitura")

        #Adicionar Laboratório
        self.actionAdicionar_laborat_rio = QtWidgets.QAction(GUI)
        self.actionAdicionar_laborat_rio.setObjectName("actionAdicionar_laborat_rio")
        self.actionAlterar_laborat_rio = QtWidgets.QAction(GUI)
        self.actionAlterar_laborat_rio.setObjectName("actionAlterar_laborat_rio")
        self.actionAlterar_EPIs = QtWidgets.QAction(GUI)
        self.actionAlterar_EPIs.setObjectName("actionAlterar_EPIs")
        self.actionAlterar_Riscos = QtWidgets.QAction(GUI)
        self.actionAlterar_Riscos.setObjectName("actionAlterar_Riscos")
        self.actionAlterar_descri_ao = QtWidgets.QAction(GUI)
        self.actionAlterar_descri_ao.setObjectName("actionAlterar_descri_ao")
        self.actionAlterar_nome = QtWidgets.QAction(GUI)
        self.actionAlterar_nome.setObjectName("actionAlterar_nome")
        self.actionAdicionar_EPI = QtWidgets.QAction(GUI)
        self.actionAdicionar_EPI.setObjectName("actionAdicionar_EPI")
        self.actionRemover_EPI = QtWidgets.QAction(GUI)
        self.actionRemover_EPI.setObjectName("actionRemover_EPI")
        self.actionAdicionar_novo_tipo_de_prote_ao = QtWidgets.QAction(GUI)
        self.actionAdicionar_novo_tipo_de_prote_ao.setObjectName("actionAdicionar_novo_tipo_de_prote_ao")
        self.actionOrdenar_EPIs_2 = QtWidgets.QAction(GUI)
        self.actionOrdenar_EPIs_2.setObjectName("actionOrdenar_EPIs_2")
        self.actionIncluir_EPIs = QtWidgets.QAction(GUI)
        self.actionIncluir_EPIs.setObjectName("actionIncluir_EPIs")
        self.actionRemover_EPIs_2 = QtWidgets.QAction(GUI)
        self.actionRemover_EPIs_2.setObjectName("actionRemover_EPIs_2")
        self.actionIncluir_risco = QtWidgets.QAction(GUI)
        self.actionIncluir_risco.setObjectName("actionIncluir_risco")
        self.actionRemover_risco = QtWidgets.QAction(GUI)
        self.actionRemover_risco.setObjectName("actionRemover_risco")
        self.menuEditar_Laborat_rio.addAction(self.actionAlterar_nome)
        self.menuEditar_Laborat_rio.addAction(self.actionAlterar_descri_ao)
        self.menuEditar_Laborat_rio.addSeparator()
        self.menuEditar_Laborat_rio.addAction(self.actionOrdenar_EPIs_2)
        self.menuEditar_Laborat_rio.addAction(self.actionIncluir_EPIs)
        self.menuEditar_Laborat_rio.addAction(self.actionRemover_EPIs_2)
        self.menuEditar_Laborat_rio.addSeparator()
        self.menuEditar_Laborat_rio.addAction(self.actionIncluir_risco)
        self.menuEditar_Laborat_rio.addAction(self.actionRemover_risco)
        self.menuCadastro_de_EPIs.addAction(self.actionAdicionar_EPI)
        self.menuCadastro_de_EPIs.addAction(self.actionRemover_EPI)
        self.menuCadastro_de_EPIs.addAction(self.actionAdicionar_novo_tipo_de_prote_ao)
        self.menuAvan_ado.addSeparator()
        self.menuAvan_ado.addAction(self.menuCadastro_de_EPIs.menuAction())
        self.menuAvan_ado.addAction(self.actionVer_relat_rios)
        self.menuAvan_ado.addSeparator()
        self.menuAvan_ado.addAction(self.actionAdicionar_laborat_rio)
        self.menuAvan_ado.addAction(self.menuEditar_Laborat_rio.menuAction())
        self.menuBem_vindo.addAction(self.actionSobre_o_laborat_rio)
        self.menuAvaliar_EPIs.addAction(self.actionIniciar_leitura)
        self.menuAvaliar_EPIs.addAction(self.actionVer_ltima_leitura)
        self.menubar.addAction(self.menuBem_vindo.menuAction())
        self.menubar.addAction(self.menuAvaliar_EPIs.menuAction())
        self.menubar.addAction(self.menuAvan_ado.menuAction())

        self.retranslateUi(GUI)
        QtCore.QMetaObject.connectSlotsByName(GUI)

    def retranslateUi(self, GUI):
        _translate = QtCore.QCoreApplication.translate
        GUI.setWindowTitle(_translate("GUI", "EPI Check"))
        self.pushButton.setText(_translate("GUI", "Iniciar Leitura"))
        self.label.setText(_translate("GUI", "EPIs requeridos"))
        self.label_2.setText(_translate("GUI", "Laboratório:"))
        self.menuAvan_ado.setTitle(_translate("GUI", "Configurações do laboratório"))
        self.menuEditar_Laborat_rio.setTitle(_translate("GUI", "Editar Laboratório"))
        self.menuCadastro_de_EPIs.setTitle(_translate("GUI", "Cadastro de EPIs"))
        self.menuBem_vindo.setTitle(_translate("GUI", "Bem vindo"))
        self.menuAvaliar_EPIs.setTitle(_translate("GUI", "Avaliar EPIs"))
        self.actionRemover_EPIs.setText(_translate("GUI", "Remover EPIs"))
        self.actionOrdenar_EPIs.setText(_translate("GUI", "Ordenar EPIs"))
        self.actionVer_relat_rios.setText(_translate("GUI", "Ver relatórios"))
        self.actionSobre_o_laborat_rio.setText(_translate("GUI", "Sobre o laboratório"))
        self.actionIniciar_leitura.setText(_translate("GUI", "Iniciar leitura"))
        self.actionVer_ltima_leitura.setText(_translate("GUI", "Ver última leitura"))
        self.actionAdicionar_laborat_rio.setText(_translate("GUI", "Adicionar laboratório"))
        self.actionAlterar_laborat_rio.setText(_translate("GUI", "Alterar laboratório"))
        self.actionAlterar_EPIs.setText(_translate("GUI", "Alterar EPIs"))
        self.actionAlterar_Riscos.setText(_translate("GUI", "Alterar Riscos"))
        self.actionAlterar_descri_ao.setText(_translate("GUI", "Alterar descriçao"))
        self.actionAlterar_nome.setText(_translate("GUI", "Alterar nome"))
        self.actionAdicionar_EPI.setText(_translate("GUI", "Adicionar EPI"))
        self.actionRemover_EPI.setText(_translate("GUI", "Remover EPI"))
        self.actionAdicionar_novo_tipo_de_prote_ao.setText(_translate("GUI", "Adicionar novo tipo de proteçao"))
        self.actionOrdenar_EPIs_2.setText(_translate("GUI", "Ordenar EPIs"))
        self.actionIncluir_EPIs.setText(_translate("GUI", "Incluir EPIs"))
        self.actionRemover_EPIs_2.setText(_translate("GUI", "Remover EPIs"))
        self.actionIncluir_risco.setText(_translate("GUI", "Incluir risco"))
        self.actionRemover_risco.setText(_translate("GUI", "Remover risco"))


