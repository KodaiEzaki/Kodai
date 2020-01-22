# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:36:10 2020

@author: Kodai
"""

N, K = map(int, input().split())
height_list = list(map(int, input().split()))
len_height_list = len(height_list)
count = 0

for i in range(len_height_list):
    if height_list[i] >= K:
        count += 1
        
print(count)