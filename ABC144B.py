# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:46:06 2020

@author: TANAKA
"""

N = int(input())
A = 100000000000

for i in range(1,10):
    if N % i == 0:
        B = N//i
        A = min(A, B)
    
    
if A <= 9:
    print('Yes')

else:
    print('No')    