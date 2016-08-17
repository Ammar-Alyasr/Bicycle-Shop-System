__author__ = 'Ammar Ahmed ALYASRY'
# !/usr/bin/env python
# -*- coding: cp1254 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import json,os
import time, locale
from PyQt4 import QtCore, QtGui


# ---------- Bu alanda değişiklik yapmayınız --------
class Otopark_Otomasyonu(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Otopark_Otomasyonu, self).__init__(parent)
# --------  istenen değerleri burada tanımlanıyor ----------
        self.plaka = QLabel('AD')
        self.plaka.setStyleSheet("background-color: rgb(200, 30, 200);")#bu saatir renk veriyor

        self.TL = QLabel('TL')
        #self.cm=QLabel('m')

        self.yukseklik = QLabel('Bisikletin Sayi')
        self.yukseklik.setStyleSheet("background-color: rgb(200, 30, 200);")

        self.yer = QLabel('NOT')
        self.yer.setStyleSheet("background-color: rgb(200, 30, 200);")

        self.gSaat = QLabel('Giris Saati')
        self.gSaat.setStyleSheet("background-color: rgb(200, 30, 200);")

        self.fiyat=QLabel('fiyat TL')
        self.fiyat.setStyleSheet("background-color: rgb(200, 30, 200);")

        self.cikisSaat=QLabel('Cikis Saat')
        self.cikisSaat.setStyleSheet("background-color: rgb(200, 30, 200);")
#????? ??????



# -------- Formun istenen değerleri tanımlama buraya kadar ---------
# 1) .......

# ------- Formda kullanıcıdan alınan değerler ---------
        self.plakasi = QLineEdit()
        self.plakasi.setMinimumSize(QtCore.QSize(350, 30)) #burada textbox daha genis haline getirir
        self.plakasi.setMaximumSize(QtCore.QSize(350, 30))



        self.yuksekligi = QLineEdit()
        #self.yuksekligi.setInputMask('9')     # nokta koymak icin koydum
        self.yuksekligi.setText('1')
        self.yuksekligi.setMinimumSize(QtCore.QSize(30, 30))
        self.yuksekligi.setMaximumSize(QtCore.QSize(30, 30))


        self.yeri = QLineEdit()
        #self.yeri.setReadOnly(True) #burada onemli bir yer cunki texbox durumu sadece okumak icin olsun yani orada degisiklik yaplamaz
        #self.yeri.setStyleSheet("background-color: rgb(4, 200, 186);")
        self.yeri.setMinimumSize(QtCore.QSize(350, 30))
        self.yeri.setMaximumSize(QtCore.QSize(350, 30))

        self.gSaati = QLineEdit()
        self.gSaati.setReadOnly(True)
        self.gSaati.setStyleSheet("background-color: rgb(4, 200, 186);")


        self.fiyati=QLineEdit()
        self.fiyati.setReadOnly(True)
        self.fiyati.setStyleSheet("background-color: rgb(4, 200, 186);")
        self.fiyati.setAlignment(QtCore.Qt.AlignCenter)
        self.fiyati.setMaximumSize(QtCore.QSize(350, 30))
        self.fiyati.setMinimumSize(QtCore.QSize(350, 30))


        #self.fiyati.setMinimumSize(QtCore.QSize(30, 30))
        #self.fiyati.setMaximumSize(QtCore.QSize(30, 30))
        self.cikisSaati=QLineEdit()
        self.cikisSaati.setReadOnly(True)
        self.cikisSaati.setStyleSheet("background-color: rgb(4, 200, 186);")

        self.kaydet = QPushButton('Kirala')
        #self.kaydet.setStyleSheet("background-color: rgb(200,10,100 );")

        self.cikis= QPushButton('Ger Al')
        self.temizleme= QPushButton('Temizle')

        #self.connect(self.cikis, SIGNAL('pressed()'), self.topla)
        self.connect(self.cikis, SIGNAL('pressed()'), self.zaman2)
        self.connect(self.kaydet, SIGNAL('pressed()'), self.zaman)    # Kaydet butonuna tıklandığu anda ekle isimli bir fonksiyon çağrılır.
        self.connect(self.temizleme, SIGNAL('pressed()'), self.temizle)
        #self.connect(self.cikis, SIGNAL('pressed()'), self.ekle)
        #self.connect(self.cikis, SIGNAL('pressed()'), self.ucret)


