
class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = node()
        
    def append(self, data):
        new_node = node(data)
        cur = self.head
        
        while cur.next != None:
            cur = cur.next
        
        cur.next = new_node
    
    def length(self):
        cur = self.head
        total = 0
        
        while cur.next != None:
            total += 1
            cur = cur.next
        
        return total
    
    def display(self):
        cur = self.head
        elems = []
        
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        
        print(elems)
        
    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
    
        cur = self.head
        curIdx = 0
        
        while True:
            cur = cur.next
            if curIdx == index:
                return cur.data
            curIdx += 1
            
    def remove(self, data):
        
        if self.head == None:
            print("EMPTY LINKED LIST!")
            return None
        
        curNode = self.head
        prevNode = None
        
        while curNode.next != None:
            prevNode = curNode
            curNode = curNode.next
            
            if curNode.data == data:
                prevNode.next = curNode.next #####
            
            
            
            
    
    
myList = LinkedList()

myList.append(10)
myList.append(3)
myList.append(1)
myList.append(7)
myList.append(7)

myList.display()  

myList.remove(3)

myList.display()  
    
     
    
    