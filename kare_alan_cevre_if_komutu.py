# Karenin çevresini ve alanını seçim ile hesaplayan program...

print("1 - ÇEVRE HESAPLAMA")
print("2 - ALAN HESAPLAMA")
oku = int(input("SEÇENEK GİRİN 1 - 2 : "))
sayi = int(input("HESAPLANACAK SAYİYİ GİRİN : "))
if(oku == 1):
    cevre = 4 * sayi
    print("ÇEVRESİ : ",cevre)
elif(oku == 2):
    alan = sayi * sayi
    print("ALANI : ",alan)