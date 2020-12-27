#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as rnd
name=input("Lütfen adınızı giriniz:")
kelime=["P y t h o n"] 
letter=""
ayni=[]
game=rnd.choice(kelime)
game=game.split(" ")
count=0
deneme=5
print(f"Selam {name} hazırsan başlayalım")
while True:

    letter=input("Harf tahmini:")
    if(letter in ayni):
        print("Başka bir harf deneyin!! ")
        pass
    else:
        for a in range(0,len(game)):
            if letter==game[a]:
                ayni.append(letter)
                cnt=len(game)-1
                print(f"güzel {letter} harfini buldun. Şimdi {cnt} harf kaldı")
                count+=1
                while True:
                    try:
                        game.remove(letter)
                    except ValueError:
                        break
                break
        if(deneme <1):
            print("Kaybettiniz :( ")
            break

        if(count==0):
            deneme-=1
            print(f"deneme {deneme} kaldı ")
        if(count>0 and deneme>0):
            count=0
        if(len(game)==0):
            print("Terbrikler!! KAZANDINIZ")
            print("Bulduğunuz kelime:",kelime)
            break


# In[ ]:




