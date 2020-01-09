# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:37:53 2019

@author: Kodai
"""

'''
#このコードだと時間オーバー#
A, B, X = map(int, input().split())
N = 0

while True:
    
    dN = len(str(N))
    Price = A*N + B*dN
    
    if X > Price:
        N += 1
    else:
        break

print(N)
'''

a, b, x = map(int, input().split())
l = 0
r = 10**9 + 1
while r-l>1:
    mid = (l+r)//2
    anbd = a*mid + b*len(str(mid))
    if anbd > x:
        r = mid
    else:
        l = mid
print(min(10**9, l))