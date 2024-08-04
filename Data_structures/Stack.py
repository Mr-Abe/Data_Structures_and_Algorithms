''' Stacks are used as a last-in, first-out data structure. 
They are used to store data in a way that allows for efficient insertion and removal of elements. 
The stack data structure is used in many applications, like the undo feature in text editors, or the back button in web browsers.
'''

class Stack:

    '''Class will have 5 unique methods: push, pop, peek, is_empty, and size.'''
    def __init__(self):
        self.stack = []

    def push (self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        else:
            return self.stack.pop()
        
    def peek(self):
        if self.is_empty():
            return 'Stack is empty'
        else:
            return self.stack[-1]
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)