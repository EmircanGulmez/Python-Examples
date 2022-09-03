# Saat bilgisine göre otopark ücretini hesaplayan programı yazınız.
# 0-1 Saat ---> 10 TL
# 1-5 Saat arası ---> 15 TL
# 5-10 Saat arası ---> 20 TL
# 10 Saat sonrası ---> 25 TL

print("SÜRE BİLGİSİ GİRER İKEN SAAT CİNSİNDEN NOKTA İLE BELİRTİN ÖRNEK: 4.5 'SAAT'")
saat = float(input("SAAT SÜRESİ : "))
if(0 < saat <= 1):
    print("ÖDENECEK TUTAR : 10 TL")
elif(1 < saat <= 5):
    print("ÖDENECEK TUTAR : 15 TL")
elif(5 < saat <= 10):
    print("ÖDENECEK TUTAR : 20 TL")
elif(saat > 10):
    print("ÖDENECEK TUTAR : 25 TL")
else:
    print("YANLIŞ SÜRE GİRİLDİ")
