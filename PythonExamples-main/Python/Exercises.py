#Girilen sayının pozitif ya da negatif olduğunu ekrana yazınız
sayi=int(input("sayi giriniz:"))
if sayi < 0 :
    print("sayi negatif")
elif sayi > 0:
    print("sayı pozitif")
else:
    print("sayi ne negatif ne de pozitif")

#Vize ve Final notu girilen öğrencinin geçip geçmediğini
#hesaplayan program (vizenin %40,finalin %60’ı hesaplanır.
#Final en az 60 olmak zorundadır,vize+final 55ten büyük olmalıdır.)
vize=int(input("vize notunu giriniz"))
final=int(input("final notunu giriniz"))
vize1=(vize*40)/100
final1=(final*60)/100
toplamnot=vize1+final1
if final >=60 and toplamnot >=55 :
    print("gectiniz")
else:
    print("kaldiniz")

#girilen sayinin mutlak degerini bulan program
sayi=int(input("sayi giriniz:"))
if sayi<0:
    print("sayinin mutlak degeri:",sayi*-1)
elif sayi>0:
    print("sayinin mutlak degeri:",sayi)
else:
    print("sayiniz 0")

# #girilen sayının mutlak degerini bulan program (abs)
sayi=int(input("sayi giriniz:"))
mutlak=abs(sayi)
print("sayinin mutlak degeri:",mutlak)

#Kullanıcının girdiği üç sayıdan büyük olanını yazdıran program?   
sayi1=int(input("sayi1 giriniz :"))
sayi2=int(input("sayi2 giriniz :"))
sayi3=int(input("sayi3 giriniz :"))
a=[]
a.append(sayi1)
a.append(sayi2)
a.append(sayi3)
en_buyuk_sayi = max(a)
print("En buyuk sayi:", en_buyuk_sayi)

#Girilen sayının 6'nın katı olduğunu bulan program?
num=int(input("sayi giriniz"))
if num % 6==0:
    print("sayi 6nin kati")
else:
    print("sayi 6nin kati degil")

#Ekrana 1:Toplama, 2:Çıkarma,..yaz. Sonra kullanıcıdan iki sayı alıp işlemi seçerek sonucu ekranda yazan program?
print("1:Toplama") 
print("2:Cikarma")
print("3:Carpma")
print("4:Bolme")
secim=int(input("Yapmak istediginiz islemin numarasini secin :"))
num1=int(input("sayi1 giriniz:"))
num2=int(input("sayi2 giriniz:"))
if secim == 1:
    print(num1+num2)
elif secim==2:
    print(num1-num2)
elif secim==3:
    print(num1*num2)
elif secim==4:
    print(num1/num2)


# #Fahrenheit olarak girilen sicakligi celciusa ceviren ve 
# 0<a<15 soguk,15<a<25 ilik,a>=25 sicak olarak degerlerine bulan program (Fahrenheit alt degeri -459.67 olacak sekilde bulunuz)

F=int(input("derece giriniz:"))
if F<= -459.67:
    print("fahrenheit alt sinirindan kucuk deger girdiniz")
C=(F-32)/1.8000
print("girdiginz fahrenheit =",C)

if C>=0 and C<=15:
    print("hava soguk")
elif C<15 and C>25:
    print("hava ilik")
elif C>=25 :
    print("hava sicak")


#Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve
#çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız.
k=[]
t=[]
sayii=int(input("sayi giriniz :"))
for i in range(1,sayii+1):
    if i %2==0:
        k.append(i)
for z in range(1,sayii+1):
    if z %2!=0:
        t.append(z)
print("Ciftlerin toplami:", sum(k))
print("Teklerin toplami:", sum(t))



#Girilen sayının tam bölenlerini bulan program?
l=[]
Deger=int(input("sayi  giriniz:"))
for i in range(1,Deger+1):
    if Deger%i==0:
        l.append(i)
print(l)

#girilen meitndeki bosluklari continue ifadesiyle silen kod.Karakterler yan yana yazilacak
a=input("metin giriniz:")
sayac=" "
for i in a:
    if i == " ":
        continue 
    sayac+=i
print(sayac)   


#Girilen bir sayının asal çarpanlarını bulan program?
num3 = int(input("Sayı giriniz:"))
asal_mi = True  
for i in range(2, num3):
    if num3 % i == 0:
        asal_mi = False
        break  
if asal_mi and num3 > 1:  
    print("Sayiniz asal.")
else:
    print("Sayiniz asal degil.")

#girilen sayinin kac basamakli oldugunu bulan program
sayi = int(input("sayi gir:"))
basamak_sayisi = len(str(sayi))
print("girilen sayının basamak sayısı:", basamak_sayisi)

#Kullanıcının girdiği üç sayıdan büyük olanını yazdıran program?   
sayi1=int(input("sayi1 giriniz :"))
sayi2=int(input("sayi2 giriniz :"))
sayi3=int(input("sayi3 giriniz :"))
a=[]
a.append(sayi1)
a.append(sayi2)
a.append(sayi3)
en_buyuk_sayi = max(a)
print("En buyuk sayi:", en_buyuk_sayi)

