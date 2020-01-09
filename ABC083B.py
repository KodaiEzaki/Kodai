# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:43:37 2019

@author: TANAKA
"""

N, A, B = map(int, input().split())

LIST = []
for i in range(N+1):
  LIST.append(i)

list = []

def keta_sum(i):
    sum = 0
    while i>0:
        sum += i%10
        i = i//10
    return(sum)
  
list = [i for i in LIST if A<=keta_sum(i)<=B]

print(sum(list))