# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:39:09 2020

@author: Kodai
"""

A, B = map(int, input().split())

if A <= 2*B:
    print(0)

else:
    print(A - 2*B)