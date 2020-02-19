import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Dynamic allocation of data, array has limitations
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # something gets put onto the stack, it goes first, so add to head
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        # Last in first out, so remove head

        if self.size > 0: #Let us check to make sure it's not empty
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
