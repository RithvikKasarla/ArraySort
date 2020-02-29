import time
from arraySort import arraySort
from random import randint
arr = []
for i in range(5000000):
  arr.append(randint(0, 1000000))

#Equal to quicksort in array size 50000 & max 50000
#Better than quicksort in array size 500000 & max 100000
#Looses Horrribly to quicksort at size 5000000 & max 1000000

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


print("Array Sort")
## Can be used as the fastest string sorting algorithm
arr_copy = arr.copy()
start_time = time.time()
arraySort(arr_copy) ## can take up to 8 zeroes 
end = time.time()
print(end - start_time)

arr_copy = arr.copy()
print("QuickSort")
start_time = time.time()
quickSort(arr_copy,0,len(arr_copy)-1) ## can take up to 8 zeroes 
end = time.time()
print(end - start_time)
