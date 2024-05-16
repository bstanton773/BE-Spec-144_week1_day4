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

    # Method to find a node based on a value - will either return the BST Node instance or None
    def find_node(self, target):
        # If the target is equal to current node's value
        if target == self.value:
            # We found it!
            return self
        # If the target is less than the current node's value
        elif target < self.value:
            # See if the current node's left is empty
            if self.left is None:
                # We know the target is not in the tree because it would be here (or at least on this path)
                return None
            # if the current node does have a left subtree
            else:
                # Call the find_node method from the left subtree and return that value
                return self.left.find_node(target)
        # If the target is greater than the current node's value
        elif target > self.value:
            # See if the current node's right is empty
            if self.right is None:
                # We know the target is not in the tree because it would be here (or at least on this path)
                return None
            # if the current node does have a right subtree
            else:
                # Call the find_node method from the right subtree and return that value
                return self.right.find_node(target)


tree = BST(50)
tree.insert(40)
tree.insert(30)
tree.insert(90)
tree.insert(75)
tree.insert(10)
tree.insert(35)
print(tree.find_node(35))
print(tree.find_node(87))