#girilen sayinin basamaklarini ekrana yazdirin
list=[]
a=int(input("sayi giriniz:"))
yüzler=a//100
onlar=(a%100)//10
birler=(a%10)
list.append(yüzler)
list.append(onlar)
list.append(birler)
print(f"yüzler basamağı {yüzler}")
print(f"onlar basamağı {onlar}")
print(f"birler basamağı {birler}")

#girilen sayinin basamak sayisini ve rakamlari toplamini yazdiriniz
num=int(input("lutfen sayi giriniz:"))
digit_num=0  #basamak sayisi
digit_total=0 #rakamlari toplami
while num>0:
    digit=num%10 #modunu al
    digit_num+=1 #bas sayisini 1 artır
    digit_total+=digit #rakamları toplamını modu kadar artır
    print("basamak:",digit) #basamaklari sirayla yazdir
    num=((num-digit)//10) #girilen sayidan modu cikar or 156-6=150 //10 bolum 15 yeni sayi 15... sonraki sefer 15%10=mod 5 en son 15-5=10//10=1
    
print("basamak sayisi:",digit_num)
print("rakamlari toplami:",digit_total)


#N’e kadar tek sayıları yazdıran program?
N = int(input("Bir N degeri giriniz:"))

for sayi in range(1, N + 1, 2):
    print(sayi)

#20'ye kadar olan sayıları, 10'dan küçük ve 10'dan büyük şeklindelisteleyecek Python kodu nasıl olmalıdır?
kucuk_liste = []
buyuk_liste = []

for sayi in range(1, 21):
    if sayi < 10:
        kucuk_liste.append(sayi)
    else: 
        buyuk_liste.append(sayi)
print("10'dan kucuk sayilar:", kucuk_liste)
print("10'dan buyuk sayilar:", buyuk_liste)


#Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve
#çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız.
k=[]
t=[]
sayii=int(input("sayi giriniz :"))
for i in range(1,sayii+1):
    if i %2==0:
        k.append(i)
for z in range(1,sayii+1):
    if z %2!=0:
        t.append(z)
print("Ciftlerin toplami:", sum(k))
print("Teklerin toplami:", sum(t))

#Girilen 5 sayının ortalamasını bulan program? 
liste = []

for i in range(5):
    sayi = int(input("Sayı Giriniz:"))
    liste.append(sayi)

ortalama = sum(liste) / len(liste)
print("Girilen sayıların ortalaması:", ortalama)

#iki basamakli sayinin rakamlarinin faktoriyeli
a=int(input("sayi giriniz:"))
onlar=(a%100)//10
birler=(a%10)
carpim=1
for i in range(1,onlar+1):
    carpim*=i
print(carpim)
carpma=1
for b in range(1,birler+1):
    carpma*=b
print(carpma)

#girilen cumleyi ters ceviren program
a=[]
for i in range(1):
    x=str(input("Cumleyi Girin:"))
    a.append(x)
ters=a[0][::-1]
print(f"{a[0]}ters hali:",ters)

#Serinin ilk elemanı, toplam eleman sayısını ve artış değeri girildiğinde seri sonucunu hesaplayan program? 
a=int(input("Serinin toplam eleman sayisi:"))
b=int(input("Serinin artis degeri :"))
c=int(input("Serinin ilk elemani"))
for i in range(c,c+b*a,b):
    print(i)


#Klavyeden 3 adet kenar uzunluğu giriliyor. Girilen kenar uzunlukları göz önüne 
#alındığında üçgenin çizilip çizilemeyeceğini, çizilebilir ise türünü (ikizkenar, çeşitkenar, eşkenar), 
#alanını ve çevresini hesaplayan program?

a = float(input("1. Kenar Uzunlugu: "))
b = float(input("2. Kenar Uzunlugu: "))
c = float(input("3. Kenar Uzunlugu: "))
if a + b > c and a + c > b and b + c > a:
    print("Bu kenar uzunluklariyla bir ucgen cizilebilir.")
    
   
    if a == b == c:
        print("Bu bir eskenar ucgendir.")
    elif a == b or a == c or b == c:
        print("Bu bir ikizkenar ucgendir.")
    else:
        print("Bu bir cesitkenar ucgendir.")
    
   
    s = (a + b + c) / 2
    alan = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f"ucgenin alani: {alan}")
    
    cevre = a + b + c
    print(f"ucgenin cevresi: {cevre}")

else:
    print("Bu kenar uzunluklariyla bir ucgen cizilemez.")

