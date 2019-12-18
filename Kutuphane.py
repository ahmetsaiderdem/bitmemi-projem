from PyQt5 import QtWidgets
import sys
from AnaGiris import Ui_AnaGiris
from PyQt5 import QtCore
from Yönetici import Ui_Yonetici
from Öğrenci import Ui_Ogrenci

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp,self).__init__()
        self.ui = Ui_AnaGiris()
        self.ui.setupUi(self)
        self.yön = myApp2()
        self.ögr = myApp3()
        
        self.ui.btn_grs.clicked.connect(self.giris)
        
    def giris(self):
        k = self.ui.ln_kll.text()
        s = self.ui.ln_sif.text()
        if self.ui.cmb_grs.currentText() == "Yönetici" and k == "admin1" and s == "1234566":
            self.yön.show()
            myApp.hide(self)
            
        elif self.ui.cmb_grs.currentText() == "Öğrenci" and k == "192106035" and s == "159357":
            self.ögr.show()
            myApp.hide(self)
        else:
            self.ui.lbl_hata.setText(str("Kullanıcı Adı \nveya Şifre Hatalı"))

class myApp2(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp2,self).__init__()
        self.ui2 = Ui_Yonetici()
        self.ui2.setupUi(self)

        self.ui2.btn_ycks.clicked.connect(self.yckis)
        self.ui2.btn_ktpekle.clicked.connect(self.kitapsec)
        self.ui2.btn_ktpal.clicked.connect(self.kitapal)
        self.ui2.btn_ktpekle.clicked.connect(self.tarih)

    def tarih(self):
        baslangic = self.ui2.dte_tarih.date()
        bitis = self.ui2.dte_tarih2.date()
        if self.ui2.cmb_ogrenciler.currentText() == "Ahmet 192106035":
            self.ui2.lbl_a2.setText(format(baslangic.daysTo(bitis)))
        elif self.ui2.cmb_ogrenciler.currentText() == "Bekirhan 192106010":
            self.ui2.lbl_b2.setText(format(baslangic.daysTo(bitis)))
        elif self.ui2.cmb_ogrenciler.currentText() == "Furkan 192106011":
            self.ui2.lbl_f2.setText(format(baslangic.daysTo(bitis)))
        elif self.ui2.cmb_ogrenciler.currentText() == "Mustafa 192106012":
            self.ui2.lbl_m2.setText(format(baslangic.daysTo(bitis)))
        elif self.ui2.cmb_ogrenciler.currentText() == "Doğukan 192106013":
            self.ui2.lbl_d2.setText(format(baslangic.daysTo(bitis)))
        elif self.ui2.cmb_ogrenciler.currentText() == "Mücahit 192106014":
            self.ui2.lbl_mu2.setText(format(baslangic.daysTo(bitis)))
    def kitapal(self):
        if self.ui2.cmb_ogrenciler.currentText() == "Ahmet 192106035":
            self.ui2.lbl_a1.clear() , self.ui2.lbl_a2.clear()
        elif self.ui2.cmb_ogrenciler.currentText() == "Bekirhan 192106010":
            self.ui2.lbl_b1.clear() , self.ui2.lbl_b2.clear()
        elif self.ui2.cmb_ogrenciler.currentText() == "Furkan 192106011":
            self.ui2.lbl_f1.clear() , self.ui2.lbl_f2.clear()
        elif self.ui2.cmb_ogrenciler.currentText() == "Mustafa 192106012":
            self.ui2.lbl_m1.clear() , self.ui2.lbl_m2.clear()
        elif self.ui2.cmb_ogrenciler.currentText() == "Doğukan 192106013":
            self.ui2.lbl_d1.clear() , self.ui2.lbl_d2.clear()
        elif self.ui2.cmb_ogrenciler.currentText() == "Mücahit 192106014":
            self.ui2.lbl_mu1.clear() , self.ui2.lbl_mu2.clear()
    def kitapsec(self):
        items = self.ui2.grp_kitap.findChildren(QtWidgets.QRadioButton)
        if self.ui2.cmb_ogrenciler.currentText() == "Ahmet 192106035":
             for rb in items:
                if rb.isChecked():
                    self.ui2.lbl_a1.setText(rb.text())
        elif self.ui2.cmb_ogrenciler.currentText() == "Bekirhan 192106010":
             for rb in items:
                if rb.isChecked():
                    self.ui2.lbl_b1.setText(rb.text())
        elif self.ui2.cmb_ogrenciler.currentText() == "Furkan 192106011":
             for rb in items:
                if rb.isChecked():
                    self.ui2.lbl_f1.setText(rb.text())
        elif self.ui2.cmb_ogrenciler.currentText() == "Mustafa 192106012":
             for rb in items:
                if rb.isChecked():
                    self.ui2.lbl_m1.setText(rb.text())
        elif self.ui2.cmb_ogrenciler.currentText() == "Doğukan 192106013":
             for rb in items:
                if rb.isChecked():
                    self.ui2.lbl_d1.setText(rb.text())
        elif self.ui2.cmb_ogrenciler.currentText() == "Mücahit 192106014":
             for rb in items:
                if rb.isChecked():
                    self.ui2.lbl_mu1.setText(rb.text())
    def yckis(self):
        myApp2.close(self)
class myApp3(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp3,self).__init__()
        self.ui3 = Ui_Ogrenci()
        self.ui3.setupUi(self)
        self.ui3.btn_cks2.clicked.connect(self.ockis)
        
    def ockis(self):
        myApp3.close(self)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()