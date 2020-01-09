# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:41:09 2020

@author: TANAKA
"""

N = int(input())
S, T = input().split()

list_S = list(S)
list_T = list(T)
list_NEW =[]

for i in range(N):
    list_NEW.append(list_S[i])
    list_NEW.append(list_T[i])

print(''.join(list_NEW))