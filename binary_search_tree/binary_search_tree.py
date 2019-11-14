import sys

sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.value}"

    # Insert the given value into the tree
    def insert(self, value):
        parent_node = self
        new_node = BinarySearchTree(value)
        while True:
            if value >= parent_node.value:
                if parent_node.right:
                    parent_node = parent_node.right
                else:
                    parent_node.right = new_node
                    break
            else:
                if parent_node.left:
                    parent_node = parent_node.left
                else:
                    parent_node.left = new_node
                    break

    # recursive insert:
    '''
    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        else:
            if self.left:
                self.left.inert(value)
            else:
                self.left = BinarySearchTree(value)
    '''

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        curr_node = self
        while True:
            if target == curr_node.value:
                return True
            elif target >= curr_node.value:
                if curr_node.right:
                    curr_node = curr_node.right
                else:
                    return False
            else:
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    return False


    # recursive contains
    '''
        def contains(self, target):
            if self.value == target:
                return True
            elif target < self.value:
                if self.left:
                    return self.left.contains(target)
                else:
                    return False
            else:
                if self.right:
                    return self.right.contains(target)
                else:
                    return False
    '''
    # Return the maximum value found in the tree
    def get_max(self):
        curr_node = self
        while curr_node.right:
            curr_node = curr_node.right
        return curr_node.value

    # recursive max
    '''
        def get_max(self):
            return self.right.get_max() if self.right else self.value
    '''
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)

        print(node.value)

        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
            curr_node = queue.dequeue()
            print(curr_node.value)
            if curr_node.left:
                queue.enqueue(curr_node.left)
            if curr_node.right:
                queue.enqueue(curr_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.size > 0:
            curr_node = stack.pop()
            print(curr_node.value)
            if curr_node.left:
                stack.push(curr_node.left)
            if curr_node.right:
                stack.push(curr_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)

        if node.left:
            self.pre_order_dft(node.left)

        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)

        if node.right:
            self.post_order_dft(node.right)

        print(node.value)



