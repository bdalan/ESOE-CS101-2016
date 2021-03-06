#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 繳交日期：2016.10.17

# 作業內容：
# 1. 請閱讀 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)

# 2. 請試玩 http://armorgames.com/play/17826/logical-element

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。
from operator import itemgetter           #operator module

def charFreqLister(string):

    string=input("請輸入一個字串:")
    resultLIST=[]
    print("確認輸入:",string)
    string_length=len(string)

    for n in string:
        times=string.count(n)
        frequency=times/string_length
        resultLIST.append((frequency,n))
    
    resultLIST1=set(resultLIST)
    resultLIST=list(resultLIST1)
    resultLIST.sort(key=itemgetter(0), reverse= True)
        
    return resultLIST
string=""
print(charFreqLister(string).frequency)

''''
# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
def huffmanTranslater(string):
    inputlist=charFreqLister(string)
    x=0
    a=[]
    b=[]
    c=[]
    for x in (range(len(inputlist))-1):
        while len(inputlist)>0:
            a[x]=min(inputlist,key=itemgetter(0))
            inputlist.remove(a[x])
            b[x]=min(inputlist,key=itemgetter(0))
            inputlist.remove(a[x])
            c[x]=
        
    

resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]

return resultLIST

# 4 請參考以下 condNOT() 的例子，設計四個 func() 依以下條件，能算出 condition02 ~ 04 的值

#condition00 not condition01
def condNOT(inputSTR_X):
    outputSTR = ""
    for i in inputSTR_X:
        if i == "0":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR


#condition00 and condition02
def condAND(inputSTR_X, inputSTR_Y):
    x=len(inputSTR_X)
    a=0
    outputSTR=""
    
    while a <= (x-1):
        if inputSTR_X[a] =="1" and inputSTR_Y[a]=="1":
            
            outputSTR=outputSTR+"1"
            
        else:
            outputSTR=outputSTR+"0"
        a+=1
        
    return outputSTR


#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR=""
    
    for n in range(len(inputSTR_X)):
        if int(inputSTR_X[n])+int(inputSTR_Y[n]) >= 1:
            outputSTR=outputSTR+"1"
                        
        else:
            outputSTR=outputSTR+"0"
    
    return outputSTR


#condition00 xor condition04

def conXOR(inputSTR_X, inputSTR_Y):
    outputSTR=""
    for i in range(len(inputSTR_X)):
        if int(inputSTR_X[i])+int(inputSTR_Y[i])>=1:
            outputSTR=outputSTR+"0"
        else:
            outputSTR=outputSTR+"1"
    return outputSTR

if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print(condition01)

    # 5 請完成以下課本習題並將答案以字串型 (str or unicode) 填入。
    print("Ans:")
    Ch3P3_20a = "0100 0000 1110 0110 0000 0000 0000 0000"
    Ch3P3_20b = "1100 0001 0100 1010 0100 0000 0000 0000"
    Ch3P3_20c = "0100 0000 1100 1101 0000 0000 0000 0000"
    Ch3P3_20d = "1011 1110 1100 0000 0000 0000 0000 0000"
    print("========")
    Ch3P3_28a = "234"
    Ch3P3_28b = "overflow"
    Ch3P3_28c = "874"
    Ch3P3_28d = "888"
    print("========")
    Ch3P3_30a = "234"
    Ch3P3_30b = "overflow"
    Ch3P3_30c = "875"
    Ch3P3_30d = "889"
    print("========")
    Ch4P4_3a = ""
    Ch4P4_3b = ""
    Ch4P4_3c = ""
    Ch4P4_3d = ""
    print("========")
    Ch4P4_4a = ""
    Ch4P4_4b = ""
    Ch4P4_4c = ""
    Ch4P4_4d = ""
    print("========")
    Ch4P4_13a = ""
    Ch4P4_13b = ""
    Ch4P4_13c = ""
    Ch4P4_13d = ""
    print("========")
    Ch4P4_15a = ""
    Ch4P4_15b = ""
    Ch4P4_15c = ""
    Ch4P4_15d = ""
    print("========")
    Ch4P4_16a = ""
    Ch4P4_16b = ""
    Ch4P4_16c = ""
    Ch4P4_16d = ""
    

'''''