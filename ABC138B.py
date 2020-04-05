# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:41:00 2020

@author: Kodai
"""

N = int(input())
list_A = list(map(int, input().split()))
a = 1

mul_A = 1

for i in range(N):
    a = list_A[i]
    mul_A = mul_A * a
    
sum_A = 0

for i in range(N):
    a = mul_A // list_A[i]
    sum_A = sum_A + a
    
print(mul_A/sum_A)