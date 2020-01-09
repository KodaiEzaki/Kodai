# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 15:56:52 2020

@author: TANAKA
"""
W=input()
ans=[]

for i in range(len(W)):
    if(W[i]!='a' and W[i]!='i' and W[i]!='u' and W[i]!='e' and W[i]!='o'):
        ans.append(W[i])

print(''.join(ans))