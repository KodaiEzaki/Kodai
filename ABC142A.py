# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:33:28 2020

@author: Kodai
"""

N = int(input())

if N % 2 == 0:
    print(0.50000000000)
else:
    odd_N = N//2 + 1
    print(odd_N / N)