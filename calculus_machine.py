sonuc = ""

islemKarar = True
while islemKarar:  """kodun bu kısmında işlemlerin bitip bitmediğini sürekli olarak kontrol etmek gerektiği için sonsuz bir 
                      while döngüsü oluşturdum ancak bu döngü klavyeden "e" karakteri haricinde girelen bütün karakterlerde bozuluyor."""
    
    
    def islem_secim(): # bu fonksiyon işlem seçimini ve klavyeden işlem yapılacak olan verileri alıp seçilen işleme göre sonucu ekrana yazdırmaktadır. 
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
        def islem_gecmis_kayit(): # bu işlem ile daha önce yapılan işlemleri bir .txt dosyasına kaydederek daha sonra kullanılabilmesi veya bir geçmiş olarak kullanıcıya tekrar döndürlmesi sağlanmıştır.
            
            file = open("btk/YapayZeka/islem_gecmis.txt","a")
            file.write(" Isleminiz : " + str(sayi1) + " " + str(islem) + " " + str(sayi2) +"  "+"Islem Sonucunuz :" + str(sonuc)+"\n")
            file.close()
        islem_gecmis_kayit()
    islem_secim()
    islemDevam = input("Başka İşlem Yapacakmısınız ? (e/h) : ")
    
    if islemDevam == "e": # uygulamanın kapatılıcak mı yoksa daha fazla işlem yapılıcak mı olduğunun kararını veren karar bloğu 
        pass
    else:
        print("İyi Günler :)")
        break













