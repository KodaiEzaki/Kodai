# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:50:19 2020

@author: Kodai
"""

Tap = input()
len_Tap = len(Tap)
count = 0

for i in range(len_Tap):
    if (i+1) % 2 == 1:
        if Tap[i] == 'R' or Tap[i] == 'U' or Tap[i] == 'D':
            count += 1
    
    else:
        if Tap[i] == 'L' or Tap[i] == 'U' or Tap[i] == 'D':
            count += 1

if count == len_Tap:
    print('Yes')

else:
    print('No')