"""
Height of Tree: the height of a tree is the height of its root node.
Height of Node: the height of a node is the number of edges on the longest
path between that node and a leaf.

Take the max between the maximum height from left subtree and 
the maximum height from right subtree
"""


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
            
    def height(node):
        if node is None:
            return -1
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        return 1 + max(left_height, right_height)
    

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        