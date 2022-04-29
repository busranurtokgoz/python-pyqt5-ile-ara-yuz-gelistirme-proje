from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class Program(QDialog):
    def __init__(self,a=None):
        super(Program, self).__init__(a)
        alan = QGridLayout()

        self.magazaciro=QLabel("Mağazanın Aylık Cirosu")
        alan.addWidget(self.magazaciro,0,0)
        self.personelsatis=QLabel("Personelin Satışı")
        alan.addWidget(self.personelsatis,1,0)
        self.personelmaas=QLabel("Personelin Maaşı ")
        alan.addWidget(self.personelmaas,2,0)
        self.pprimorani=QLabel("Personele yapılan prim oranı ")
        alan.addWidget(self.pprimorani,3,0)
        self.personelprimi=QLabel("Personelin Maaşı+ Prim")
        alan.addWidget(self.personelprimi,7,0)
        self.yazisi = ""
        self.QLEdit1 = QLineEdit()
        alan.addWidget(self.QLEdit1,0,1)
        self.QLEdit2= QLineEdit()
        alan.addWidget(self.QLEdit2,1,1)
        self.QLEdit3= QLineEdit()
        alan.addWidget(self.QLEdit3,2,1)
        self.QLab4= QLabel()
        alan.addWidget(self.QLab4,3,1)
        self.personelprimiyazi=QLabel(self.yazisi)
        alan.addWidget(self.personelprimiyazi,7,1)

        butontus=QPushButton("Hesapla")


        butontus.clicked.connect(self.fonksiyon)
        alan.addWidget(butontus,4,0)

        self.setLayout(alan)
        self.setWindowTitle("Personel Prim Hesaplayıcı")


    def fonksiyon(self):
        q1=int(self.QLEdit1.text())
        q2=int(self.QLEdit2.text())
        q3=int(self.QLEdit3.text())
        sonuc=(q2)/(q1/100)
        prim = q3/sonuc
        print(prim)
        partim=int(prim)+int(q3)
        self.QLab4.setText(str(sonuc))
        self.personelprimiyazi.setText(str(partim))

app=QApplication([])
wind=Program()
wind.resize(400,400)

wind.show()
app.exec_()
