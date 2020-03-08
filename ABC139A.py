# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:16:46 2020

@author: Kodai
"""

S = input()
T = input()

count = 0

for i in range(3):
    if S[i] == T[i]:
        count += 1
        
print(count)