
class Node:
    
    def __init__(self,value=None):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        
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
                curNode.leftchild.parent = curNode
            else:
                self._insert(value, curNode.leftChild)
        elif value > curNode.value:
            if curNode.rightChild == None:
                curNode.rightChild = Node(value)
                curNode.rightChild.parent = curNode
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
    
    # return the node with specified input value    
    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None
    
    def _find(self, value, curNode):
        if value == curNode.value:
            return curNode
        elif value < curNode.value and curNode.leftChild != None:
            return self._find(value, curNode.leftChild)
        elif value < curNode.value and curNode.rightChild != None:
            return self._find(value, curNode.rightChild)
        
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
    
    """
    BST Deletion
    
    1. Deleting a node with no children (EASIEST)
    
    2. Deleting a node with one child
    
    3. Deleting a node with two children
    """
    
    def delete_value(self, value):
		return self.delete_node(self.find(value))

	def delete_node(self, node):

		## -----
		# Improvements since prior lesson

		# Protect against deleting a node not found in the tree
		if node == None or self.find(node.value) == None:
			print("Node to be deleted not found in the tree!")
			return None 
		## -----

		# returns the node with min value in tree rooted at input node
		def min_value_node(n):
			current = n
			while current.left_child!=None:
				current=current.left_child
			return current

		# returns the number of children for the specified node
		def num_children(n):
			num_children=0
			if n.left_child!=None: num_children+=1
			if n.right_child!=None: num_children+=1
			return num_children

		# get the parent of the node to be deleted
		node_parent=node.parent

		# get the number of children of the node to be deleted
		node_children=num_children(node)

		# break operation into different cases based on the
		# structure of the tree & node to be deleted

		# CASE 1 (node has no children)
		if node_children==0:

			# Added this if statement post-video, previously if you 
			# deleted the root node it would delete entire tree.
			if node_parent!=None:
				# remove reference to the node from the parent
				if node_parent.left_child==node:
					node_parent.left_child=None
				else:
					node_parent.right_child=None
			else:
				self.root=None

		# CASE 2 (node has a single child)
		if node_children==1:

			# get the single child node
			if node.left_child!=None:
				child=node.left_child
			else:
				child=node.right_child

			# Added this if statement post-video, previously if you 
			# deleted the root node it would delete entire tree.
			if node_parent!=None:
				# replace the node to be deleted with its child
				if node_parent.left_child==node:
					node_parent.left_child=child
				else:
					node_parent.right_child=child
			else:
				self.root=child

			# correct the parent pointer in node
			child.parent=node_parent

		# CASE 3 (node has two children)
		if node_children==2:

			# get the inorder successor of the deleted node
			successor=min_value_node(node.right_child)

			# copy the inorder successor's value to the node formerly
			# holding the value we wished to delete
			node.value=successor.value

			# delete the inorder successor now that it's value was
			# copied into the other node
			self.delete_node(successor)
    
    
    

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