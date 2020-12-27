#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class s_s_s:
    dKayit={}
    dSayisi=0
    dOrtalama=0
    dNotlari={}
    count=3
    def __init__(self,name="",surname=""):
        self.name=name;
        self.surname=surname
    def adDegistir(self,yeniAd,yenisoyad):
        self.count-=1
        self.name=yeniAd
        self.surname=yenisoyad
    def dNotHesapla(self):
        for x,y in self.dKayit.items():
            if (y[0]*0.3+y[1]*0.5+y[2]*0.2)>=90:
                self.dNotlari[x]="AA ile Geçtin"
            elif 70<=int(y[0]*0.30+y[1]*0.5+y[2]*0.2)<90:
                self.dNotlari[x]="BB ile Geçtin"
            elif 50<=int(y[0]*0.30+y[1]*0.5+y[2]*0.2)<70:
                self.dNotlari[x]="CC ile Geçtin"
            elif 30<=int(y[0]*0.30+y[1]*0.5+y[2]*0.2)<50:
                self.dNotlari[x]="DD ile Geçtin"
            elif int(y[0]*0.30+y[1]*0.5+y[2]*0.2)<30:
                self.dNotlari[x]="FF ile Kaldın"
        for x,y in self.dNotlari.items():
            print(f"Ders Adi:{x},Ders Notu:{y}")
        
    def dTanimla(self,dAdi,midterm,final,project):
        self.dSayisi+=1
        self.dAdi=dAdi
        self.midterm=midterm
        self.final=final
        self.project=project
        self.dKayit[self.dAdi]=[self.midterm,self.final,self.project]
        

    def dKayitYazdir(self):
    
        return self.dKayit
    def dKayiKeys(self):
        count=1
        for x in self.dKayit.keys():
            print(f"Ders {count}:{x}")
            count+=1

case={
1:"1-Ad Değiştir",
2:"2-Ders Kaydı",
3:"3-Ders Notu Hesapla",
4:"4-Dersleri Göster",
"Default":"Yanlış Tuş Girişi"}
 
print("Öğrenci Kaydınızı Yapın Lütfen")
name=input("Lütfen Adınızı Giriniz:")
surname=input("Lütfen soyadınızı giriniz:")
obje=s_s_s(name,surname)
print("Öğrenci Kaydınız Başarılı.")
kontrol=True
while kontrol:
    print(f"Merhaba {obje.name} {obje.surname}")
    for x in case.values():
        if x in "Yanlış Tuş Girişi":
            pass
        else:
            print(x)
    switch=int(input("Yapmak istediğiniz işlemi seçiniz:"))
   
    if switch==1:
        if(obje.count>0):
            yeniad=input(f"{obje.count} defa adınızı ve soyadınızı değiştirebilirsiniz Yeni Ad Giriniz:")
            yeniSoyad=input(f"{obje.count} defa adınızı ve soyadınızı değiştirebilirsiniz Yeni Soyad Giriniz:")
            obje.adDegistir(yeniad,yeniSoyad)
            print(f"Adınız ve soyadınız {obje.name} {obje.surname} olarak değiştirildi")
        else:
            print("Hakkınız bitti")
    elif switch==2:
        if(obje.dersSayisi>5):
            print("Daha Fazla Ders Giremezsiniz")
        else:
            dAdi=input("Ders Adını Giriniz:")
            vize=int(input("Vize Notunu Girniz:"))
            final=int(input("Final Notunu Girniz:"))
            proje=int(input("Proje Notunu Giriniz:"))
            obje.dTanimla(dAdi,vize,final,proje)
            print("Ders Kaydınız Başarılı")
    elif switch==3:
        if(obje.dSayisi>2):
              obje.dNotHesapla()
        else:
            print(f"Ders sayınız en az 3 olmalı. sizin ders sayınız: {obje.dSayisi}")
    elif switch==4:
        if(obje.dSayisi>0):
            obje.dKayiKeys()
        else:
            print("Dersiniz Yok Lütfen ders ekleyin")
    else:
        case["Default"]
    kontrol=input("Devam Etmek İstiyor musunz E/H")
    if kontrol=="e" or kontrol=="E":
        kontrol=True
    else:
        kontrol=False
        print("Tekrar Bekleriz")

