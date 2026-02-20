# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 23:59:45 2025

@author: Sombit Mazumder
"""

def partition(arr,low,high):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    elif low < high:
        pivot = arr[low]
        l = low
        m = low
        for i in range(low+1,high):
            if arr[i] > pivot:
                m += 1
            else:
                arr[l+1],arr[i] = arr[i],arr[l+1]
                l+= 1
                m += 1
        arr[l],arr[low] = arr[low],arr[l]
        return l
#print(partition([3,5,1,4,6], 0, 5))
def quicksort(arr,low,high):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    if low < high:
        l = partition(arr,low,high)
        quicksort(arr,low,l)
        quicksort(arr,l+1,high)
    return arr
    
    