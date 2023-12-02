class Araba():
    
    arabaMarkaları = ["Mercedes","Audi","BMW","Porshe","Bentley","Ferrari","Lamborghini"]
    
    def __str__(self):
        print("hoşgeldiniz. Öncelikle adınızı,soyadınızı,iletişim numaranızı lütfen giriniz.")
        pass
    
    def __init__(self,isim,Soyİsim,iletişimNo):
        self.__isim = isim
        self.__Soyİsim = Soyİsim
        self.__iletişimNo = iletişimNo
        
        print(f"sayın {self.__isim} {self.__Soyİsim} hoşgeldiniz.")
        
        pass
    
    def KişiBilgileriniDeğiştir(self,Yeniİsim,YeniSoyisim,YeniİletişimNo):
        self.__isim = Yeniİsim  #override
        self.__Soyİsim = YeniSoyisim  
        self.__iletişimNo =  YeniİletişimNo
        print(f"bilgiler değiştirilmiştir. yeni bilgiler : \n isim : {self.__isim} \n soyisim : {self.__Soyİsim} \n iletişim numarası : {self.__iletişimNo}")
        
        pass
    
    
    def ArabaBilgileriniAl(self,marka,model,yıl,km,fiyat):
        self.marka = marka
        self.model = model
        self.yıl = yıl
        self.km = km
        self.fiyat = fiyat
        
        print(f"sayın {self.__isim} {self.__Soyİsim} seçtiğiniz araç için bilgiler şunlardır : \n marka : {self.marka} \n model {self.model} \n yıl : {self.yıl} \n kilometre : {self.km} \n fiyat : {self.fiyat}")

        pass
    
    def ArabaMarkaListele(self):
        for araba in Araba.arabaMarkaları:
            print(araba)
            pass
        pass
    

#ilk bilgiler buradan alınacak
isim = input("isminiz :")
soyisim  = input("soyisim : ")
numara = input("tel no : ")

#instance alınan kısım
alıcı = Araba(isim , soyisim , numara)

#işlem seçme kısmı
while True:
    yapılabilecekİşlemler = ["1- Kişi bilgilerini değiştirme \n2- Araba Bilgilerini almak \n3- Araba Markalarını Listelemek \n4- Çıkış"]


    for iş in yapılabilecekİşlemler:
        print(iş)
        pass

    numara = int(input("lütfen yapmak istediğiniz işlemi seçiniz 1-3"))

    if(numara == 1):
        isim2 = input("yeni ismi giriniz :")
        soyisim2 = input("yeni soyismi giriniz :")
        numara2 = input("yeni iletişim numarasını giriniz : ")
    
        alıcı.KişiBilgileriniDeğiştir(isim2,soyisim2,numara2)
    
        pass

    elif(numara == 2):
        marka = input("Marka ismi giriniz :")
        model = input("model giriniz :")
        yıl = int(input("yıl giriniz : "))
        km = int(input("kilometre giriniz :"))
        fiyat = int((input("fiyat giriniz : ")))
        
        alıcı.ArabaBilgileriniAl(marka,model,yıl,km,fiyat)
    
        pass

    elif(numara == 3):
        print("Markalar listeleniyor .. ")
    
        alıcı.ArabaMarkaListele()
    
        pass

    elif(numara == 4):
        print("çıkış yapılıyor...")
        break

print("çıkış yapıldı")
