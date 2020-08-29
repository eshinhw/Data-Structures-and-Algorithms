# merge sort

# constructs randomized array of length 'size', each element
# is randomly selected from the range 0 up to 'max'

def create_array (size=5,max=10):
    from random import randint
    return [randint(0,max) for _ in range(size)]

def merge (a,b):
    c = [] # final output array
    a_idx,b_idx = 0,0
    
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
            
    
    if a_idx == len(a): 
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])
    
    return c

def merge_sort(a):
    
    # a list of zero or one elements is sorted, by definition
    
    if len(a) <= 1:
        return a
    
    left = merge_sort(a[:len(a)//2])
    right = merge_sort(a[len(a)//2:])
    
    return merge(left,right)

a = create_array()
print(a)
s = merge_sort(a)
print(s)
    
    
    
    
