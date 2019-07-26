# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:59:56 2019

@author: HP
"""
#ODEV 1: Sayi Tahmin
#		-Kullanicidan aklindan 0-100 araliginda bir sayi tutmasini isteyin.
#		-Yazdiginiz kod ile bu sayiyi tahmin etmeye calisin.
#		-Tahmin sonucunda, kullanicidan alacaginiz input, pc'nin tahmin ettigi sayi kullanicinin belirledigi 
#		 sayidan buyukse kullanici daha dusuk sayi tahmin etmelisin manasinda "-" seklinde olsun, pc'nin tahmin 
#		 ettigi sayi kullanicinin belirledigi sayidan kucukse "+" seklinde olsun.
#		-Pc'nin tahmini dogru oldugunda da kullanicidan bunu belirtebilecegi bir input isteyin.
#		-Gelistireceginiz algoritma sayesinde kullanicinin belirledigi sayiyi en az hamlede bilmeye calisin :)
#
##		Ornek:
#
#			 Kullanicinin aklindan tuttugu sayi: 56 (kullanicidan bunun icin bir input almayacagiz sadece 
#			 aklinizdan bir sayi belirlemis iseniz oyunumuza baslayabiliriz seklinde bir input alabiliriz. 
#			 Yani belirledigi sayiyi sisteme girmesini istemiyoruz.)

#			 Pc'nin tahmini = 89
#			 Kullanicinin inputu = -
#			 Pc'nin tahmini = 45
#			 Kullanicinin inputu = +
#			 Pc'nin tahmini = 56
#			 Kullanicinin inputu = "Enter"


print("0-100 araliginda aklinizda bir sayi belirlemis iseniz oyuna baslayabiliriz ...")
e=input("Sayiniz hazir ise 'e' ye basiniz   ; ")
if e=='e':
    print("Oyun baslamistir ilk tahmin geliyor...")
import random 
x=1 ; y=100
pc_tahmin=random.randrange(x,y)
k=1
while True :
    print('Tahmin  = ',pc_tahmin)
    a=input("Ne dersin; buyuk tahmin icin '+', kucuk tahmin icin '-' basiniz = ")
    print("Tahmin dogru ise lutfen 'enter' a basiniz ; ")
            
    if a=='+':  
        x=pc_tahmin
    elif a=='-':
        y=pc_tahmin 
    else :
        print("Sayiniz...=",pc_tahmin, 've tam', k,'. tahminde sayi belirlendi!')
        break
    k+=1
    print(x,y)
    pc_tahmin=random.randrange(x,y)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    