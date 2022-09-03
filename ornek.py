'''
# inheritance (kalıtım)
class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("person created")

class Student(Person):
    def __init__(self, fname, lname, snumber):
        Person.__init__(self, fname, lname)   # super().__init__(fname, lname) -> super metoduylada yazılabilir.
        self.number = snumber
        print("student created")

p1 = Person("Emir","Gülmez")
s1 = Student("İbram","Öztaş",1234)

print(p1.firstName, p1.lastName)
print(s1.firstName, s1.lastName, s1.number)
'''


# OOP Örnek
'''
OOP ve modül kullanarak 5 adet araba markaları ve özellikleriyle sırasıyla gösterilecektir bilgi alma işlemleri
modül içerisinden yapılacaktır

'''
'''
# oluşturduğumuz arabaModul.py dosyasını kullanarak işlem yapılır
import arabaModul

# result = dir(arabaModul)
# result = arabaModul.models["araba 1"]["model"]
# print(result)

class arabalar():
    print("arabalar class")
    
    def __init__(self, giris):
        self.giris = giris
        print("default class")

    def modul(self):
        print("modul class")
        return arabaModul.models[giris]["model"]

while True:
    giris = input("giris : ")

    # araba objesi
    araba = arabalar(giris)
    print(araba.modul())


from ast import While
import re
from unittest import result
liste = ["1","2","5a","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.
for i in liste:
    try:
        result = int(i)
        print(result)
    except ValueError:
        continue

# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı 
# olduğundan emin olunuz aksi halde hata mesajı yazın.
while True:
    veri = input("Sayısal değer giriniz : ")
    if veri == 'q':
            break
    try:
        result = int(veri)
    except Exception as ex:
        print("Hata :",ex)
    else:
        print("Alınan değer sayısaldır.")

# 3: Girilen parola içinde türkçe karakter hatası veriniz.
turkceKarakterler = "ıöüğşçİÇÖÜĞŞ"
parola = input("Parola giriniz : ")
for i in parola:
    if i in turkceKarakterler:
        raise Exception("parolada türkçe karakter vardır")
print("Parolada tamamdır.")

# 4: Faktoriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.
# negatif, str vb.
def fak(x):
    x = int(x)
    if x < 0:
        raise ValueError("Negatif değer")
    sonuc = 1
    for i in range(1, x+1):
        sonuc *= i
    return sonuc
for x in [5, 10, 20, -3, '10a']:
    try:
        y = fak(x)
    except ValueError as eer:
        print(eer)
        continue
    print(y)

# Öğrenci notları giriş dosya kaydetme okuma ve harf notu hesaplama...
def notHesapla(dosya):
    dosya = dosya[:-1]
    liste = dosya.split(' : ')

    ogrenci = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ort = (not1 + not2 + not3) / 3

    if ort <= 100 and ort >= 90:
        harf = 'AA'
    elif ort <= 89 and ort >= 85:
        harf = 'BA'
    elif ort <= 84 and ort >= 80:
        harf = 'BB'
    elif ort <= 79 and ort >= 75:
        harf = 'CB'
    elif ort <= 74 and ort >= 70:
        harf = 'CC'
    elif ort <= 69 and ort >= 65:
        harf = 'DC'
    elif ort <= 64 and ort >= 60:
        harf = 'DD'
    elif ort <= 59 and ort >= 50:
        harf = 'FD'
    elif ort <= 49:
        harf = 'FF'
    else:
        harf = "Hata..."
    return ogrenci + " : " + harf + "\n"

def ortOku():
    with open("ogrenci_notlari.txt","r",encoding="utf-8") as file:
        for dosya in file:
            print(notHesapla(dosya))

def notGir():
    ad = input("öğrenci adı : ")
    soyad = input("öğrenci soyadı : ")
    not1 = input("not 1 : ")
    not2 = input("not 2 : ")
    not3 = input("not 3 : ")

    with open("ogrenci_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad + ' ' + soyad + ' : ' + not1 + ',' + not2 + ',' + not3 + "\n")

def notKaydet():
    with open("ogrenci_notlari.txt","r",encoding="utf-8") as file:
        kayitListe = []

        for i in file:
            kayitListe.append(notHesapla(i))
    
        with open("ogrenciNotKayıt.txt","w",encoding='utf-8') as kaydet:
            for i in kayitListe:
                kaydet.write(i)

while True:
    islem = input("1- Ortalamaları Oku\n2- Not Gir\n3- Notları Kaydet\n4- Çıkış\n")

    if islem == '1':
        ortOku()
    elif islem == '2':
        notGir()
    elif islem == '3':
        notKaydet()
    else:
        break


# us alma, faktoriyel, çarpma, bölme, toplama, çıkarma, mod alma işlemleri kendi
# fonksiyonlarında hesaplayarak ne kadar zaman geçtiğini ile sonucu ekranda göstersin.
import math
import time

def zaman(fonksiyon):
    def ic(*arg,**kwarg):
        basla = time.time()
        time.sleep(1)
        fonksiyon(*arg,**kwarg)
        bitis = time.time()
        print("fonksiyon " + fonksiyon.__name__ + " " + str(bitis-basla) + " saniye sürdü.")
    return ic

@zaman  # altında ki fonksiyonu zaman decoratoruna gönderir ve işlem görür
def fak(num):
    print(math.factorial(num))

@zaman
def usAlma(a,b):
    print(math.pow(a,b))

@zaman
def carpma(a,b):
    print(a*b)

@zaman
def bolme(a,b):
    print(a/b)

@zaman
def modAlma(a,b):
    print(a%b)

@zaman
def cikarma(a,b):
    print(a-b)

@zaman
def toplama(a,b):
    print(a+b)

fak(5)
usAlma(5,3)
carpma(9,8)
bolme(100,5)
modAlma(10,2)
cikarma(500,90)
toplama(604,400)

from datetime import datetime
simdi = datetime.now()
sonuc = datetime.strftime(simdi,"%w")
print(sonuc)

# PC uygulama çalıştırma
import os
os.system("notepad.exe")

# https://medium.com/@ilyaskaraca/python-gui-programlama-tkinter-d63a99b43179
# pencere açma
from tkinter import *
from tkinter import messagebox
pencere = Tk()  # pencere objesini oluşturulur.
pencere.title("text")   # pencere başlığına yazı yazma
pencere.geometry("500x200") # pencere boyutu
# pencere.maxsize(500,300)  # max ayarlanabilir boyut
# pencere.minsize(500,300)  # min ayarlanabilir boyut
# pencere.resizable(width = False, height = False)  # pencere boyut ayarını kapatma

# def ButtonFunc():     # butonun işlevi
#     messagebox.showinfo("Hello Python", "Hello World")  # ekranda mesaj gösterme
B = Button(pencere, text ="Hello", background="green", activebackground="yellow")   # buton ayarlamaları
B.pack()
pencere.mainloop()  # kullanıcı pencereyi kapatana kadar açık kalmasını sağlar, kodlarda en sona yazılır.


# Öğrencilerin girilen öğrenci no ismi, vize, finali ile ortalamasını hesaplayıp 
# ve harf notu bulunacaktır. Ayrıca öğrenci notu girilirken geçen zaman hesaplanıp 
# herşey tek bir dosyaya kaydedilecektir.
import time

def zaman(fonk):
    def ic(*arg,**kwarg):
        start = time.time()
        fonk(*arg,**kwarg)
        finish = time.time()
        print("\nNot girme işlemi " + str(finish-start) + " saniye sürdü.\n")
    return ic

@zaman
def notGir():
    no = input("Öğrenci no : ")
    ad = input("Öğrenci adı : ")
    soyad = input("Öğrenci soyad : ")
    vize = input("Vize notu : ")
    final = input("Final notu : ")

    with open("ogrenciGecici.txt","a",encoding="utf-8") as file:
        file.write(no + " " + ad + " " + soyad + " : "+vize+" , "+final+"\n")

def ortOku():
    with open("ogrenciGecici.txt","r",encoding="utf-8") as file:
        for dosya in file:
            print(ortHarfHesapla(dosya))

def ortHarfHesapla(dosya):
    dosya = dosya[:-1]
    liste = dosya.split(' : ')

    ogrenci = liste[0]
    notlar = liste[1].split(' , ')

    vize = int(notlar[0])
    final = int(notlar[1])

    ort = vize*0.4 + final*0.6
    
    if ort <= 100 and ort >= 90:
        harf = 'AA'
    elif ort <= 89 and ort >= 85:
        harf = 'BA'
    elif ort <= 84 and ort >= 80:
        harf = 'BB'
    elif ort <= 79 and ort >= 75:
        harf = 'CB'
    elif ort <= 74 and ort >= 70:
        harf = 'CC'
    elif ort <= 69 and ort >= 65:
        harf = 'DC'
    elif ort <= 64 and ort >= 60:
        harf = 'DD'
    elif ort <= 59 and ort >= 50:
        harf = 'FD'
    elif ort <= 49:
        harf = 'FF'
    else:
        harf = "Hata..."
    ort = str(ort)
    return ogrenci + " : " + "\n - Ortalama : " + ort + "\n - Harf notu : " + harf + "\n"

def notKaydet():
    with open("ogrenciGecici.txt","r",encoding="utf-8") as file:
        kayit = file.read()
        with open("Öğrenci_Kayıt.txt","w",encoding="utf-8") as file1:
            file1.write(kayit)
            print("Dosya kaydetme başarılı...")

while True:
    islem = input("1- Ortalamaları Oku\n2- Not Gir\n3- Notları Kaydet\n4- Çıkış\n")
    if islem == '1':
        ortOku()
    elif islem == '2':
        notGir()
    elif islem == '3':
        notKaydet()
    elif islem == '4':
        break
    else:
        raise Exception("Hatalı giriş yapıldı...")

# turtle graphics
from turtle import *
hideturtle()
bgcolor("black")
color("greenyellow")
speed(0)
fwd = 1
while True:
    forward(fwd)
    left(143)
    fwd += 2
'''

import numpy as np

numbers2 = np.array([[0,5,10,11,12],[15,20,25,30,40],[50,75,85,86,87]])
result = numbers2[-1,:]
print(result)
