"""
Implementation of Binary Tree
"""

# 1. Definition of Node Class

class Node(object):
    def __init__(self, value):
        
        self.value = value
        self.left = None
        self.right = None
        
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

# 2. Definition of BinaryTree Class
        
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        
    
    
    def preorder(self, root):
        """ root -> left -> right"""
        if root:
            print(root.value)
            self.preorder(root.left)
            self.preorder(root.right)

    
    def inorder(self, root):
        """left -> root -> right"""
        if root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)
    
    def postorder(self, root):
        """left -> right -> root"""
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value)
            
    def levelOrder(self, root):
        
        if root is None:
            return
        
        queue = Queue()
        queue.enqueue(root)
        
        while (len(queue) > 0):
            
            print(queue.peek())
            node = queue.dequeue()
            
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
                
    # reverse level order traversal: use a queue and a stack
                
    def reverseLevelOrder(self, root):
        
        if root is None:
            return
        
        queue = Queue()
        queue.enqueue(root)
        st = []
        
        while (len(queue) > 0):
            
            node = queue.dequeue()
            st.append(node)
            
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        for n in st[::-1]:
            print(n.value)
            
    def height(self, node):
        if node is None:
            return -1
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return 1 + max(left_height, right_height)
    
    def size(self):
        if self.root is None:
            return 0
        
        st = []
        
        st.append(self.root)
        size = 1
        
        while st:
            node = st.pop()
            if node.left:
                size += 1
                st.append(node.left)
            if node.right:
                size += 1
                st.append(node.right)
        
        return size
    
    def size_(self, node):
        if node is None:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)
    

"""
         1
       /  \
      2    3
     / \  /  \
    4   5 6  7

Depth First Search (PreOrder, InOrder, PostOrder)

* Pre Order Traversal (Parent -> left -> right)

1. Check if the current node is empty / null.
2. Display the data part of the root (or current node).
3. Traverse the left subtree by recursively calling the pre-order function.
4. Traverse the right subtree by recursively calling the pre-order function.
"""

bt = BinaryTree(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)

print("PreOrder Traversal")
bt.preorder(bt.root)

print("InOrder Traversal")
bt.inorder(bt.root)

print("PostOrder Traversal")
bt.postorder(bt.root)

print("Level Order Traversal")
bt.levelOrder(bt.root)

print("Reverse Level Order Traversal")
bt.reverseLevelOrder(bt.root)

print("-----")
print("height:")
print(bt.height(bt.root))

print("-----")
print("size:")
print(bt.size())
print(bt.size_(bt.root))






