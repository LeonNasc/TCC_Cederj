# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laboratorio.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(590, 560)
        self.nome = QtWidgets.QLineEdit(Dialog)
        self.nome.setGeometry(QtCore.QRect(100, 30, 221, 25))
        self.nome.setObjectName("nome")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(400, 530, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 530, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Riscos = QtWidgets.QListView(Dialog)
        self.Riscos.setGeometry(QtCore.QRect(10, 120, 261, 192))
        self.Riscos.setObjectName("Riscos")
        self.Riscos_LAB = QtWidgets.QListView(Dialog)
        self.Riscos_LAB.setGeometry(QtCore.QRect(340, 120, 241, 192))
        self.Riscos_LAB.setObjectName("Riscos_LAB")
        self.descricao = QtWidgets.QLineEdit(Dialog)
        self.descricao.setGeometry(QtCore.QRect(100, 60, 481, 25))
        self.descricao.setObjectName("descricao")
        self.EPIS_LAB = QtWidgets.QListView(Dialog)
        self.EPIS_LAB.setGeometry(QtCore.QRect(340, 320, 241, 192))
        self.EPIS_LAB.setObjectName("EPIS_LAB")
        self.EPIS = QtWidgets.QListView(Dialog)
        self.EPIS.setGeometry(QtCore.QRect(10, 320, 261, 192))
        self.EPIS.setObjectName("EPIS")
        self.Risco_incluir = QtWidgets.QPushButton(Dialog)
        self.Risco_incluir.setGeometry(QtCore.QRect(290, 140, 31, 25))
        self.Risco_incluir.setObjectName("Risco_incluir")
        self.Risco_remover = QtWidgets.QPushButton(Dialog)
        self.Risco_remover.setGeometry(QtCore.QRect(290, 170, 31, 25))
        self.Risco_remover.setObjectName("Risco_remover")
        self.EPI_remover = QtWidgets.QPushButton(Dialog)
        self.EPI_remover.setGeometry(QtCore.QRect(290, 360, 31, 25))
        self.EPI_remover.setObjectName("EPI_remover")
        self.EPI_incluir = QtWidgets.QPushButton(Dialog)
        self.EPI_incluir.setGeometry(QtCore.QRect(290, 330, 31, 25))
        self.EPI_incluir.setObjectName("EPI_incluir")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 67, 21))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 100, 561, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Laboratório"))
        self.pushButton.setText(_translate("Dialog", "Cancelar"))
        self.pushButton_2.setText(_translate("Dialog", "Incluir"))
        self.Risco_incluir.setText(_translate("Dialog", ">"))
        self.Risco_remover.setText(_translate("Dialog", "<"))
        self.EPI_remover.setText(_translate("Dialog", "<"))
        self.EPI_incluir.setText(_translate("Dialog", ">"))
        self.label.setText(_translate("Dialog", "Laboratório"))
        self.label_2.setText(_translate("Dialog", "Descrição"))
