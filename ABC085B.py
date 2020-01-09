# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 17:06:21 2019
@author: TANAKA
"""

N = int(input())
list_n = []

for _ in range(N):
    list_n.append(int(input()))

for i in range(N):
    for j in range(N):
        if list_n[i] == list_n[j] and i != j:
            list_n[i] = 0

count = 0

for i in list_n:
    if i != 0:
        count += 1
        
print(count)