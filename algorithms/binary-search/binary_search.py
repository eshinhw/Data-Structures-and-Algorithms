
class BinarySearch():
    
    def recursive_BinarySearch():
        pass
    
    def iterative_BinarySearch(self, A,x):
        """
        Precondition: A is a sorted array of length at least 1.
        Postcondition: Return an integer t such that
        0 <= t <= length(A)-1 and A[t] = x, if such a t exists;
        otherwise return 0;
        """
        
        start = 1
        end = len(A)
        
        while start != end:
            middle = (start + end) // 2
            
            if A[middle] >= x:
                end = middle
            else:
                start = middle + 1
        
        if A[start] == x:
            return start
        else:
            return 0


a = BinarySearch()

print(a.iterative_BinarySearch([1,2,3,4,5], 3))


        

        
        
        
        