# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:58:31 2020

@author: Kodai
"""

K, X = map(int, input().split())
list_ans = []

for i in range(K):
    list_ans.append(X-(K-(i+1)))
 
for j in range(K-1):
    list_ans.append(X+j+1) 

print(*list_ans)