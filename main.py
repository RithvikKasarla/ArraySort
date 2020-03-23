import time
from arraySort import arraySort
from Char_arraysort import arraySortStrings
from random import randint


#Equal to quicksort in array size 50000 & max 50000
#Better than quicksort in array size 500000 & max 100000

def partition(arr,low,high): 
    i = ( low-1 )        
    pivot = arr[high]    
  
    for j in range(low , high): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quickSort(arr,low,high): 
    if low < high:        
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)

arr = []
for i in range(5000000):
  arr.append(randint(0, 10000000))

for runs in range(10):
    print("Trial #", runs+1,"----------------------")

    print("Array Sort")
    ## Can be used as the fastest string sorting algorithm
    arr_copy = arr.copy()
    start_time = time.time()
    arraySort(arr_copy) 
    end = time.time()
    print(end - start_time)

    print("QuickSort")
    start_time = time.time()
    quickSort(arr_copy,0,len(arr_copy)-1) 
    end = time.time()
    print(end - start_time)

"""
import string 
import random

letters = string.ascii_lowercase
line = ''.join(random.choice(letters) for i in range(9000))

print("Array Sort")
s = time.time()
arraySortStrings(line)
end = time.time()
print(end - s)
"""

