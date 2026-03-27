'''
Created on Apr 10, 2020

@author: pglauner
'''

def merge(S1, S2, S):
    #Check coursework
    pass

def merge_sort(S): 
    n = len(S) 
    if n < 2: 
        return 
    mid = n // 2 
    S1 = S[:mid] 
    S2 = S[mid:] 
    merge_sort(S1) 
    merge_sort(S2) 
    merge(S1, S2, S)
