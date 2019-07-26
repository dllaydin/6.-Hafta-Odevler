# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:00:30 2019

@author: HP
"""

#ODEV 2: XOX Oyunu
#		Kitapta yer alan XOX oyunu iki kisinin karsilikli oynayabilecegi sekilde duzenlenmis. Sizden bu oyunu 
#		kullanicinin bilgisayara karsi oynayabilecegi versiyonunu yapmanizi istiyoruz. Ayrica gelistireceginiz 
#		algoritma sayesinde bilgisayarin tamamen rastgele hamleler yapmasindan ziyade mantikli hamleler yapmasini 
#		saglamanizi istiyoruz. Ornegin bilgisayarin "O" hamlesini yaptigini varsayalim: 
#					X O _  
#					_ X _   
#					_ _ _
#
#		seklinde olusan bir durumda hamle sirasi bilgisayarda ve bilgisayar kaybetmemek icin sag-alt koseye "O" 
#		koymalidir.

#		Farkli bir ihtimal:
#					O X X 
#					O _ X 
#					_ _ _ 
#
#		boyle bir durumda da hamle sirasi bilgisayarda ve bilgisayar kazanma hamlesi olarak sol-alt koseye "O" koyarak 
#		oyunu bitirmelidir.


# BCB oyunu ;
print("Oyun basliyor...",end='\n'*2)
tablo=[['___','___','___'],
       ['___','___','___'],
       ['___','___','___']]
for i in tablo:
    print('\t'.expandtabs(20),*i, end='\n'*2)
    
kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[0, 2], [1, 1], [2, 0]]]
b_durumu = []
c_durumu = []
sira = 1
bitis=0 ;u=0;w=0
c=[]
import random

while sira < 10 :             # Sirayla bir ben bir de computer
    if sira % 2 == 0:
        işaret = "B".center(3)
        print("İŞARET: {}".format(işaret))
        x = input("Satir No  [1, 2, 3]...; ")
        y = input("Sutun No  [1, 2, 3]...; ")
        if x=='q' or y=='q' :
            print('Cikiliyor...')
            break
    else:
        işaret = "C".center(3)
        print("İŞARET: {}".format(işaret))
        c.clear()
        for i in kazanma_ölçütleri:
            c = [z for z in i if z in c_durumu]
            if len(c)==2 :
                print('c nin yeri onemli')
                for k in range(0,3):
                        if tablo[u][k]=='___' :
                            x=u+1
                            y=k+1
                for k in range(0,3):
                    if tablo[k][w]=='___':
                            x=k+1     
                            y=w+1
                for k in range(0,3):
                    if tablo[k][k]=='___':
                            x=k+1
                            y=k+1
                            
            else:
                x = random.randint(1,3)
                y = random.randint(1,3)
    x = int(x)-1
    y = int(y)-1
    print(x,y)
    
    if tablo[x][y] == "___":
        tablo[x][y] = işaret
        if işaret == "B".center(3):
            b_durumu += [[x, y]]
        elif işaret == "C".center(3):
            c_durumu += [[x, y]]
            u=x ; w=y
            print(c_durumu)
        sira += 1
    else:
        print("\nORA DOLU! TEKRAR DENEYİN\n")
    
    # Son durum tabloyu yazdirma    
    print('\nTabloda son durum...;')
    for i in tablo:
        print("\t".expandtabs(20), *i, end="\n"*2)
        
    # Kazanani belirleme...
    for i in kazanma_ölçütleri:
        c = [z for z in i if z in c_durumu]
        b = [z for z in i if z in b_durumu]
        if len(c) == len(i):
            print("Computer KAZANDI!")
            bitis=1
        elif len(b) == len(i):
            print("Ben KAZANDIM!\n"*3)
            bitis=1
    if bitis==1 :
        break
    elif sira==10:
        print("Oyun bitti kazanan YOK...")
        break
    
    
        
    

