# Suyun sıcaklığı ve fiziki durumunu göstern programı yazınız.
# DURUMLAR :
# derece <= 0   ---> KATI
# derece < 100  ---> SIVI
# derece >= 100 ---> GAZ

derece = int(input("DERECE : "))
if(derece <= 0):
    print("DURUMU :'KATI'")
elif(derece < 100):
    print("DURUMU :'SIVI'")
else:
    print("DURUMU :'GAZ'")