#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

import os

#HW1-1

#file=open("C:\sample.txt","r")
file = open("./sample.txt", "r")
#用相對路徑的適用性會更廣一些。
text=file.read()
file.close()

text1=text.replace("?"," ")
text2=text1.replace("-"," ")
text3=text2.replace("\""," ")
text4=text3.replace("."," ")
text5=text4.replace(","," ")
textl=text5.replace("\n"," ")

wordl=textl.split(" ")

samplewordlist=[ ]


for x in wordl:
    if len(x)>5:
        samplewordlist.append(x)

print (samplewordlist)

#HW1-2

i=0

keyin=input("Please key in a word:")

while i<1000:
    if len(keyin)<5:
        print ("Please key in a word more than five letters.")
        i=i+1
        break
    elif keyin in samplewordlist:
        print ("The word exists in the list!")
        break
    else:
        print ("The word doesn't exist in the list.")
        break

os.system("pause")
#這行在這個程式裡沒什麼作用。