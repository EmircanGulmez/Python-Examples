# Girilen sayının faktoriyelini bulan sayac mantığı ile programını yazınız.

carp = 1
sayi = int(input("SAYI GİRİN : "))
while(sayi >= 1):
    carp = carp * sayi
    sayi = sayi - 1
print(carp)