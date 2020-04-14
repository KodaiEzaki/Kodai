# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:52:29 2020

@author: Kodai
"""

N = int(input())
sum_ = 0

for i in range(1,N+1):
  if i % 3 != 0 and i % 5 != 0:
    sum_ += i
    
print(sum_)