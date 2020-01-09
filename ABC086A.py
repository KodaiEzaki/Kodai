# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:00:15 2019

@author: TANAKA
"""

a, b = map(int, input().split())

if a % 2 == 1 and b % 2 == 1:
    print("Odd")
else:
    print("Even")