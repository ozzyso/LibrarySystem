import os
kitaplar=[]

menu="""
[1] Kitap Ekle
[2] Kitap Çıkar
[3] Kitap Listele
[q] Programdan Çık
"""

def kitapEkle(kitaplar,kitap):
    kitaplar+=[kitap] #girilen kitabın halihazırda olup olmadığına bakmak lzm önce
    print("Kitap Ekleme Başarılı")
    print("Ana menüye dönmek için enter'a basın")
    input("")

def kitapCikar(kitaplar,kitap):
    for i in kitaplar:
        if(i==kitap):
            kitaplar.remove(kitap)
    bitis=len(kitaplar)
    if(bitis<baslangic):
        print("Kitap çıkarma işlemi tamamlandı")
        print("Ana menüye dönmek için enter'a basın")
        input("")
    else:
        print("Kitap listede bulunamadı")
        print("Ana menüye dönmek için enter'a basın")
        input("")

def kitapListele(kitaplar):
    for i in kitaplar:
        print("Kitap Adı:{}".format(i)) #for un altında olmalı, olmadan dene!!
    print("Ana menüye dönmek için enter'a basın")
    input("")    

def cikis(i):
    quit()

while True:
    os.system("cls")
    print(menu)
    secim=input("Lütfen seçim yapın: ")
    if(secim=="1"):
        kitap=input("Kitap adı giriniz: ")
        kitapEkle(kitaplar,kitap)
    elif (secim=="2"):
        kitap=input("Kitap adı giriniz: ")
        kitapCikar(kitaplar,kitap)
    elif (secim=="3"):
        kitapListele(kitaplar)
    elif (secim=="q" or secim=="Q"):
        cikis()



