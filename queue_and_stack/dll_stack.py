import sys

sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def __repr__(self):
        return f"{self.storage.__repr__()}"

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.storage.tail is not None:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return

    def len(self):
        return self.size
