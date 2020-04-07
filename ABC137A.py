# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:53:53 2020

@author: Kodai
"""

A, B = map(int, input().split())

list_ans = [A+B, A-B, A*B]

print(max(list_ans))