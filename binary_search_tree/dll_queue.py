import sys
#sys.path.append('./doubly_linked_list') #imported it directly into the file
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        #Joining the line, you get in at the end of the line, because FIFO
        self.storage.add_to_tail(value)
        self.size +=1

    def dequeue(self):
        # When you leave the line, you're at the front, so head gets cut off
        if self.size  > 0:
            self.size -= 1
            return self.storage.remove_from_head()          
        else:
            return None

    def len(self):
        return self.size
