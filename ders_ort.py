# 2 yazılı, 2 perfonmans, 1 proje ort hesaplayan ve sınıfı geçtiği ya da kaldğı programı yazınız.

yaz1 = int(input("YAZILI 1: "))
yaz2 = int(input("YAZILI 2: "))
per1 = int(input("PERFORMANS 1: "))
per2 = int(input("PERFORMANS 2: "))
prj = int(input("PROJE: "))
ort = (yaz1+yaz2+per1+per2+prj)/5

if(ort <= 100):
    print("ORTALAMA SONUCU:",ort)
    if(ort >= 50):
        print("GEÇTİ")
    else:
        print("KALDI")
else:
    print("100'DEN BÜYÜK SAYI GİRİLDİ")