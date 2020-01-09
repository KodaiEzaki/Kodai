# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:41:29 2019

@author: TANAKA
"""
n = input()
a = 0
l = [int(x) for x in list(n)]

for i in range(len(l)):
    if l[i] == 1:
        a = a + 1

print(a)