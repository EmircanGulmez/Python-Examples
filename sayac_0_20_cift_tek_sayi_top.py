# 0 ile 20 arasındaki çift ve tek sayıların ayrı ayrı toplamını bulan sayaç mantığı ile programı yazınız.

say = 0
tek  = -1
cift = 0
tektop = 0
cifttop = 0
while(say < 10):
    say = say + 1
    tek = tek + 2
    cift = cift + 2
    tektop = tektop + tek
    cifttop = cifttop + cift
print("TEK SAYILARIN TOPLAMI :",tektop)
print("ÇİFT SAYILARIN TOPLAMI :",cifttop)
