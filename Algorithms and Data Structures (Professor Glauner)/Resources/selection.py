'''
Created on Dec 30, 2025

@author: pglauner
'''

def find_min_1(data):
    min1 = float('inf')
    for val in data:
        if val < min1:
            min1 = val
    return min1


def find_min_2(data):
    min1 = float('inf')
    min2 = float('inf')
    for val in data:
        if val < min1:
            min2 = min1
            min1 = val
        elif min1 < val < min2:
            min2 = val


def find_min_3(data):
    min1 = float('inf')
    min2 = float('inf')
    min3 = float('inf')
    for val in data:
        if val < min1:
            min3 = min2
            min2 = min1
            min1 = val
        elif min1 < val < min2:
            min3 = min2
            min2 = val
        elif min2 < val < min3:
            min3 = val
    return min3


import random

def quick_select(data, k, pivot_fn=random.choice):
    if len(data) == 1:
        return data[0]
    pivot = pivot_fn(data)
    less = [x for x in data if x < pivot]
    equal = [x for x in data if x == pivot]
    greater = [x for x in data if x > pivot]
    if k < len(less):
        return quick_select(less, k, pivot_fn)
    elif k < len(less) + len(equal):
        return pivot
    else:
        j = k - len(less) - len(equal)
        return quick_select(greater, j, pivot_fn)

def median_simple(data):
    data = sorted(data)
    if len(data) % 2 == 1:
        return data[len(data) // 2]
    else:
        return 0.5 * (data[len(data) // 2 - 1] + data[len(data) // 2])

def quick_select_median(data, pivot_fn=random.choice):
    if len(data) % 2 == 1:
        return quick_select(data, len(data) // 2, pivot_fn)
    else:
        return 0.5 * (quick_select(data, len(data) // 2 - 1, pivot_fn) +
                      quick_select(data, len(data) // 2, pivot_fn))

def chunked(data, chunk_size):
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def median_of_medians(data):
    if len(data) < 5:
        return median_simple(data)
    chunks = chunked(data, 5)
    full_chunks = [chunk for chunk in chunks if len(chunk) == 5]
    sorted_groups = [sorted(chunk) for chunk in full_chunks]
    medians = [chunk[2] for chunk in sorted_groups]
    res = quick_select_median(medians, median_of_medians)
    return res
