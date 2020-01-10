# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:43:25 2020

@author: TANAKA
"""

A, B = map(int, input().split())

if (1 <= A <= 9) and (1 <= B <= 9):
    print(A*B)
    
else:
    print(-1)