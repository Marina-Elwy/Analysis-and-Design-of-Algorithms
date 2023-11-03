import time
import matplotlib.pyplot as plt
import random 

def merge_sort(array):
    if len(array)<=1:
        return array
    mid=len(array)//2
    left=array[:mid]
    right=array[mid:]
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left, right)

def merge(left, right):
    r=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i] > right[j]:
           r.append(right[j])
           j += 1 
        else:
            r.append(left[i])
            i += 1
    r.extend(left[i:])
    r.extend(right[j:])
    return r 

def binary_search(array,n,i,j):
    if j>=i:
        mid =(i+j)//2

        if array[mid]==n:
             return mid
        elif array[mid] > n:
            return binary_search(array, n, i, mid-1)   
        else:
            return binary_search(array, n, mid+1,j)    
    return -1

def sum_pairs(array,n):
    pairs=[]
    sortedArr=merge_sort(array)

    for i in range(len(sortedArr)):
        comp=n-sortedArr[i]
        bs=binary_search(sortedArr,comp,0,len(sortedArr)-1)
        if(bs!=-1):
            pairs.append((sortedArr[i],comp))
    return pairs


n_values = [10, 100, 1000, 10000, 100000]


execution_times = []

for n in n_values:
 
    array = [random.randint(1, n * 2) for _ in range(n)]

   
    start_time = time.time()
    pairs = sum_pairs(array, n)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)

# Create a graph
plt.plot(n_values, execution_times, marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Running Time (seconds)')
plt.title(' sum_pairs ')
plt.grid(True)
plt.show()