# ---------- Yukarıdaki kodu değiştirmeyiniz. Ancak ekleme yapabilirsiniz. --------
        izgara = QGridLayout()
        izgara.addWidget(self.plaka, 0, 0,)
        izgara.addWidget(self.yukseklik, 1, 0,)
        izgara.addWidget(self.yer, 2, 0,)
        izgara.addWidget(self.gSaat, 4, 0,)
        izgara.addWidget(self.fiyat, 3, 0,)
        izgara.addWidget(self.cikisSaat,5,0,)


        izgara.addWidget(self.plakasi, 0, 1,)
        izgara.addWidget(self.yuksekligi, 1, 1,)
        izgara.addWidget(self.yeri, 2, 1,)
        izgara.addWidget(self.gSaati, 4, 1,)
        izgara.addWidget(self.fiyati,3,1,)

        izgara.addWidget(self.TL,3,2)
        #izgara.addWidget(self.cm,1,2)


        izgara.addWidget(self.cikisSaati,5,1,)

        izgara.addWidget(self.kaydet, 6, 0,)
        izgara.addWidget(self.cikis, 6, 1,)
        izgara.addWidget(self.temizleme, 6, 2,)

        self.setLayout(izgara)
        self.setWindowTitle('Bisiklet Kiralik, Arac Formu')




    def zaman(self):            #burasi giris fonksiyonun basladigi yer
        dosya = open('arabalar.json','a')
        conv=self.plakasi.text().replace("ğ","g").replace("ü","u").replace("ı","i").replace("ö","o").replace("ş","s").replace("ç","c")


        self.cikisSaati.setText("")
        if conv!="" and self.yuksekligi.text()!="":
            i=self.yeri.text()
            i=i.replace("ğ","g").replace("ü","u").replace("ı","i").replace("ö","o").replace("ş","s").replace("ç","c")
            self.gSaati.setText(time.strftime("%H:%M:%S")) #giris zamani yaziyor
            dosya.write('{"citys":'+ '{'+'"yeri"'+':'+'"'+i+'"' +',' +'"numarasi"'+':'+ '"'+conv+'"' + ',' + '"zaman"'+':'+'"'+ time.strftime("%H:%M:%S") + '"'+','+'"yukseklikleri"'+':'+ self.yuksekligi.text()+'}}'+ '\n')
            self.yuksekligi.setText("")
            self.gSaati.setText("")    #islem bittikten sonra texboxlar bosalsin
            self.yeri.setText("")
            self.yuksekligi.setText("1")
            self.plakasi.setText("")
        else :
            QtGui.QMessageBox.question(self, 'Hata Mesajı',
             "Giris yapmak istediginiz kisinin adini giriniz!!", QtGui.QMessageBox.Ok)

        dosya.close()

    def temizle(self):
        self.gSaati.setText("")    #islem bittikten sonra texboxlar bosalsin
        self.fiyati.setText("")
        self.yeri.setText("")
        self.yuksekligi.setText("1")
        self.plakasi.setText("")
        self.cikisSaati.setText("")


    def zaman2(self):               #burasi cikis fonksiyonudur


        #self.cikisSaati.setText(time.strftime("%H:%M:%S"))  #cikis saati yaziyor
        if self.plakasi.text()=="":
            #print("Çıkış yapmak istediğiniz kişinin adını giriniz!!")
            QtGui.QMessageBox.question(self, 'Hata Mesajı',
             "Cikis yapmak istediginiz kisinin adini giriniz!!", QtGui.QMessageBox.Ok)
        #rer=open("arabalar.json")
        #for kk in rer :
          #  boos= json.loads(kk)
            #if self.plakasi.text()!=boos['citys']['numarasi']:
              #  QtGui.QMessageBox.question(self, 'Hata Mesajı',
               # "vgrfgrgr yapmak istediginiz kisinin adini giriniz!!", QtGui.QMessageBox.Ok)

        import json
        if os.path.exists("arabalar.json"):
            acmak=open("arabalar.json") #olusturdugum dosyayi tekrer aciyor ve satirlari okuyor
            for doc in acmak:
                veriler = json.loads(doc)
                conv=self.plakasi.text().replace("ğ","g").replace("ü","u").replace("ı","i").replace("ö","o").replace("ş","s").replace("ç","c")
