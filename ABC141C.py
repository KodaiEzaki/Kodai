# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:15:08 2019

@author: Kodai
"""

N, K, Q = map(int, input().split())
list_winner = []
list_point =[]

for _ in range(Q):
    A = int(input())
    list_winner.append(A)

for i in range(N):
    list_point.append(K)
    
    
def add(n):
    return n-Q
    
list_point_new = []

for i in list_point:
    list_point_new.append(add(i))
    
for i in range(Q):
    a = list_winner[i]-1
    list_point_new[a] = list_point_new[a] + 1
    
for i in range(N):
    if list_point_new[i] <= 0:
        print('No')
    else:
        print('Yes')