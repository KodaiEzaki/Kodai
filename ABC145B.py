# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:20:55 2020

@author: TANAKA
"""

N = int(input())
S = input()
len_S = len(S)
count = 0

if len_S % 2 == 1:
    print('No')

else:
    for i in range(len_S//2):
        if S[i] == S[i+(len_S//2)]:
            count += 1
        else:
            print('No')
            break

    if count == len_S//2:
        print('Yes')