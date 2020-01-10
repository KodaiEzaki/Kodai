# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:48:08 2020

@author: TANAKA
"""

N = int(input())
S = input()
list_S = list(S)
list_ans = []

alphabet_number = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13,
            'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

number_alphabet = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M',
                   14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}

for i in range(len(list_S)):
    A = alphabet_number[list_S[i]]
    
    if A + N <= 26:
        B = A + N
    else:
        B = (A+N) - 26
        
    C = number_alphabet[B]
    list_ans.append(C)

print(''.join(list_ans))