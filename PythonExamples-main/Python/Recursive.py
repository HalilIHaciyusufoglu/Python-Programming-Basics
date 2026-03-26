# faktöriyel
def fak(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fak(n-1)
print(fak(5))   


#uslu sayi (a uzeri b =a.a.a….) hesaplama
def us(a,b):
    if b==0:
        return  1
    else:
        return a*us(a,b-1)
print(us(2,3))


#listedeki sayilarin toplami
def top(list):
    if len(list)==1:
        return list[0]
    else:
        return list[0]+top(list[1::])
print(top([2,3,4]))

#fibonacci (girilen n değeri direkt fibonaccideki değeri verecek or:n=4 icin 4. deger olan 5i verir)
def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(3))



#girilen sayidan geri sayim
def GeriSayim(n):
    if n<=0:
        return 0
    else:
        print(n)
        return GeriSayim(n-1)
print(GeriSayim(5))



#girilen sayinin rakamlari toplami
def Basamak(n):
    if n==0:
        return 0
    else:
        return n%10+ Basamak(n//10)
print(Basamak(156))



# girilen sayinin basamak sayisi
def KacBas(n):
    if n<10:
        return 1
    else:
        return 1+KacBas(n//10)
print(KacBas(156))



#listeyi ters cevir
def ReverseList(list):
    if len(list)==0:
        return []
    else:
        return [list[-1]]+ReverseList(list[:-1])
print(ReverseList([2,3,4,5]))



#dizideki cift sayilari ekle
def CiftEleman(list):
    if len(list)==0:
        return []
    elif list[0]%2==0:
        return ([list[0]] + CiftEleman(list[1:]))
    else:
        return CiftEleman(list[1:])
print(CiftEleman([2,3,4,5,6]))



#dizideki elemanlarin carpimi
def elemanCarp(list):
    if len(list)==0:
        return 1
    else:
        return list[0]*elemanCarp(list[1:])
print(elemanCarp([1,2,3]))




# a ve b arasındaki sayilarin toplam
def A_B(a,b):
    if a>b:
        return 0
    else:
        return a+A_B(a+1,b)
print(A_B(2,5))
    


#ebob
def ebob(a,b):
    if b==0:
        return a
    else:
        return ebob(b,b%a)
print(ebob(24,8))




            
#girilen sayinin asal olup olmadigini bulan prog
def asal(n,i=2):
    if n<=1:
        return False
    if n==i:
        return True
    if n%i==0:
        return False
    return asal(n,i+1)
print(asal(18))




#girilen sayinin binary karsiligi
def to_binary(n):
    if n == 0:  
        return ""
    return to_binary(n // 2) + str(n % 2)
print(to_binary(8))




#Verilen tam sayıya kadarki değerlerin toplamını
#döndüren özyinelemeli programı yazınız?
def Topla(n):
    if n==1:
        return 1
    else: 
        return n + Topla(n-1)
print(Topla(5))


#dizideki sayilari kucukten buyuge sirala
def sirala(dizi):
    if len(dizi) <= 1: 
        return dizi
    else:
        min_deger = min(dizi)
        dizi.remove(min_deger)
        return [min_deger] + sirala(dizi)

print(sirala([3, 1, 4, 1, 5, 9]))  

#piramit
def piramid_yazdir(n, satir=1):
    if satir > n:  
        return
    else:
        print(" " * (n - satir) + "*" * (2 * satir - 1))
        piramid_yazdir(n, satir + 1)

piramid_yazdir(5)
# Çıktı:
#     *
#    ***
#   *****
#  *******
# *********




#ekok alma
def ekok(a, b, kat):
    if kat % a == 0 and kat % b == 0: 
        return kat
    else:
        return ekok(a, b, kat + 1)

print(ekok(6, 8, max(6, 8)))  



#sayinin bolenlerini listeye ekleme
def bolenler(n, i=1):
    if i > n:  
        return []
    elif n % i == 0:  
        return [i] + bolenler(n, i + 1)
    else:  
        return bolenler(n, i + 1)

print(bolenler(12))  



#dizideki en kucuk eleman
def en_kucuk(dizi):
    if len(dizi) == 1: 
        return dizi[0]
    else:
        min_digerleri = en_kucuk(dizi[1:])
        return dizi[0] if dizi[0] < min_digerleri else min_digerleri

print(en_kucuk([3, 1, 4, 1, 5, 9])) 