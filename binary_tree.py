# Binary Search Tree
# Nodes - each node is a BST itself
# 3 attr - .value, .left, .right

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"<BST|{self.value}>"

    # Method to insert a new node into the tree
    def insert(self, new_value):
        # If the new value is less than the current node's value
        if new_value < self.value:
            # Look at the node's left and see if its empty
            if self.left is None:
                # Set the left subtree to be the new instance of BST with new value
                self.left = BST(new_value)
            # If the current node has a left subtree
            else:
                # Call the insert method from the left subtree
                self.left.insert(new_value)
        # If the new value is greater than or equal to the current node's value
        else:
            # Look at the node's right and see if its empty
            if self.right is None:
                # Set the right subtree to be the new instance of BST with new value
                self.right = BST(new_value)
            # If the current node has a right subtree
            else:
                # Call the insert method from the right subtree
                self.right.insert(new_value)


tree = BST(50)
tree.insert(40)
tree.insert(30)
tree.insert(90)
tree.insert(75)
tree.insert(10)
tree.insert(35)
