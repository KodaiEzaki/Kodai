# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 17:15:16 2020

@author: TANAKA
"""
import math

N = int(input())
root_N = int(math.sqrt(N)) + 1
A = 100000000000000000000000000000000000

for i in range(1, root_N):
    if N % i == 0:
        B = N//i
        A = min(A, B)

ans_1 = A
ans_2 = N//A
ans = ((ans_1)-1) + ((ans_2)-1)

print(ans)