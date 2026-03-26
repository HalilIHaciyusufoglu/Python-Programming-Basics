# girilen 5 sayinin ortalamasini bulan program
def ortalama():
    list=[]
    for i in range(5):
        sayi=int(input("sayi giriniz:"))
        list.append(sayi)
    ortalama=sum(list)/5
    return ortalama
print(ortalama())        

# girilen sayının mutlak degerini bulan program
def Mutlak(N):
    sayi=abs(N)
    return sayi
print(Mutlak(-4))

# girilen 5 sayi icindeki maks min degerleri bulan program
def MaksMin():
    list=[]
    for i in range(5):
        sayi=int(input("sayi giriniz:"))
        list.append(sayi)
    maks=max(list)
    minimum=min(list)
    return maks,minimum
print(MaksMin())


# N e kadarki tek sayilari yazdıran program
def nTek(N):
    list=[]
    for i in range(1,N+1,2):
        list.append(i)
    return list
print(nTek(17))

# Girilen sayinin tam bolenleri bulan program
def Bolen(sayi):
    list=[]
    for i in range(1,sayi+1):
        if sayi%i==0:
            list.append(i)
    return list
print(Bolen(25))



# girilen n degerine gore fibonacci serisinin ilk n terimi hesaplayiniz (özyinelemeli)
def Fib(n):
    if n==1 or n==2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
print(Fib(4))

# Girilen sayinin asal olup olmadigini bulunuz
def asalmi(sayi):
    asalmi=True
    for i in range(2,sayi):
        if sayi%i==0:
            asalmi=False
            break
    if asalmi==True:
        return True
    else:
        return False
print(asalmi(5))
        

# girilen cumleyi ters ceviren program
def Reverse(cumle):
    reverse=cumle[::-1]
    return reverse
print(Reverse("bu cumleyi ters cevir"))

# Girilen cümledeki sesli ve sessiz harf sayısını bulun?
def SesSiz(cumle):
    sesliharf = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    sessiz = 0
    sesli = 0
    for harf in cumle:
        if harf == " ":  
            continue
        if harf in sesliharf:  
            sesli += 1
        else:  
            sessiz += 1
    return sessiz, sesli

print(SesSiz("merhaba ben ege"))


# Girilen cümledeki harflerin adetlerini ekrana yazın? 
def HarfAdet(cumle):
    harfadet=0
    for i in cumle:
        if i!=" ":
            harfadet+=1
    return harfadet
print(HarfAdet("cumledeki harf adet"))

# girilen metindeki bosluklari continue ifadesiyle silen kod.Karakterler yan yana yazilacak
def ContinueIleSil(cumle):
    bosluk=" "
    for i in cumle:
        if i==" ":
            continue
        bosluk+=i
    return bosluk
print(ContinueIleSil("merhaba ben ege"))


# Girilen sayının Pronic (ardışık iki sayının çarpımına eşit) olup olmadığını bulunuz
def Pronic(sayi):
    for i in range(1,sayi):
        if i*(i-1)==sayi:
            return True
    return False
print(Pronic(56))

# N’e kadar ki Harshad (sayının kendisi rakamları toplamına bölünüyor) olanları listele?
def Harshad(N):
    liste = []
    for i in range(1, N + 1):
        toplam = 0
        orijinal = i  
        while orijinal > 0:
            digit = orijinal % 10
            toplam += digit
            orijinal //= 10
        if i % toplam == 0:  
            liste.append(i)
    return liste

print(Harshad(36))


# 1 den 100e kadar asal sayilari listele
def isPrime(): 
    liste=[]
    for i in range(2,101):
        asalmi=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                asalmi=False
                break
        if asalmi==True:
            liste.append(i)
    return liste

print(isPrime())


#Sayı tahmin oyunu
import random
def Tahmin():
      hak=5
      sayi=random.randint(1,12)
      while hak>0:
            tahmin=int(input("tahmin girin:"))
            if tahmin!=sayi:
                  hak-=1
                  print(f"bilemediniz kalan hak{hak}")
                  
            else:
                print("tebrikler bildiniz")
                break
      if hak==0:
            print(f"hakkınız bitti sayi {sayi}")
Tahmin()

