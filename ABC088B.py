9
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:41:43 2019

@author: TANAKA
"""
N = int(input())
list_n = list(map(int, input().split()))
  
list_n.sort(reverse=True)
#print(list_n)

list_even = list_n[0::2]
sum(list_even)
#print(sum(list_even))

list_odd = list_n[1::2]
sum(list_odd)
#print(sum(list_odd))

print(abs(sum(list_odd)-sum(list_even)))