class Node:
    def __init__(self, data):
        self.data = data
        self.next= None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    # Method to append a new node at the end
    def append(self, data):
        n_node = Node(data)
        if self.head == None:
            self.head.next == n_node
            n_node.next = None
        
        else:
            while 

    # Method to display the linked list
    def display(self):
        pass

    # Method to prepend a new node at the beginning
    def prepend(self, data):
        pass

    # Method to delete a node by value
    def delete(self, key):
        pass