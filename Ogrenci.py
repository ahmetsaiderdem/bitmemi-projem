# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Öğrenci.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ogrenci(object):
    def setupUi(self, Ogrenci):
        Ogrenci.setObjectName("Ogrenci")
        Ogrenci.resize(301, 203)
        self.centralwidget = QtWidgets.QWidget(Ogrenci)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 251, 111))
        self.groupBox.setObjectName("groupBox")
        self.alo_1 = QtWidgets.QLabel(self.groupBox)
        self.alo_1.setGeometry(QtCore.QRect(40, 50, 55, 16))
        self.alo_1.setText("")
        self.alo_1.setObjectName("alo_1")
        self.alo_2 = QtWidgets.QLabel(self.groupBox)
        self.alo_2.setGeometry(QtCore.QRect(120, 50, 81, 16))
        self.alo_2.setText("")
        self.alo_2.setObjectName("alo_2")
        self.btn_cks2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cks2.setGeometry(QtCore.QRect(20, 120, 251, 28))
        self.btn_cks2.setObjectName("btn_cks2")
        Ogrenci.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ogrenci)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 301, 26))
        self.menubar.setObjectName("menubar")
        Ogrenci.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ogrenci)
        self.statusbar.setObjectName("statusbar")
        Ogrenci.setStatusBar(self.statusbar)

        self.retranslateUi(Ogrenci)
        QtCore.QMetaObject.connectSlotsByName(Ogrenci)

    def retranslateUi(self, Ogrenci):
        _translate = QtCore.QCoreApplication.translate
        Ogrenci.setWindowTitle(_translate("Ogrenci", "MainWindow"))
        self.groupBox.setTitle(_translate("Ogrenci", "Ahmet 192106035"))
        self.btn_cks2.setText(_translate("Ogrenci", "Çıkış"))
