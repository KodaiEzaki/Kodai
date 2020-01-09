# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:51:31 2020

@author: TANAKA
"""

N = int(input())
list_A = []

for _ in range(N):
    A = int(input())
    list_A.append(A)
    
A = max(list_A)
index_A = list_A.index(A)

list_B = sorted(list_A, reverse=True)
B = list_B[1]

for i in range(N):    
    if list_A[i] == A:
        print(B)
    else:
        print(A)
        
"""       
N = int(input())
list_A = []

for _ in range(N):
    A = int(input())
    list_A.append(A)
    
A = max(list_A)
index_A = list_A.index(A)

for i in range(N):
    if list_A[i] == A:
        list_A[i] = 0
        print(max(list_A))
        list_A[i] = A
    else:
        print(A)
"""