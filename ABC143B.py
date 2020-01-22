# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 17:48:28 2020

@author: Kodai
"""

N = int(input())
list_d = list(map(int, input().split()))
len_d = len(list_d)
list_2d = []

for i in range(len_d-1):
    for j in range(i+1,len_d):
        recovery = list_d[i] * list_d[j]
        list_2d.append(recovery)

print(sum(list_2d))