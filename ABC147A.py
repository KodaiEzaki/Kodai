# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:33:03 2020

@author: TANAKA
"""

A, B, C = map(int, input().split())

if A + B + C >= 22:
    print('bust')
    
else:
    print('win')