
class Node:
    
    def __init__(self,value=None):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        
class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        
        if self.root == None:
            self.root = Node(value)
        
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, curNode):
        if value < curNode.value:
            if curNode.leftChild == None:
                curNode.leftChild = Node(value)
            else:
                self._insert(value, curNode.leftChild)
        elif value > curNode.value:
            if curNode.rightChild == None:
                curNode.rightChild = Node(value)
            else:
                self._insert(value, curNode.rightChild)                
        else:
            print("Value already in tree!")
    
    def print_tree(self):
        
        if self.root != None:
            self._print_tree(self.root)
    
    def _print_tree(self, curNode):
        
        if curNode != None:
            
            self._print_tree(curNode.leftChild)
            
            self._print_tree(curNode.rightChild)
            print("%d " % curNode.value)
    
    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        else:
            return 0
    
    def _height(self, curNode, curHeight):
        if curNode == None:
            return curHeight
        leftHeight = self._height(curNode.leftChild, curHeight+1)
        rightHeight = self._height(curNode.rightChild, curHeight+1)
        return max(leftHeight,rightHeight)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False
        
    def _search(self, value, curNode):
        if value == curNode.value:
            return True
        elif value < curNode.value and curNode.leftChild != None:
            return self._search(value, curNode.leftChild)
        elif value > curNode.value and curNode.rightChild != None:
            return self._search(value, curNode.rightChild)
        return False
    
    

def fill_tree(tree, num_elems = 10, max_int = 20):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0,max_int)
        tree.insert(cur_elem)
    return tree

tree = BinarySearchTree()
# tree = fill_tree(tree)

tree.insert(5)
tree.insert(3)
tree.insert(2)
tree.insert(1)
tree.insert(4)

tree.print_tree()
print("tree height: " + str(tree.height()))

print(tree.search(2))
print(tree.search(9))        