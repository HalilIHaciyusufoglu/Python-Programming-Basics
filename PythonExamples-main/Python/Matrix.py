# #matris yazdir

import random
def MatrisYazdir(boyut):
    matris=[[int (random.random()*10)for i in range(boyut)]for j in range(boyut)]
    for i in matris:
        print(i)
MatrisYazdir(3)



# birim matris olusturma
def birim(boyut):
    matris = [[1 if i == j else 0 for j in range(boyut)] for i in range(boyut)]
    return matris
print(birim(3))



#sifir matris
def Sifir(a,b):
    matris=[[0 for i in range(b)]for j in range(a)]
    return matris
print(Sifir(3,3))

#kare matris olusturma
def Kare(boyut):
    matris1=[[(random.randint(1,9))for i in range(boyut)]for j in range(boyut)]
    for i in matris1:
        print(i)
    for satir in range(boyut):
        for sütun in range(boyut):
            matris1[satir][sütun]=(matris1[satir][sütun])**2
    return matris1
print(Kare(3))




#rastgele iki matrisin  toplami
import random
def Topla(boyut):
    matris1=[[int (random.random()*10)for i in range(boyut)]for j in range(boyut)]
    matris2=[[int (random.random()*10)for i in range(boyut)]for j in range(boyut)]
    sifir=[[0 for i in range(boyut)]for j in range(boyut)]
    for satir in range(boyut):
        for sütun in range(boyut):
            sifir[satir][sütun]=matris1[satir][sütun]+matris2[satir][sütun]
    for i in matris1:
        print(i)
    print(" ")
    for i in matris2:
        print(i)
    print(" ")
    for i in sifir:
        print(i)
    return sifir
print(Topla(3))


# #matrisin transpozunu al
def Transpoz(boyut):
    matris1=[[int (random.random()*10)for i in range(boyut)]for j in range(boyut)]
    sifir=[[0 for i in range(boyut)]for j in range(boyut)]
    for satir in range(boyut):
        for sütun in range(boyut):
            sifir[sütun][satir]=matris1[satir][sütun]
    return sifir
print(Transpoz(3))


#rastgele iki matrisin carpimi
def Carpim(boyut):
    matris1=[[int (random.random()*10)for i in range(boyut)]for j in range(boyut)]
    matris2=[[int (random.random()*10)for i in range(boyut)]for j in range(boyut)]
    sifir=[[0 for i in range(boyut)]for j in range(boyut)]


    for satir in range(boyut):
        for sütün in range(boyut):
            for k in range(boyut):
                sifir[satir][sütün]+=matris1[satir][k]*matris1[k][sütün]

    # for i in matris1:
    #     print(i)
    # print(" ")
    # for i in matris2:
    #     print(i)
    # print(" ")
    # for i in sifir:
    #     print(i)
    # print(" ")
    return sifir 
print(Carpim(3))


#matristeki en buyuk sayiyi bul
def enbuyuk(boyut):
    matris=[[random.randint(0,9)for i in range(boyut)]for j in range(boyut)]
    maximum=matris[0][0]
    for satir in range(len(matris)):
        for sütun in range(len(matris[satir])):
            if matris[satir][sütun]>maximum:
                maximum=matris[satir][sütun]
    return matris,maximum
print(enbuyuk(3))







# #girilen N degerine gore NxN boyutlu matrisin hucrelerine 1den NxNe kadar sayıları yerlestr
def Ndegeri(N):
  
    sifir=[[0 for i in range(N)]for j in range(N)]
    index=1

   
    for satir in range(N):
        for sütun in range(N):
            sifir[satir][sütun]=index
            index+=1
    return sifir
print(Ndegeri(3))


#bir matris ve bir sayı verilecek matristeki deger  verilen sayidan buyuk esitse 1 degilse matristeki yerine 0 yazılacak
def esik(boyut,esik):
    matris=[[random.randint(0,9)for i in range(boyut)]for j in range(boyut)]
    for i in matris:
        print(i)
    print(" ")
    for i in range(boyut):
        for j in range(boyut):
            if matris[i][j]>=esik:
                matris[i][j]=1
            else:
                matris[i][j]=0
    for i in matris:
        print(i)
    return " "
print(esik(3,5))