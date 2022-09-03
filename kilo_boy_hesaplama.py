# Kilo boy oranına göre kilo boy endeksini hesaplayan programı yazınız.
# vki <= 19      ---> Zayıf
# 19 < vki <= 25 ---> Normal
# 25 < vki <= 30 ---> Kilolu
# 30 < vki       ---> Obez

boy = float(input("BOY 'm' : "))
kilo = float(input("KİLO 'kg' : "))
vki = kilo / (boy * boy)
if(vki <= 19):
    print("ENDEKSi : ",vki)
    print("DURUMU : 'ZAYIF'")
elif(19 < vki <= 25):
    print("ENDEKSi : ",vki)
    print("DURUMU : 'NORMAL'")
elif(25 < vki <= 30):
    print("ENDEKSi : ",vki)
    print("DURUMU : 'KİLOLU'")
elif(vki > 30):
    print("ENDEKSi : ",vki)
    print("DURUMU : 'OBEZ'")
else:
    print("YANLIŞ DEĞER GİRİLDİ")
