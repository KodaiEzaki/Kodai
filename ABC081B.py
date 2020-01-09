# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:52:59 2019

@author: TANAKA
"""

N = int(input())
a = list(map(int, input().split()))

ans = 100000000
for i in range(N):
    c = a[i]
    count = 0
    while c %2 == 0:
        c = c//2
        count += 1
    ans = min(ans,count)
print(ans)