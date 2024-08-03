''' Stacks are used as a last-in, first-out data structure. 
They are used to store data in a way that allows for efficient insertion and removal of elements. 
The stack data structure is used in many applications, like the undo feature in text editors, or the back button in web browsers.
'''

class Stack:

    '''Class will have 5 unique methods: push, pop, peek, is_empty, and size.'''
    def __init__(self):
        self.stack = []
        self.size = 0

    def push (self, item):
        self.stack[self.size] = item
        self.size += 1

    def pop(self):
        if self.size == 0:
            return 'Stack is empty'
        else:
            last_item = self.stack[self.size]

            self.size -= 1

            return last_item
        
    def peek(self):
        last_item = self.stack[self.size]