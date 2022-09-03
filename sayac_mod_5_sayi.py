# Girilen 5 adet sayıdan kaç tanesi 5'e tam bölündüğünü bulan sayaç mantığı ile programı yazınız.

say = 0
while(say < 5):
    sayi = int(input("SAYI GİRİN : "))
    sayi = sayi % 5
    say = say + 1
    if(sayi == 0):
        print("SAYI 5'E TAM BÖLÜNÜR")
    else:
        print("SAYI 5'E TAM BÖLÜNMEZ")