#tc 1.3.5.7.9 hanelerinin toplamının 7 katından,2.4.6.8 hanelerin toplamından cıkarıldıgından elde edilen sonucun %10 u bize 10. haneyi verir
#1.2.3.4.5.6.7.8.9.10 hanelerin toplamından elde edilen sonucun 10 bolumunden kalan  bize 11. haneyi verir
tc=str(input("tc giriniz:"))
list=[]
say0=0
say1=0
say2=0
for i in tc:
    list.append(i)
print(list)
for i in range(0,10,2):
    say0=say0+int(list[i])
for j in range(1,9,2):
    say1=say1+int(list[j])
for i in range(10):
    say2=say2+int(list[i])
print("10.hane:",((say0*7)-say1)%10)
print("11.hane:",say2%10)

# Sayı tahmin oyunu
import random
a=random.randint(1,100)
hak=5
while hak>0:
    sayi=int(input("tahmin giriniz:"))
    if sayi!=a:
        hak-=1
        print(f"yanlis kalan hak: {hak}")
    else:
        print("tebrikler bildiniz")
        break
if hak == 0:
    print(f"hakkiniz bitti sayi : {a}idi ")



#Girilen sayının Pronic (ardışık iki sayının çarpımına eşit) olup olmadığını bulunuz

sayi=int(input("sayi giriniz:"))
sayac=0
for i in range(1,sayi+1):
    if i*(i+1)==sayi:
        sayac=1
        break
if sayac==1:
    print("sayi pronic")
else:
    print("sayi pronic degil")



# N’e kadar ki Harshad (sayının kendisi rakamları toplamına bölünüyor) olanları listele? 

list = []
N = int(input("N degerini giriniz: "))
for i in range(1, N + 1):
    basamaktoplam = 0
    a= i
    while a > 0:
        digit = a % 10
        basamaktoplam += digit
        a =(a-digit) //10 
    if i % basamaktoplam == 0:
        list.append(i)
print(list)


    
#Girilen sayının Jumbled (komşu rakamlar arasındaki fark maksimum 1) olup olmadığını bulunuz? 
sayi=int(input("sayi giriniz:")) 
sayac=0
a=sayi%10 
sayi=(sayi-a)//10 
while sayi>0:
    sonhane=sayi%10 
    if abs(sonhane-a)>1:
        sayac=1
        break
    a=sonhane
    sayi=(sayi-sonhane)//10
if sayac==1:
    print("sayi jumbled")
else:
    print("sayi jumbled degil")

#Girilen cümledeki sesli ve sessiz harf sayısını bulun?
sesli=["a","e","ı","i","o","ö","u","ü"]
sessizSayi=0
sesliSayi=0
cumle=input("cumle giriniz")
for i in cumle.lower():
        if i in sesli:
            sesliSayi+=1
        else:
            sessizSayi+=1
print(f"sesli adedi {sesliSayi} , sessiz adedi {sessizSayi}")



#Girilen cümledeki harflerin adetlerini ekrana yazın?
yazi = input("Yazi giriniz: ")
hs = 0 
for chr in yazi:
    if (ord(chr) >= 65 and ord(chr) <= 90) or (ord(chr) >= 97 and ord(chr) <= 122):
        hs += 1
print(hs)
    

# Girilen sayının basamak değerlerinde
# k rakamı olmayanları listeleyen program?
a=int(input("a:"))
k=int(input("k:"))
while a>0:
    son=a%10
    if son!=k:
        print(son)
    a=a//10

# TC kimlik noyu 
# doğru girmeye zorlayınız? 
# (11 karakter ve tamamı sayı
tc=str(input("tc"))
rakam=[0,1,2,3,4,5,6,7,8,9]
if len(tc)!=11:
    print("11 haneli tc giriniz:")
else:
    sayac=False
    for i in tc:
        if i in rakam:
            sayac=True
            break
    if sayac==False:
        print("Tc sorunsuz")
    else:
        print("Tc sorunlu")

#Girilen sayinin basamaklarinin  carpimini bulan program
sayi = int(input("Bir sayi giriniz: "))
carpim = 1
while sayi > 0:
    digit = sayi % 10  
    print("Basamak:", digit)
    carpim *= digit  
    sayi = sayi // 10 
print("Basamaklarin carpimi:", carpim)

# kullanıcıdan alınan sayılar (q harfine basana kadar almaya devam edecek)
# bir listeye alın ve input alma işlemi bittiginde 
# istedeki ekenanların aritmetik ort hesaplayan program
 
list=[]
while True:
    sayi=input("sayi giriniz:")
    
    if sayi=="q":
        break
    list.append(int(sayi))
ortalama=sum(list)/len(list)
print(ortalama)

        
#kullanıcıdan alınan cumle icinde 
#belirli kelime var mı yok mu kontrolu yapan kod 
#aranacak kelime de kullanıcıdan alınacak
cumle=str(input("cumle giriniz:"))
belirli=str(input("kelime giriniz:"))
if belirli in cumle:
    print(f"kelimeniz:{belirli} cumleniz {cumle} icerisinde var")
else:
    print(f"kelimeniz:{belirli} cumle icinde yok")