# kullanıcıdan alınan sayılar (q harfine basana kadar almaya devam edecek) bir listeye alın ve input alma işlemi bittiginde listedeki ekenanların aritmetik ort hesaplayan program
def aritmetik_ort():
    sayilar = []  
    print("Sayilari girin (q ile cikis yapabilirsiniz):")
    
    while True:
        sayi=(input("sayi giriniz:"))
        if sayi=="q":
            break
        sayilar.append(int(sayi))
    ort=sum(sayilar)/len(sayilar)
    return ort
print(aritmetik_ort())

# kullanıcıdan alınan cumle icinde belirli kelime var mı yok mu kontrolu yapan kod aranacak kelime de kullanıcıdan alınacak
def WordCheck(cumle,aranan):
    if aranan in cumle: 
        return "Aranan kelime cumlede var"
    else:
        return "Aranan kelime cumlede yok"
print(WordCheck("merhaba ben ege","ege"))




       

# Tam sayı değerleri olan m elemanlı bir listedeki sayıları basamak değerlerine dönüştüren,          
# sonra basamak değerlerinin toplamını geri döndüren programı yazınız? ([454, 10002, 20])) → 3 + 5 + 2 ⇒ 10
def BasDegerDonustur(m):
    list=[]
    toplam=0
    for i in range(m):
        sayi=int(input("sayi giriniz:"))
        list.append(sayi)
        while sayi>0:
            digit=sayi%10
            toplam+=1
            sayi//=10
    return toplam
print(BasDegerDonustur(3))


