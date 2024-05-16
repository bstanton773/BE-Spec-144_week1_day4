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

    # Method to find the minimum value in a tree
    def find_min(self):
        # If the left is empty
        if self.left is None:
            # Then this is the smallest value
            return self
        # if not empty
        else:
            # Move to the left and try again
            return self.left.find_min()

    # Method to find the maximum value in a tree
    def find_max(self):
        # If the right is empty
        if self.right is None:
            # Then this is the largest value
            return self
        # if not empty
        else:
            # Move to the right and try again
            return self.right.find_max()

    # Method to remove a node from the tree
    def remove(self, target, parent=None):
        # Find the node to remove
        if target < self.value:
            # If the target is less than the current node's value, move to the left and try again
            if self.left:
                self.left.remove(target, self) # Recursively search left subtree
        elif target > self.value:
            # If the target is greater than the current node's value, move to the right and try again
            if self.right:
                self.right.remove(target, self) # Recursively search right subtree
        # We have found the node we are trying to delete
        else:
            # Case 1: Node we are trying to delete has two children
            if self.left and self.right:
                # Replace node's value with the maximum value from the left subtree
                self.value = self.left.find_max().value
                # Remove the node with the max value from the left subtree
                self.left.remove(self.value, self)
            # Case 2: Node is a root and has one or no children
            elif parent is None:
                # if the node only has a left subtree
                if self.left:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                # If the node only has a right subtree
                elif self.right:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                # Case 3: Root Node is a leaf
                else:
                    # Delete the tree
                    del self
            # Case 4: Node has one or no children and is the left child of its parent
            elif parent.left == self:
                # Update the parent's left point to point to the node's child
                parent.left = self.left if self.left else self.right
            # Case 5: Node has one or no children and is the right child of its parent
            elif parent.right == self:
                # Update the parent's right point to point to the node's child
                parent.right = self.left if self.left else self.right

    # Method to perform an in-order traversal
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()



tree = BST(50)
tree.insert(40)
tree.insert(30)
tree.insert(90)
tree.insert(75)
tree.insert(10)
tree.insert(35)
print(tree.find_node(35))
print(tree.find_node(87))

tree.inorder_traversal()
