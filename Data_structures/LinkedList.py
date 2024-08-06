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
            self.head = n_node
        
        else:
            last = self.head

            while last.next is not None:
                last = last.next
            
            last.next = n_node


    # Method to display the linked list
    def display(self):

        if self.head == None:
            print ('The list is empty.')
        
        else:
            selector = self.head

            while selector is not None:
                print (selector.data, end= " -> ")

                selector = selector.next
            
            print ('None.')

    # Method to prepend a new node at the beginning
    def prepend(self, data):

        n_node = Node(data)

        n_node.next = self.head

        self.head = n_node

    # Method to delete a node by value
    def delete(self, key):
        if self.head == None:
            raise IndexError ('The list is empty')
        
        elif self.head.data == key:
            self.head = self.head.next

        else:
            current = self.head
            found = False

            while current.next is not None:
                if current.next.data == key:
                    current.next = current.next.next
                    found = True
                    break
                current = current.next
            if not found:
                print (f'{key} is not found in the list!')