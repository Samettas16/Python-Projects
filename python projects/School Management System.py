class Ogrenci():
    
    dersler = ["Matematik", "fizik", "kimya", "biyoloji"]
    Matematik = 0
    Fizik = 0
    Kimya = 0
    Biyoloji = 0
    Devamsızlık = 0
    

    def __str__(self):
        print("ogrenci sistemidir. Ogrenciler buradan bilgilerine ulaşabilir.")
        pass
    
    def __init__(self,Ogrenci_isim, Ogrenci_Soyisim, Ogrenci_No):
        self.__Ogrenci_isim = Ogrenci_isim
        self.__Ogrenci_Soyisim = Ogrenci_Soyisim
        self.__Ogrenci_No = Ogrenci_No     
        pass
    
    def OgrenciNotGöster(self):
        
        print(f"Hosgeldin {self.__Ogrenci_isim}")
        print(f"Matematik = {Ogrenci.Matematik} \nFizik = {Ogrenci.Fizik} \nKimya = {Ogrenci.Kimya} \nBiyoloji = {Ogrenci.Biyoloji}")
        pass
    
    def OgrenciOrtalamaGöster(self):
        print(f"Hosgeldin {self.__Ogrenci_isim}")
        
        print("ders ortalamaların : {}".format((Ogrenci.Matematik + Ogrenci.Fizik + Ogrenci.Kimya + Ogrenci.Biyoloji) / 4))
        
        pass
    
    def OgrenciDisiplinDurumu(self):
        print(f"sayın :  {self.__Ogrenci_isim}")
        print("Şu nedenle hocan sana disiplin girdi : ",Ogretmen.disiplin_durumu)
        pass
    
    def OgrenciDevamsızlıkBilgisi(self):
        print(f"sayın :  {self.__Ogrenci_isim} devamsızlık gün sayınız : {Ogrenci.Devamsızlık}")
        if(Ogrenci.Devamsızlık <= 10):
            print("devamsızlık gün hakkınız : {}".format(10 - Ogrenci.Devamsızlık))
            pass
        else:
            print("devamsızlıktan kaldınız. İDAREYE GELİNİZ...")
        
        pass
    
    pass





class Ogretmen(Ogrenci):
    
    disiplin_durumu = ""
    
    def __str__(self):
        print("sayın öğretmenlerimiz. Kullanıcı adlarınızı ve şifrelerinizde isimleriniz vb. yazıların bulunmamsına özen gösteriniz.")
        pass
    
    def __init(self,Ogretmen_ad, Ogretmen_soyad, ogretmen_bransAD, ogretmen_No):
        self.__Ogretmen_Ad = Ogretmen_ad
        self.__Ogretmen_soyad = Ogretmen_soyad
        self.__bransAd = ogretmen_bransAD
        self.__Ogretmen_No = ogretmen_No
        
        pass
    
    def OgrenciNotGir(self):
        
        for ders in Ogrenci.dersler:
            print(ders)
            pass
        
        for i in range(len(Ogrenci.dersler)):
            
            print("yukarıda dersler Listelenmiştir. Hangi dersin notunu girmek istersiniz ? \n")
            print("1- Matematik \n2- Fizik \n3- Kimya \n4- Biyoloji")
            secim = int(input("lütfen seciniz : "))
              
            if secim == 1:
                Mnot = int(input("\nMatematik dersi notunu lütfen giriniz : "))
                Ogrenci.Matematik = Mnot
                pass
            elif secim == 2:
                Fnot = int(input("\nFizik dersi notunu lütfen giriniz : "))
                Ogrenci.Fizik = Fnot
                pass
            elif secim == 3:
                Knot = int(input("\nKimya dersi notunu lütfen giriniz : "))
                Ogrenci.Kimya = Knot
                pass
            elif secim == 4:
                Bnot = int(input("\nBiyoloji dersi notunu lütfen giriniz : "))
                Ogrenci.Biyoloji = Bnot
                pass
            else:
                print("\nHatalı giriş lütfen bilgileri tekrar girin.")
                continue
            pass
    
    def OgrenciDisiplinGir(self):
        Ogretmen.disiplin_durumu = input("Neden Disiplin giriyorsunuz ? :") 
        print("idareye başvurunuz iletilmiştir.")
        pass
    
    def OgrenciDevamsızlıkGir(self):
        gun = int(input("devamsızlık giriniz :"))
        Ogrenci.Devamsızlık = gun
        pass
    
    def OgretmenSifreDegistir(self):
        sifre = input("şifre :")
        
        while True:
            
            if (len(sifre) <= 8):
                print("lütfen sifenizi 8 karakterden kısa yapmayınız...")
                
                continue
    
            else:
                print("şifreniz başarı ile değiştirildi.")
                
                break