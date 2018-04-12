class DoubleLinkedNode:

    def __init__(self, data):
        self.data = data
        self.previous_node = None
        self.next_node = None


class DoublyLinkedlist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self, data):
        doubleNode = DoubleLinkedNode(data)
        if self.head is None:
           self.head = doubleNode
           self.tail = doubleNode
        else:
            self.head.previous_node = doubleNode
            doubleNode.next_node = self.tail
            doubleNode.previous_node = self.head
            self.head = doubleNode
            self.tail = doubleNode
        self.size += 1
    def printdata(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next_node


    def addlast(self,data):
        current = self.head
        node = DoubleLinkedNode(data)
        if current is None:

            self.head = node
            self.tail = node
            
        else:
            lastNode = self.tail
            #print(lastNode.data)
            lastNode.previous_node = node
            node.next_node = lastNode
            self.tail = node
        self.size += 1

dl = DoublyLinkedlist()
dl.add(1)
dl.add(2)
dl.add(3)
dl.addlast(0)

dl.printdata()  



