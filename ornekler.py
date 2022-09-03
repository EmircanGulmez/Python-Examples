'''
def fonk(parametre,kere):
    print(parametre*kere)
kelime = input("string ifade : ")
kac = int(input("kaç kere yazılsın : "))
fonk(kelime, kac)

def listeler(*parametre):
    print(type(parametre),parametre)
    liste = []
    for a in parametre:
        liste.append(a)
    return liste
sonuc = listeler(10,20,30,'merhaba',3.15)
print(type(sonuc),sonuc)

def asal(a,b):
    for sayi in range(a,b+1):  # sayi
        if sayi > 1:
            for c in range(2,sayi):  # bölen
                if sayi%c == 0:
                    break
            else:
                print(sayi)
asal(100,300)

def tamBolen(sayi):
    tamBolenler = []
    for i in range(2, sayi+1):
        if sayi%i == 0:
            tamBolenler.append(i)
    return tamBolenler
print(tamBolen(20))

# Bankamatik Uygulaması
EmirHesap = {
    'ad': 'Emircan GÜLMEZ',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}
IbrahimHesap = {
    'ad': 'İbrahim Ömer ÖZTAŞ',
    'hesapNo': '12345678',
    'bakiye': 2000,
    'ekHesap': 1000
}
def paraCek(hesap, miktar):
    if hesap['bakiye'] >= miktar:   # miktar bakiyeden küçük eşit ise
        hesap['bakiye'] -= miktar
        print("Paranızı alabilirsiniz :",miktar,"\nGüncel bakiyeniz :",hesap['bakiye'])
    else:
        bakiyeTop = hesap['bakiye'] + hesap['ekHesap']
        if bakiyeTop >= miktar:     # miktar toplam bakiyeden küçük eşit ise
            ek = input("ek hesap kullanılsın mı? (e/h) : ")
            if ek == 'e':
                hesap['bakiye'] = 0
                bakiyeTop -= miktar 
                hesap['ekHesap'] = bakiyeTop
                print("Paranızı alabilirsiniz :",miktar,"\nGüncel hesap bakiyeniz :",hesap['bakiye'],"\nGüncel ek hesap bakiyeniz :",hesap['ekHesap'])
            elif ek == 'h':
                print(hesap['hesapNo'],"nolu hesabınızda yeterli bakiye bulunmamaktadır..")
        else:
            print(hesap['hesapNo'],"nolu hesabınızda bakiye yetersiz..")
paraCek(EmirHesap, 3060)
'''

