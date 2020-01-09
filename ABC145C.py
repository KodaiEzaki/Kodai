# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:34:00 2019

@author: Kodai
"""

N = int(input())
list_x = []
list_y = []
list_distance = []

for _ in range(N):
    (x, y) = map(int, input().split())
    list_x.append(x)
    list_y.append(y)
    
for i in range(N-1):
    for j in range(i+1,N):
        xi = list_x[i]
        yi = list_y[i]    
        xj = list_x[j]
        yj = list_y[j]
        
        distance = ((xj-xi)**2 + (yj-yi)**2)**(1/2)
        list_distance.append(distance)

Total = sum(list_distance)

Ans = (2*Total)/N
print(Ans)