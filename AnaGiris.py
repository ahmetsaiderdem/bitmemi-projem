# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnaGiris.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Yönetici import Ui_Yonetici

class Ui_AnaGiris(object):
    def setupUi(self, AnaGiris):
        AnaGiris.setObjectName("AnaGiris")
        AnaGiris.resize(368, 371)
        self.centralwidget = QtWidgets.QWidget(AnaGiris)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_grs = QtWidgets.QLabel(self.centralwidget)
        self.lbl_grs.setGeometry(QtCore.QRect(50, 100, 91, 20))
        self.lbl_grs.setObjectName("lbl_grs")
        self.btn_grs = QtWidgets.QPushButton(self.centralwidget)
        self.btn_grs.setGeometry(QtCore.QRect(180, 190, 111, 31))
        self.btn_grs.setObjectName("btn_grs")
        self.cmb_grs = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_grs.setGeometry(QtCore.QRect(220, 100, 69, 22))
        self.cmb_grs.setObjectName("cmb_grs")
        self.cmb_grs.addItem("")
        self.cmb_grs.addItem("")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 130, 141, 53))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ln_kll = QtWidgets.QLineEdit(self.layoutWidget)
        self.ln_kll.setObjectName("ln_kll")
        self.gridLayout.addWidget(self.ln_kll, 0, 0, 1, 1)
        self.ln_sif = QtWidgets.QLineEdit(self.layoutWidget)
        self.ln_sif.setObjectName("ln_sif")
        self.gridLayout.addWidget(self.ln_sif, 1, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(47, 129, 91, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_kll = QtWidgets.QLabel(self.layoutWidget1)
        self.lbl_kll.setObjectName("lbl_kll")
        self.gridLayout_2.addWidget(self.lbl_kll, 0, 0, 1, 1)
        self.lbl_sif = QtWidgets.QLabel(self.layoutWidget1)
        self.lbl_sif.setObjectName("lbl_sif")
        self.gridLayout_2.addWidget(self.lbl_sif, 1, 0, 1, 1)
        self.lbl_hata = QtWidgets.QLabel(self.centralwidget)
        self.lbl_hata.setGeometry(QtCore.QRect(180, 230, 171, 71))
        self.lbl_hata.setText("")
        self.lbl_hata.setObjectName("lbl_hata")
        AnaGiris.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AnaGiris)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 368, 26))
        self.menubar.setObjectName("menubar")
        AnaGiris.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AnaGiris)
        self.statusbar.setObjectName("statusbar")
        AnaGiris.setStatusBar(self.statusbar)

        self.retranslateUi(AnaGiris)
        QtCore.QMetaObject.connectSlotsByName(AnaGiris)

    def retranslateUi(self, AnaGiris):
        _translate = QtCore.QCoreApplication.translate
        AnaGiris.setWindowTitle(_translate("AnaGiris", "MainWindow"))
        self.lbl_grs.setText(_translate("AnaGiris", "Giriş Yöntemi"))
        self.btn_grs.setText(_translate("AnaGiris", "Giriş"))
        self.cmb_grs.setItemText(0, _translate("AnaGiris", "Yönetici"))
        self.cmb_grs.setItemText(1, _translate("AnaGiris", "Öğrenci"))
        self.lbl_kll.setText(_translate("AnaGiris", "Kullanıcı adı:"))
        self.lbl_sif.setText(_translate("AnaGiris", "Şifre :"))