# Üç basamaklı rakamları birbirinden farklı sayıları liste halinde döndüren programı yazınız?  
def UcBas():
    list=[]
    for i in range(1,1000):
        son=i%10
        orta = (i // 10) % 10
        bas = (i // 100) % 10
        if (bas!=orta)and (orta!=son) and (son!=bas):
            list.append(i)
    return list
print(UcBas())

# Listeyi tersine ceviren kod
def ReverseList(liste):
    reversedList = liste[::-1]
    return reversedList

print(ReverseList([1, 2, 3, 4, 5]))


def faktoriyel():
    print("0!=1")
    print("1!=1")
    carpim=1
    for i in range(2,10):
        carpim*=i
        print(f"{i}!={carpim}")
    
faktoriyel()

def fak():
    for i in range(10):
        carpim=1
        for j in range(1,i+1):
            carpim*=j
        print(f"{i}!={carpim}")        
fak()

# Sayı tahmin oyunu         
import random
def Tahmin():
    sayi=random.randint(1,30)
    hak=5
    while hak>0:
        tahmin=int(input("tahmin gir:"))
        if sayi!=tahmin:
            hak-=1
            print(f"bilemediniz tekrar deneyiniz kalan hak {hak}")
        
        else:
            print("tebrikler bildiniz")
            break
    if hak==0:
        print(f"maalesef sayi {sayi}idi")
    return "oyun bitti"
Tahmin()



#  Verilen m, a ve b parametrelerini kullanarak, m adet tam sayı            
#  içeren bir liste oluşturunuz. Sayılar [a-b] aralığında olmalı.
import random
def generate_random_numbers(m, a, b):
    numbers_list = []  
    for i in range(m):  
        sayi = random.randint(a, b) 
        numbers_list.append(sayi) 
    return numbers_list
print(generate_random_numbers(2,6,10))

# # Başlangıç Saat, Dakika ve Saniye bilgileri verildiğinde         
# #  ilk 5 saniyelik saat bilgisini listeye ekleyen fonsiyonu yazınız?
# #  Çıktı: ['18.23.58','18.23.59','18.24.0','18.24.1','18.24.2']
def Clock(saat,dakika,saniye):
    list=[]
    for i in range(5):
        saniye+=1
        if saniye==60:
            dakika+=1
            if dakika==60:
                saat+=1
                if saat==24:
                    saat=0
        list.append(f"{saat}.{dakika}.{saniye}")
    print(list)
Clock(10,24,48)

# Uzunlugu cift olan ve tam sayi degerler iceren bir liste verildiginde
# 0. ve 1. elemanları,2. ve 3. elemanlı,4.ve5. elemanları,... yer degistiren prog
def yer_degistir(liste):
    # Listenin uzunluğunun çift olduğuna emin olalım
    if len(liste) % 2 != 0:
        print("Liste uzunluğu çift olmalı.")
        return None

    # 0. ve 1., 2. ve 3., 4. ve 5. vb. elemanları yer değiştir
    for i in range(0, len(liste), 2):
        liste[i], liste[i+1] = liste[i+1], liste[i]

    return liste




# Verilen bir cümledeki türkçe karakterleri ingilizce karşılıklarına 
#  dönüştüren programı yazınız? Harflerin hepsinin küçük olduğunu düşünelim
def turkce_karakterleri_degistir(cumle):
    
    turkce_karakterler = {
        'ç': 'c',
        'ğ': 'g',
        'ı': 'i',
        'İ': 'i',
        'ö': 'o',
        'ş': 's',
        'ü': 'u',
        'Ç': 'c',
        'Ğ': 'g',
        'Ö': 'o',
        'Ş': 's',
        'Ü': 'u'
    }
    
    
    yeni_cumle = ""
    for karakter in cumle:
        if karakter in turkce_karakterler:
            yeni_cumle += turkce_karakterler[karakter]  
        else:
            yeni_cumle += karakter 
    
    return yeni_cumle



# Verilen bir cümledeki büyük ve küçük harf sayısını bulan programı yazınız? Cümlenin sadece       
# İngilizce karakterler içerdiğini düşünelim. ASCII karakterleri aşağıdaki gibidir:  ‘a’🡺97, ‘z’🡺122, ‘A’🡺65,‘Z’🡺90
def BuyukKucuk(cumle):
    buyuk=0
    kucuk=0
    for i in cumle:
        if (ord(i)>=65 and ord(i)<=90):
                buyuk+=1
        elif (ord(i)>=97 and ord(i)<=122):
                kucuk+=1
    return f"buyuk {buyuk}, kucuk {kucuk}"
print(BuyukKucuk("merhAba beN EGE"))



# Üç basamaklı rakamları birbirinden farklı sayıları liste halinde döndüren programı yazınız?  
def UcBas():
    liste=[]
    for i in range(100,1000):
        birler=i%10
        onlar = (i // 10) % 10
        yuzler = (i // 100) % 10
        if birler!=onlar and birler!=yuzler and onlar!=yuzler:
            liste.append(i)
    return liste
print(UcBas())


# Girilen cümledeki harflerin adetlerini ekrana yazın?
def harfAdet(cumle):
    adetler = {}  # Boş bir sözlük oluştur
    for harf in cumle:
        if harf != " ":  # Boşlukları göz ardı et
            if harf in adetler:
                adetler[harf] += 1  # Harf zaten sözlükte varsa, sayısını 1 artır
            else:
                adetler[harf] = 1  # Harf yoksa, ilk kez ekle
    return adetler



# baslangic ve bitis sayilari arasinda adet        
# # kadar rastgele tam sayi uretip listeyen ekleyen program
import random
def SayiUret(a,b):
      liste=[]
      for i in range(a,b):
            sayi=(random.randint(a,b))
            liste.append(sayi)
      return liste
print(SayiUret(2,10))

# kullanıcıdan alınan sayılar (q harfine basana kadar almaya devam edecek) bir listeye alın  
def Kullanici():
      liste=[]
      while True:
            sayi=input("sayi giriniz cikis icin q ya basiniz")
            if sayi=="q":
                  break
            liste.append(int(sayi))
      return liste
print(Kullanici())

# kullanıcıdan alınan cumle icinde belirli kelime var mı yok mu kontrolu yapan kod aranacak kelime de kullanıcıdan alınacak
def k(cumle):
      kelime=str(input("kelimeye giriniz"))
      if kelime in cumle:
            return "kelime cumlede var"
      else:
            return "kelime cumlede yok"
print(k("merhaba ben ege"))




#def BozanElamanIndeksi(Liste):
#6) Artış miktarı sabit olan aritmetik bir seri liste şeklinde verildiğinde örüntüyü bozan elemanın indeksini dönderiniz?
# KOD BURAYA YAZILACAK
#return Indeks
#----------------------------------------------------------------------------------------------------
#Örnek kod: print(BozanElamanIndeksi([1,3,5,7,9,12,13]))
#Çıktı: 6
def VizeBozanElamanIndeksi(Liste):
    fark1 = []
    fark2 = []
    for i in range(1,len(Liste)):
        fark1.append(Liste[i]-Liste[i-1])
    for i in range(1,len(fark1)):
        fark2.append(fark1[i]-fark1[i-1])        
    indeks = 1
    for i in fark2:    
        if i!=0:
            break
        indeks+=1
        
    return indeks+2


#1) Verilen m, a ve b parametrelerini kullanarak, m adet
#tam sayı içeren bir liste oluşturunuz. Sayılar [a-b]
#aralığında olmalı. NOT: randint komutu kullanılmayacak.
#def ListeOlustur(m,a,b):
#…
#return Liste
#--------------------------------------------------
#Örnek kod: print(ListeOlustur(5,3,8))
#Çıktı: [4, 4, 3, 7, 8]
import random
def ListeOlustur(m,a,b):
    Liste=[]
    for i in range(m):
        sayi=random.random()
        sayi=sayi*(b-a)+a
        Liste.append(sayi)
    return Liste
print(ListeOlustur(5,3,8))

#2) Tam sayı değerleri olan m elemanlı bir listede 1. ve m.,
#2. ve m-1., 3. ve m-2. elemanları toplayarak yeni bir liste
#üretiniz. Liste boyutu tek olduğunda ortanca elemanı yeni
#listeye direk ekleyiniz.
#def Topla(Liste):
#…
#return Liste
#--------------------------------------------------
#Örnek kod: print(Topla([4,1,2,8,3,5,9,3,1]))
#Çıktı: [5,4,11,13,3]
def Topla(liste):
    y=[]
    m=len(liste)
    for i in range(m//2):
        y.append(liste[i] + liste[m-i-1])
    if m%2==1:
        y.append(liste[m//2])
    return [y]
print(Topla([2,4,6,7,84,5,2]))


#Verilen bir cümledeki türkçe karakterleri ingilizce
#karşılıklarına dönüştüren programı yazınız? Harflerin
#hepsinin küçük olduğunu düşünelim.
#def Tr2Eng(cumle):
#…
#return ncumle
#--------------------------------------------------
#Örnek kod: print(Tr2Eng(‘hayırlı günler’))
#Çıktı: ‘hayirli gunler’
def Tr2Eng(cumle):
    ncumle = ''
    List = ['ı','ö','ü','ş','ç']
    Dict = {'ı':'i','ö':'o','ü':'u','ş':'s','ç':'c'}
    for i in cumle:
        if i in List:
            ncumle = ncumle + Dict[i]
        else:
            ncumle = ncumle + i
    return ncumle
print(Tr2Eng('hayırlı günler'))


#6) Tam sayı değerleri olan m elemanlı bir listedeki sayıları basamak değerlerine dönüştüren, sonra basamak
#değerlerinin toplamını geri döndüren programı yazınız?
#def BasamakDegeri(Liste):
#…
#return toplam
#--------------------------------------------------
#Örnek kod: print(BasamakDegeri([454, 10002, 20])) → 3 + 5 + 2 ⇒ 10
def BasamakDegeri(Liste):
    def basamak(n):
        k=0
        while n>0:
            k+=1
            n = n//10
        return k

    top = 0
    for i in Liste:
        top += basamak(i)
    
    return top


##2) Üç basamaklı rakamları birbirinden farklı sayıları
#liste halinde döndüren programı yazınız?
#def UcBasamakli():
#…
#return Liste
#--------------------------------------------------
#Örnek kod: print(UcBasamakli())
#Çıktı: 102 103 104 105 106 107 108 109 120 123 . . . . .
#980 981 982 983 984 985 986
def UcBasamakli():
    Liste=[]
    for i in range(100,1000):
        birler=i%10
        onlar=((i//10)%10)
        yüzler=((i//100))
        if birler!=onlar and birler!=yüzler and onlar!=yüzler:
            Liste.append(i)
    return Liste
print(UcBasamakli())



#3) Verilen para miktarını 100, 50, 20, 10 ve 1 TL bozuk
#paralara dönüştüren programı yazınız? Büyük değerli
#bozuklar öncelikli olmalı. Çıktı liste olmalı ve bozukların
#adetlerini sırayla içermeli.
#def ParaBozdur(para):
#…
#return Liste
#--------------------------------------------------
#Örnek kod: print(ParaBozdur(2458))
#Çıktı: [24, 1, 0, 0, 8]
def ParaBozdur(para):
    Liste = [0,0,0,0,0]
    while para>0:
        if para >= 100:             
            Liste[0]+=1
            para -= 100
        elif para >= 50:             
            Liste[1]+=1
            para -= 50
        elif para >= 20:            
            Liste[2]+=1
            para -= 20
        elif para >= 10:            
            Liste[3]+=1 
            para -= 10
        else:
            Liste[4]=para
            para = 0
    return Liste
print(ParaBozdur(2132))



