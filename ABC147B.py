# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:35:16 2020

@author: TANAKA
"""

S = input()
len_S = len(S)
list_S = list(S)

if len_S % 2 ==0:
    list_S1 = list_S[0:(len_S//2)]
    list_S2 = list_S[(len_S//2):len_S]
    list_S2.reverse()
    
else:
    list_S1 = list_S[0:(len_S//2)]
    list_S2 = list_S[((len_S//2)+1):len_S]
    list_S2.reverse()
    
count = 0

for i in range(len_S//2):
    if list_S1[i] != list_S2[i]:
        count += 1

print(count)