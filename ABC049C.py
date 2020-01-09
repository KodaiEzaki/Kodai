# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:42:01 2019

@author: Kodai
"""
s=str(input())
ans=0
leng=len(s)
while(len(s)>0):
    if s[-1]=='m' and s[-2]=='a' and s[-3] == 'e' and s[-4] =='r' and s[-5] =='d':
        s=s[0:-1]
        s=s[0:-1]
        s=s[0:-1]
        s=s[0:-1]
        s=s[0:-1]
 
    elif s[-1] =='r' and s[-2] =='e' and s[-3]=='m' and s[-4]=='a' and s[-5] == 'e' and s[-6] =='r' and s[-7] =='d': 
        s=s[0:-1]
        s=s[0:-1]
        s=s[0:-1]
        s=s[0:-1]
        s=s[0:-1]
        s=s[0:-1]
        s=s[0:-1]
    elif s[-1]=='e' and s[-2] =='s' and s[-3] =='a' and s[-4] =='r' and s[-5] =='e':
        s=s[0:-1]
        s=s[0:-1]
        s=s[0:-1]
        s=s[0:-1]
        s=s[0:-1]
    elif s[-1] =='r' and s[-2]=='e' and s[-3] =='s' and s[-4] =='a' and s[-5] =='r' and s[-6] =='e':
        s=s[0:-1]
        s=s[0:-1]
        s=s[0:-1]
        s=s[0:-1]
        s=s[0:-1]
        s=s[0:-1]
    else:
        ans=1
        break
    if not s:
        break
if ans ==1:
    print('NO')
else :
    print('YES')