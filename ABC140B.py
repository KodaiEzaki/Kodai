# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:20:11 2020

@author: Kodai
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
sum = 0

A.append(0)

for i in range(N):
  sum += B[A[i]-1]
  if A[i+1] == A[i] + 1:
    sum += C[A[i]-1]

print(sum)