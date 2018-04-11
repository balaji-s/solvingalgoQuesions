class DoubleLinkedNode:

    def __init_(self, data):
        self.data = data
        self.previous_node = None
        self.next_node = None


class DoublyLinkedlist:

    def __init__(self):
        self.head = None
        self.size = 0
    
    def add(self, data):
        doubleNode = DoubleLinkedNode(data)
        if self.head is None:
           self.head = doubleNode
        else:
            self.head.previous_node = doubleNode
            doubleNode.next_node = self.head
            self.head = doubleNode




