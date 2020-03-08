# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:22:27 2020

@author: Kodai
"""

A, B = map(int, input().split())

if A == B:
    print('1')
    
elif B == 1:
    print('0')
    
else:
    AAA = 1
    C = 0
    
    while B > AAA:
        AAA = AAA + A - 1
        C += 1
        
    print(C)