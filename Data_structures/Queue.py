from LinkedList import Node

class Queue:

    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def enqueue (self, value):
        # check if list is empty and add value to list if it is
        if self.front == None:
            self.front = self.back = value
        # if the list is not empty add the value at the end of the list
        elif self.back is not None:
            temp_back = None
            temp_back = self.back
            se.next = value
        pass

    def dequeue ():
        # check if list is empty and return error message if it is

        # if list is not 
        pass

    def peek():
        pass
    
    def isEmpty():
        pass

    def size():
        pass