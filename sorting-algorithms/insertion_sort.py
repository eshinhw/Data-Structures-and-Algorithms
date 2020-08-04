"""
Insertion Sort (삽입정렬)
"""

def create_array (size=10,max=50):
    from random import randint
    return [randint(0,max) for _ in range(size)]

def insertion_sort (a):
    
    for i in range(1,len(a)):
        
        key = a[i]
        j = i-1
        
        while j >= 0 and key < a[j]:            
            a[j+1] = a[j]
            j -= 1
        
        a[j+1] = key
        
    return a

a = create_array()

print(a) # [0, 22, 49, 25, 48, 18, 42, 33, 23, 6]

print(insertion_sort(a)) # [0, 6, 18, 22, 23, 25, 33, 42, 48, 49]