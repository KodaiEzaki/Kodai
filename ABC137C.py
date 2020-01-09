# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:32:14 2019

@author: Kodai
"""
N = int(input())
dict = {}
result = 0

for i in range(N):
    s = "".join(sorted(input()))
    if s in dict:
        result += dict[s]
        dict[s] = dict[s] + 1
    else:
        dict[s] = 1
        
print(result)