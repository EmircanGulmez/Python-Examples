# alış fiyatına ve kar oranına göre satış fiyatını bulan programı yazınız.

alis = int(input("ALIŞ FİYATI: "))
kar_oranı = int(input("KAR ORANI: "))
kar = (alis*kar_oranı)/100
satis = alis+kar
print("SATIŞ FİYATI :",satis)
