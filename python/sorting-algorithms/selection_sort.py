def create_array (size=10,max=50):
    from random import randint
    return [randint(0,max) for _ in range(size)]


def selection_sort (a):

    for i in range(len(a)):
        min_idx = i
        for j in range(i,len(a)):
            if a[j] <= a[min_idx]:
                min_idx = j
            
        if (i != min_idx):
            a[i],a[min_idx] = a[min_idx],a[i]

    return a

arr = create_array()
print(arr)

print(selection_sort(arr))
