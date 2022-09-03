# Girilen 10 adet sayıdan kaç tanesinin hem 3'e hemde 5'e tam bölündüğünü bulan sayaç mantığıyla programı yazınız.

say = 0
while(say < 10):
    sayi = int(input("SAYI GİRİN : "))
    sayi1 = sayi % 3
    sayi2 = sayi % 5
    say = say + 1
    if(sayi1 == 0 and sayi2 == 0):
        print("SAYI HEM 3'E HEMDE 5'E TAM BÖLÜNÜR")
    else:
        print("SAYI HEM 3'E HEMDE 5'E TAM BÖLÜNMEZ")

