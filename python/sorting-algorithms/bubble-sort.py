def create_array (size=10,max=50):
    from random import randint
    return [randint(0,max) for _ in range(size)]


# swapping elements happens inside the nested loop

def bubble_sort_v1 (arr):
    
    for _ in range(len(arr)):        
        for i in range(len(arr)-1):            
            if arr[i] > arr[i+1]:                
                arr[i],arr[i+1] = arr[i+1],arr[i]                
    return arr

def bubble_sort_v2 (arr):
    swapped = True
    
    while swapped:
        swapped = False
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                arr[i-1],arr[i] = arr[i],arr[i-1]
                swapped = True
                
    return arr
        


a = create_array()

print("array a: ", a)

print(bubble_sort_v1(a))

b = create_array()

print("array b: ", b)

print(bubble_sort_v2(b))
        