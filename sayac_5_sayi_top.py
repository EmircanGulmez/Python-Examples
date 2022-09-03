# Girilen 5 sayının toplamını bulan sayaç mantığında programı yazınız.

s = 1   # döngü için sayac
t = 0   # sayı toplam için
while(s <= 5):
    sayi = float(input("SAYİ GİRİN : "))
    s = s + 1
    t = t + sayi
    if(s==6):
        print(t)
    

