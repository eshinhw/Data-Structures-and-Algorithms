
class Queue(object):
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item) # Insert item at index 0 (the first position)
    
    def dequeue(self):
        # As long as the queue is not empty
        if not self.is_empty():
            return self.items.pop()
        
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)    

class Stack(object):
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pull(self):        
        if len(self.items) > 0:
            self.items.pop()
            
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items) 
        
