def create_array (size=10,max=50):
    from random import randint
    return [randint(0,max) for _ in range(size)]


def partition (arr, low, high):
    
    # partition function requires two pointers, i and j.
    # pointer i represents the most recent element smaller than the pivot
    # pointer j represents the current location
    # (traversing from the beginning to the location BEFORE the pivot)
    
    i = low-1
    pivot = arr[high]
    
    for j in range(low,high):
        
        if arr[j] <= pivot:
            
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
            
    
    arr[i+1],arr[high] = arr[high],arr[i+1]
    
    return (i+1)

def quick_sort (arr, low, high):
    
    if low < high:
        
        pi = partition (arr,low,high)
        
        quick_sort (arr, low, pi-1)
        quick_sort (arr, pi+1, high)
        
    return arr
        

arr = create_array()

print(arr)

print(quick_sort(arr,0,len(arr)-1))





            