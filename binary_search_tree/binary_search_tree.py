import sys
#sys.path.append('../queue_and_stack')--> Redid dependencies so import wouldn't be funky
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        #Initialize so the tree exists, the first node
        self.value = value
        #Left children/branch
        self.left = None
        #Right children branch
        self.right = None

  # Insert the given value into the tree
    def insert(self, value):
        #initialize new_tree as an instance of BinarySearchTree(value)
        new_tree = BinarySearchTree(value)
        #if value is less than self.value:
        if value < self.value:
        #if there's no left node, assert that self.left == new_tree
            if not self.left:
                self.left = new_tree
            else:
                #repeat the process
                self.left.insert(value)
        else:
        #if there's no right node value, assert that self.right == new_tree
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #check to see if value of current node matches the target
        if self.value == target:
            return True
  
        #if value < the current node value, call contains on the left subtree
        if target < self.value:
            #check if self.left exists
            if self.left:
                #if self.left exists, check to see if it contains the target
                if self.left.contains(target):
                    return True
        else:
            if self.right: #if self.right exists, check to see if it contains the target
                if self.right.contains(target):
                    return True
    
        #if we get here our tree doesn't contain target
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None

        max_value = self.value

        current = self

        while current:
            if current.value > max_value:
                max_value = current.value
      
            current = current.right
        return max_value


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # if self.value:
        #     cb(self)
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
            # BinarySearchTree(self.left).for_each(cb)
        if self.right:
            # BinarySearchTree(self.right).for_each(cb)
             self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
