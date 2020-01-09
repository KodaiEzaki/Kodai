# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 15:28:08 2020

@author: TANAKA
"""

M = int(input())
m = M/1000

if m < 0.1:
    print('00')
    
if 0.1 <= m < 1:
    print('0'+str(int(10*m)))
    
if 1 <= m <= 5:
    print(int(10*m))

if 6 <= m <= 30:
    print(int(m+50))

if 35 <= m <= 70:
    print(int((m-30)//5 + 80))

if m > 70:
    print(89)
    