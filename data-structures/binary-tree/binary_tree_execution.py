from binary_tree_operations import *

"""
         1
       /  \
      2    3
     / \  /  \
    4   5 6  7

Depth First Search (Pre-Order, In-Order, Post-Order)

Breath First Search (level order, reverse level order)
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

print("Pre Order Iterative")
bt.preorder_iterative(bt.root)

print("In Order Traversal")
bt.inorder_iterative(bt.root)