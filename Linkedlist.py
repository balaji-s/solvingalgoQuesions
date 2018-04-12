class Node:

    def __init__(self, data, Node = None):
        self.data = data
        self.Node = Node
    

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
    
    def add(self, data):

        node = Node(data)
        node.Node = self.head
        self.head = node
        self.size += 1
    def printll(self):
        current = self.head
        while current:
            print(current.data)
            current = current.Node
    def reverse(self):
        current = self.head
        self.head = None
        while current:
             node = Node(current.data)
             node.Node = self.head
             self.head = node
             current = current.Node
    def middle_of_linkedlist(self):
        current = self.head
        middle = self.size // 2
        count = 0
        print(middle)
        while current :
            if count == middle :
                print(current.data)
                break
            else:
                current = current.Node
                count +=1


linkedList = LinkedList()

'''for i in range(6):
    linkedList.add(i)
print('done')
linkedList.printll()
print('--after reverse--')
linkedList.reverse()
linkedList.printll()'''
two = LinkedList()
two.add(5)
two.add(4)
two.add(3)
two.add(2)
two.add(1)
two.middle_of_linkedlist()

#flattening linked list
