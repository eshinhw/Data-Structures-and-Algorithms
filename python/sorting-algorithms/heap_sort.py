"""
Heap Sort

heap: ordered binary tree ==> max heap: parent value > child value

1) build max heap: creates max heap from unsorted array
2) heapify: similar to build-max-heap, but assumes part of array is already sorted.

sorting procedure

1. Create max heap for the first time from unsorted array
2. Once in max heap, replace the largest element which is the root element with the last element
3. Assume the last element is sorted and remove from the heap

4. Since the smallest element is in the root position, we have to adjust the heap to become max heap again (heapify)

5. repeat through #2 to $4 until no element is left in the heap

Time Complexity = O(nlogn)
build-max-heap = O(n)
heapify = O(logn), called n-1 times
"""

def create_array (size=10,max=50):
    from random import randint
    return [randint(0,max) for _ in range(size)]

def heapify (arr, size, root):
    
    largest = root
    left_idx = 2 * root + 1
    right_idx = 2 * root + 2
    
    if left_idx < size and arr[root] < arr[left_idx]:
        largest = left_idx
    
    if right_idx < size and arr[largest] < arr[right_idx]:
        largest = right_idx
    
    if largest != root:
        arr[root],arr[largest] = arr[largest],arr[root]        
        heapify(arr, size, largest)

def heap_sort (arr):
    
    size = len(arr)
    
    for i in range(size//2 - 1, -1, -1):
        heapify(arr, size, i)        
    
    for i in range(size-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr


a = create_array()

print(a)

a = heap_sort(a)

print()      