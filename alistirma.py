'''
https://www.yazilimkodlama.com/programlama/python-ornekleri/

print("merhaba dünya")

print("Merhaba,",input("Kullanıcı ismi : "))

a = int(input("1. sayı :"))
b = int(input("2. sayı : "))
print("Ortalama : ",(a + b)/2)

vize = float(input("Vize Notu Giriniz :"))
final = float(input("Final Notu Giriniz : "))
ort = vize * 0.4 + final * 0.6
print("Ortalama : ",ort)

yaz1 = float(input("1. Yazılı Notu Giriniz :"))
yaz2 = float(input("2. Yazılı Notu Giriniz : "))
yaz3 = float(input("3. Yazılı Notu Giriniz :"))
ort = (yaz1 + yaz2 +yaz3)/3
print("Ortalama : ",ort)

yazili = int(input("Yazii Ortalamasını giriniz :"))
if(yazili >= 50):
    print("sınıfı geçti..")
else:
    print("sınıfta kaldı..")

sayi = int(input("sayi giriniz :"))
if((sayi%2) == 1):
    print("Sayı tektir")
elif((sayi%2) == 0):
    print("Sayı çifttir")
else:
    print("nötrdür")

sayi = int(input("sayi giriniz :"))
if(sayi < 0):
    print("Sayı negatiftir")
elif(sayi > 0):
    print("Sayı pozitiftir")
else:
    print("nötrdür")
'''
"""
Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut 
kitle indeksini (VKİ=ağırlık/(boy*boy), boymetre cinsinden 
verilmeli) hesaplayınız. VKİ 18 ile < 25 aralığındaysa normal, 
VKİ 25 ile <30 aralığındaysa kilolu, VKİ 30 ve daha yüksekse 
obez, VKİ 35 ve daha fazlaysa ciddi obez olarak kabul edilir. 
VKİ’ni hesaplayarak kişinin durumunu yazdırınız
"""
'''
boy = float(input("Boy giriniz (m): "))
kilo = float(input("Kilo giriniz (kg): "))
index = kilo/(boy*boy)
if index <= 18:
   print("Durumu : zayıf // İndex :",index)
elif index > 18 and index <= 25:
   print("Durumu : normal // İndex :",index)
elif index > 25 and index < 30:
   print("Durumu : kilolu // İndex :",index)
elif index >= 30 and index < 35:
   print("Durumu : obez // İndex :",index)
elif index >= 35:
   print("Durumu : ciddi obez // İndex :",index)

yas = int(input("yas giriniz : "))
if yas >= 18:
    print("ehliyet alabilir")
else:
    print("ehliyet alamaz :(")

for i in range(1,101):  # range komutu aralık belirler 1-100 arası
    print(i)

for i in range(1,101):
    if(i%2) == 0:
        print(i)

for i in range(1,101):
    if(i%2) == 1:
        print(i)

for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print(i)

sayi = int(input("sayi giriniz : "))
for i in range(1,sayi+1):
    print(i)

a = int(input("a kenarını giriniz :"))
b = int(input("b kenarını giriniz :"))
print("Çevre :",a * b)
print("Çevre :",a*2 + b*2)

isim = input("isim giriniz : ")
for i in range(0,len(isim)):
    print(isim[i])

sayi1 = int(input("min sayi giriniz :"))
sayi2 = int(input("max sayi giriniz :"))
top = 0
for i in range(sayi1, sayi2+1):
    top = top + i
print(top)
'''
#ornek 20
'''
Kullanıcıya sinema ya da tiyatro tercihi sorulsun. Sinema izlemek 
için 15 TL, tiyatro için 10 TL ödenmesi gerekmedir. Öğrencilere %50 
indirim yapıldığı düşünülerek öğrenci ise indirim yapılan; öğrenci 
değilse indirimsiz tutarı hesaplayarak ekrana yazdıran kodu yazınız.
'''
'''
sinema = 15
tiyatro = 10
tercih = input("Sinema mı tiyator mu? : ")
ogrenci = input("Öğrenci iseniz evet yazınız değilseniz hayır : ")
if tercih == "sinema":
    fiyat = sinema
    if(ogrenci == "evet"):
        fiyat = fiyat *50 /100
elif tercih == "tiyatro":
    fiyat = tiyatro
    if(ogrenci == "evet"):
        fiyat = fiyat *50 /100
else:
    print("hatalı giriş...")
print("ücretiniz :",fiyat,"TL")

sayi = int(input("sayi giriniz :"))
a = 0
for i in range(2,sayi):
    if sayi%i == 0:
        a += 1
        break
if a == 0:
    print("asal sayıdır")
else:
    print("asal sayı değildir")

sayi = int(input("Sayi giriniz : "))
tek = cift = 0
for i in range(1, sayi):
    if i%2 == 0:
        cift += i
    else:
        tek += i
print("tek sayıların toplamı : ",tek)
print("cift sayıların toplamı : ",cift)

yeniMaas = 0
maas = int(input("Maaş giriniz : "))
zam = int(input("Zam oranını giriniz (%): "))
yeniMaas = maas + (maas*zam/100)
print("Zamlı maaşı : ",yeniMaas)

def daireAlan(yaricap):
    alan = float(yaricap) *float(yaricap) *3.141592
    print("Darire alanı :",alan)
r = float(input("Yarı çapı giriniz : "))
daireAlan(r)

def dikdortgenAlan(yukseklik,genislik):
    alan = yukseklik * genislik
    print("\nDikdörtgen alanı :",alan)
yukseklik = int(input("Yükseklik giriniz : "))
genislik = int(input("Genislik giriniz : "))
dikdortgenAlan(yukseklik,genislik)

# sayı tamini oyunu
import random
sayi = random.randint(1,100)
while 1:
    tahmin = int(input("Tahmin : "))
    if tahmin < sayi:
        print("yukarı...")
    elif tahmin > sayi:
        print("aşağı...")
    else:
        print("buldun tebrikler...")
        break

#Verilen bir tarihin yılın kaçıncı günü olduğunu bulan program
tarih = [31,28,31,30,31,30,31,31,30,31,30,31]
toplam = 0
gun = int(input("gun giriniz :"))
ay = int(input("ay giriniz :"))
if gun <= 31 and ay <= 12:
    for i in range(0,ay-1):
        toplam += tarih[i]
    print(toplam+gun)
else:
    print("hatalı tarih girişi oldu...")

sayilar = [18,22,15,85,65,30,10,20,32,34,28,101,5,4,32]
adet = 0
for i in range(len(sayilar)):
    if sayilar[i]%5 == 0:
        adet+=1
        print(sayilar[i]," : 5'in katıdır")
print("5'in katı olan sayı adeti :",adet)

def karakter(met,istenen):
    for char in met:
        if char == istenen:
            return True
            break
metin = input("Metin yazınız : ")
istenilen = input("Bulunacak karakter : ")
karakter(metin,istenilen)
if karakter(metin,istenilen) == True:
    print(istenilen,"karakteri metin içinde var...")
else:
    print("istenilen karakteri metin içinde yok...")

minDeger = int(input("Min değer giriniz :"))
maxDeger = int(input("Max değer giriniz :"))
ort = 0
top = 0
for i in range(minDeger,maxDeger):
    if i%2 == 0:
        top += i
        ort = top/(maxDeger-minDeger)
print(ort)

# pencere açmak
import tkinter            # tkinter kütüphanesi çağırılır
pencere = tkinter.Tk()    # Tk() sınıfından pencere adlı bir obje üretilir.
pencere.mainloop()        # kodun sınırsız döngü olarakçalışması için

# sayı tamini oyunu
import random
sayi = random.randint(1,100)
hak = int(input("Ne kadar hak istiyorsun? :"))
if hak >= 10:
    print("Sence de fazla hak almadın mı? Neyse...")
say = 0
while hak > 0:
    tahmin = int(input("Tahmin : "))
    say += 1
    hak -= 1
    if tahmin == 0:
        print("Oyun iptal edildi...")
        break
    if tahmin < sayi:
        print("Hakkın : ",hak)
        print("Yukarı...")
    elif tahmin > sayi:
        print("Hakkın : ",hak)
        print("Aşağı...")
    else:
        print(f"Tebrikler {say}. defada bildiniz...")
        break
if hak == 0:
    print("Tuttuğum sayı :",sayi)
    print("Hakkın : ",hak)
    print("Oyun bitti, hakkın kalmadı...")

n = int(input("Kaç adet sayı girilecek :"))
topTek = 0
adetTek = 0
topCift = 0
adetCift = 0
while n > 0:
    sayi = int(input("sayi gir bakalım :"))
    if sayi%2 == 0:
        adetTek += 1
        topTek += sayi
    else:
        adetCift += 1
        topCift += sayi
    n -= 1
ortTek = topTek / adetTek
ortCift = topCift / adetCift
print("Tek sayıların ortalaması :",ortTek)
print("Çift sayıların ortalaması :",ortCift)

meyveler =["muz","çilek","üzüm"]
print(meyveler)

karisik = [3.141592,2.54,"CPU","WINDOWS 10",6]
print(karisik)

liste=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma"]
print(liste[4])

ders=['K','O','D','L','A','M','A']
print(ders)

liste=[3,1,2]
liste[0] = 1
print(liste)

hafta_ici=["pazartesi","salı","çarşamba","perşembe","cuma"]
print("cuma" in hafta_ici)
print("cumartesi" in hafta_ici)

sayiciklar = [10,11,12,13,14,15,16,17,18,19,20]
for i in sayiciklar:
    if i%2 == 0:    
        print(i)

sayilar=[10,11,12,13,14,15,16,17,18,19,20]
sayilar2=[21,22,23,24,25]
dizi = sayilar + sayilar2
for i in dizi:
    if i%4 == 0:
        print(i)

say = 1
while say <= 12:
    print(say,". sınıf")
    say += 1

sayi = input("sayı giriniz : ")
top = 0
for i in sayi:
    top += int(i)
print(top)

sayi = input("sayı giriniz : ")
carp = 1
for i in sayi:
    carp *= int(i)
print(carp)

liste = [10,20,30,40,50,60]
toplam = sum(liste)   # sum() listedeki elemanları toplar
adet = len(liste)
print(toplam,adet)

top = 0
while True:
    sayi = int(input("sayi giriniz : "))
    top += sayi
    if sayi == 0:
        break
print("toplam :",top)

sayi = int(input("sayi giriniz : "))
print("Sayının mutlak değeri", abs(sayi))

liste = [10,20,30,40,50,60]
print(sum(liste) / len(liste))

liste = [10,20,30,40,50,60]
top = 0
for i in liste:
    top += i
ort = top / len(liste)
print(ort)

def sayHello():

print(help(sayHello))
'''