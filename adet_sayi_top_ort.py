# -7 sayısı girilene kadar kaç adet sayı girildiğini, bu sayıların toplamını ve ort bulan programı yazınız.

top = 0
adet = 0
while(1):
    sayi = float(input("SAYI GİRİN :"))
    adet = adet + 1
    top = top + sayi
    ort = top / adet
    if(sayi == -7):
        print("SAYILARIN ADETİ :",adet)
        print("SAYILARIN TOPLAMI :",top)
        print("SAYILARIN ORTALAMASI :",ort)


