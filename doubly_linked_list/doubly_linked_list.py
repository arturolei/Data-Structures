"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        pass

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        pass

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        current_tail = self.tail
        if not self.head:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            current_tail.insert_after(value)
            self.tail = current_tail.next
     

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if not self.tail:
            return None
        if self.head == self.tail:
            tail = self.tail
            self.head = None
            self.tail = None
            return tail.value
        else:
            tail = self.tail
            self.tail.delete()
            self.tail = self.tail.prev
            return tail.value
            
    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if self.head is not node:
            if node.next and node.prev:
                node.delete()
            current_head = self.head
            self.head = node
            node.next = current_head
            current_head.prev = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.tail is not node:
            if node.next and node.prev:
                node.delete()
            current_tail = self.tail
            self.tail = node
            node.prev = current_tail
            current_tail.next = node


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        #check if our list is completely emply
        if not self.head and not self.tail:
            return None        
        # if our list has only a single node, then we delete it
        # both self.head and self.tail should be None
        if self.head == self.tail:
            self.head = None
            self.tail = None

        #check if given node is the head
        if self.head == node:
        # set the self== node.next
        # delete the node
            self.head = node.next
            node.delete()

        #check if the given node is the tail
        if self.tail == node:
        # set self.tail pointer to the previous node
            self.tail = node.prev
        # delete the node
            node.delete()

        # otherwise, the node we're looking to delete is in the middle of the list
        else:
            node.delete()
    
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        current_node = self.head
        list_max = 0
        while current_node:
            if current_node.value > list_max:
                list_max = current_node.value
            current_node = current_node.next
        return list_max