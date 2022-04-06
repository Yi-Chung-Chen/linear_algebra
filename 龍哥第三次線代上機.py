# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 13:29:27 2022

@author: timmy
"""
#龍哥的這個考試可以用複製貼上，就用力用下去

arr=input().split()
#處理龍哥的驚喜
if(len(arr)==3):
    arr.append(0)
if(len(arr)==5):
    for _ in range(4):
        arr.append(0)
if(len(arr)==6):
    for _ in range(3):
        arr.append(0)
if(len(arr)==7):
    for _ in range(2):
        arr.append(0)
if(len(arr)==8):
    arr.append(0)
if(len(arr)==13):
    for _ in range(3):
        arr.append(0)
if(len(arr)==14):
    for _ in range(2):
        arr.append(0)
if(len(arr)==15):
    arr.append(0)

#開算
if(len(arr)==4):
    det = arr[0]*arr[3]-arr[1]*arr[2]
elif(len(arr)==9):
    det = (arr[0]*arr[4]*arr[8]+arr[1]*arr[5]*arr[6]+arr[2]*arr[3]*arr[7])-(arr[2]*arr[4]*arr[6]+arr[0]*arr[5]*arr[7]+arr[1]*arr[3]*arr[8])
elif(len(arr)==16):
    minor1=(arr[5]*arr[10]*arr[15]+arr[11]*arr[13]*arr[6]+arr[14]*arr[9]*arr[7])-(arr[13]*arr[10]*arr[7]+arr[6]*arr[9]*arr[15]+arr[11]*arr[5]*arr[14])
    minor2=(arr[4]*arr[10]*arr[15]+arr[11]*arr[12]*arr[6]+arr[14]*arr[8]*arr[7])-(arr[12]*arr[10]*arr[7]+arr[11]*arr[14]*arr[4]+arr[6]*arr[15]*arr[8])
    minor3=(arr[4]*arr[9]*arr[15]+arr[11]*arr[12]*arr[5]+arr[13]*arr[8]*arr[7])-(arr[12]*arr[9]*arr[7]+arr[11]*arr[13]*arr[4]+arr[8]*arr[5]*arr[15])
    minor4=(arr[4]*arr[9]*arr[14]+arr[5]*arr[10]*arr[12]+arr[6]*arr[8]*arr[13])-(arr[12]*arr[9]*arr[6]+arr[13]*arr[10]*arr[4]+arr[14]*arr[5]*arr[8])
    det = (1*arr[0]*minor1+(-1)*arr[1]*minor2+1*arr[2]*minor3+(-1)*arr[3]*minor4)
print(det)
