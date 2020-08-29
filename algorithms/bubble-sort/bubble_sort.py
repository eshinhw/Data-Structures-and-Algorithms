def create_array (size=10,max=50):
    from random import randint
    return [randint(0,max) for _ in range(size)]

# swapping elements happens inside the nested loop

def bubble_sort_v1(arr):
    
    for i in range(len(arr)):        
        for j in range(len(arr)):            
            if arr[j] >= arr[i]:                
                arr[j],arr[i] = arr[i],arr[j]                
    return arr

def bubble_sort_v2(arr): 
    
    for _ in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


a = create_array()

print("array a: ", a) # [15, 1, 49, 2, 39, 15, 47, 21, 20, 31]

print(bubble_sort_v1(a)) # [1, 2, 15, 15, 20, 21, 31, 39, 47, 49]

b = create_array() 

print("array b: ", b) # [27, 11, 39, 36, 27, 18, 26, 16, 45, 4]

print(bubble_sort_v2(b)) # [4, 11, 16, 18, 26, 27, 27, 36, 39, 45]
        