#b=a.replace('1','bir').replace('2','iki').replace('3','uc').r
                if (conv==veriler['citys']['numarasi']): #burada zaten belli
                    self.cikisSaati.setText(time.strftime("%H:%M:%S"))
                    self.gSaati.setText(veriler['citys']['zaman'])  #buralarda bilgileri yaziyor
                    conv2=veriler['citys']['yeri']
                    conv2=conv2.replace("ğ","g").replace("ü","u").replace("ı","i").replace("ö","o").replace("ş","s").replace("ç","c")
                    self.yeri.setText(conv2)
                    sayilar=veriler['citys']['yukseklikleri']
                    self.yuksekligi.setText('')
                    self.yuksekligi.setText(str(sayilar))

                    girisZamani=veriler['citys']['zaman']

                    a=girisZamani[0]

                    b=girisZamani[1]
                    c=a+b   #giris saat kısmı
                    c=int(c)
                    #print(a,b)
                    f=girisZamani[3]
                    t=girisZamani[4]
                    d=f+t   #giris dakika kısmı
                    d=int(d)

                    #print(c,d)

                    cikisZamani=time.strftime("%H %M")
                    saat1=cikisZamani[0]
                    saat2=cikisZamani[1]
                    saat=saat1+saat2

                    saat=int(saat)

                    dakika1=cikisZamani[3]
                    dakika2=cikisZamani[4]
                    dakika=dakika1+dakika2
                    dakika=int(dakika)

                    #print(saat,dakika)

                    # inttime=(c*60)+d
                    # outtime=(saat*60)+dakika
                    # toplam=(outtime-inttime)/60
                    #print(toplam)
                    saat_farkı=0
                    dakika_farkı=0
                    toplam_saat=0

                    if saat > c:
                        if dakika > d:
                            dakika_farkı = dakika - d
                            saat_farkı = saat - c
                            toplam_dakika = (saat_farkı*60) + dakika_farkı
                            toplam_saat = toplam_dakika / 60
                        elif dakika < d:
                            dakika_farkı = (dakika+60) - d
                            saat = saat -1
                            saat_farkı = saat - c
                            toplam_dakika = (saat_farkı*60) + dakika_farkı
                            toplam_saat = toplam_dakika / 60

                    elif saat < c:
                        if dakika > d:
                            dakika_farkı = dakika - d
                            saat_farkı = (24 - c) + saat
                            toplam_dakika = (saat_farkı*60) + dakika_farkı
                            toplam_saat = toplam_dakika / 60
                        elif dakika < d:
                            dakika_farkı = (dakika+60) - d
                            saat = saat -1
                            saat_farkı = (24 - c) + saat
                            toplam_dakika = (saat_farkı*60) + dakika_farkı
                            toplam_saat = toplam_dakika / 60




                    #print("saat farkı:{0}, dakika farkı: {1}, toplam geçen süre saat cinsinden:{2}".format(saat_farkı, dakika_farkı,toplam_saat))
                    #print(toplam_saat)
                    toplam_saat=float(toplam_saat)
                    #print(toplam_saat)
                    sonsonuc=toplam_saat*4.0 # saatlik 3 TL alınmıştır. Saatlik ücret kaç TL ise 3 yerine onu yazınız.
                    #sonsonuc=float(sonsonuc)
                    sonsonuc=round(sonsonuc,2)

                    sonsonuc=sonsonuc*veriler['citys']['yukseklikleri']
                    sonsonuc=round(sonsonuc,2)
                    her=0
                    her=round(her,2)
                    if sonsonuc<4:
                           self.fiyati.setText("Bir saattan daha az!!\t"+"Toplam boruc:"+str(veriler['citys']['yukseklikleri']*4.0)+'. Bir kisi:4  ')


                    #print("Toplam ödenecek tutar[saatlik 3 TL için]:", sonsonuc,"Kişi başı ödenecek tutar:",her)
                    elif veriler['citys']['yukseklikleri']>1:
                        #hre=float(her)
                        her=sonsonuc/veriler['citys']['yukseklikleri']
                        her=round(her,2)
                        self.fiyati.setText('Toplam '+str(sonsonuc)+'\t'+'(Kisi basi '+str(her)+')')
                    else:
                        self.fiyati.setText(str(sonsonuc))

                    #print (type(veriler))
                    #print (veriler['citys']['yukseklikleri'])
                    veriler['citys']['cikissaati']=time.strftime("%H:%M ")
                    veriler['citys']['toplamborc']=sonsonuc
                    #print(veriler)

                    ihtiyat=open("ihtiyat.json","a")
                    json.dump(veriler, ihtiyat)
                    ihtiyat.write('\n')


                #else:
                   # QtGui.QMessageBox.question(self, 'Hata Mesajı',
                    #" yapmak istediginiz kisinin adini giriniz!!", QtGui.QMessageBox.Ok)

        if os.path.exists("arabalar.json"):
            acmak=open("arabalar.json")
            file=open("arabalar2.json","w")

            for hello in acmak:
                dates=json.loads(hello)
                i=self.plakasi.text()
                i=i.replace("ğ","g").replace("ü","u").replace("ı","i").replace("ö","o").replace("ş","s").replace("ç","c")
                if dates['citys']['numarasi']!=i:
                    json.dump(dates, file)
                    #json.dump('\n',file)
                    file.write('\n')
                #else:
                    #print("Silinecek kayıt:"+dates['citys']['numarasi'])
            acmak.close()
            file.close()
            os.remove("arabalar.json")
            os.renames("arabalar2.json","arabalar.json")


uygulama = QApplication([])
pencere = Otopark_Otomasyonu()
pencere.show()
uygulama.exec_()
