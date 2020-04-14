# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:41:30 2020

@author: Kodai
"""

N = input()
length_N = len(N)
count = 0

for i in range(length_N):
    if N[i] == '7':
        print('Yes')
        count += 1
        break
    
if count == 0:
    print('No')
