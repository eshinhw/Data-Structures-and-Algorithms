"""
IMPLEMENTATION OF BINARY TREE

Height of Tree: the height of a tree is the height of its root node.
Height of Node: the height of a node is the number of edges on the longest
path between that node and a leaf.

Take the max between the maximum height from left subtree and 
the maximum height from right subtree

"""

from stack_queue import *

class Node(object):
    def __init__(self, value):
        
        self.value = value
        self.left = None
        self.right = None
        
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
            
    
    def preorder_iterative(self, root):
        
        nodeStack = []
        
        nodeStack.append(root)
        
        while len(nodeStack) > 0:
            
            node = nodeStack.pop()
            print(node.value)
            
            if node.right:
                nodeStack.append(node.right)
            if node.left:
                nodeStack.append(node.left)
    
    def inorder_iterative(self, root):
        
        nodeStack = []
        
        curr = root
        
        while True:

            if curr:
                nodeStack.append(curr)
                curr = curr.left
            
            elif nodeStack:
                curr = nodeStack.pop()
                print(curr.value)
                
                curr = curr.right
            
            else:
                break
    
            
        
            
            
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
    








