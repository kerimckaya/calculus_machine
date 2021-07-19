sonuc = ""

islemKarar = True
while islemKarar:
    def islem_secim():
        sayi1 = int(input("1. sayıyı giriniz : "))

        islem = input("lütfen (+) (-) (*) (/) işlemlerinden birini seçiniz : ")

        sayi2 = int(input("2. sayıyı giriniz : "))

        
        
        if islem == "+":
            sonuc = sayi1 + sayi2
            print("Sonuç : ",sonuc )
        elif islem == "-":
            sonuc = sayi1 - sayi2
            print("Sonuç : ",sonuc )
        elif islem == "*":
            sonuc = sayi1 * sayi2
            print("Sonuç : ",sonuc )
        else:
            if sayi2 == 0:
                print("Hatalı Giriş Yaptınız Bölen \"0\" olamaz ")
            else:
                sonuc = sayi1 / sayi2
                print("Sonuç : ",sonuc )
        def islem_gecmis_kayit():
            
            file = open("btk/YapayZeka/islem_gecmis.txt","a")
            file.write(" Isleminiz : " + str(sayi1) + " " + str(islem) + " " + str(sayi2) +"  "+"Islem Sonucunuz :" + str(sonuc)+"\n")
            file.close()
        islem_gecmis_kayit()
    islem_secim()
    islemDevam = input("Başka İşlem Yapacakmısınız ? (e/h) : ")
    if islemDevam == "e":
        pass
    else:
        print("İyi Günler :)")
        break













