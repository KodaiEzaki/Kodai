# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:03:21 2019

@author: TANAKA
"""

A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            SUM = 500*i + 100*j + 50*k
            if SUM == X:
                count += 1
                
print(count)