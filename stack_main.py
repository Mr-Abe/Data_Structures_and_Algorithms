from Data_structures.Stack import Stack

numbers = Stack()
amount_of_items = numbers.size()
print (f'Before adding items to my stack the length is {amount_of_items}!', end='\n\n')

for i in range (10000):
    numbers.push(i)
    i += 1

amount_of_items = numbers.size()
print (f'After adding items to my stack the length is {amount_of_items}, can you see the difference!', end='\n\n')

peek = numbers.peek()
print (f'Using Peek I can see the most recent item added/item at the top of the stack is {peek}', end='\n\n')

for i in range(1280):
    remove = numbers.pop()

print (f'Using pop 1,280 times I can remove and see the most recent item added/item at the top of the stack, and that item is {remove}', end='\n\n')

peek = numbers.peek()
amount_of_items = numbers.size()
print (f'Now using peek the most recent item is changed to {peek} and the stack length is {amount_of_items}', end='\n\n')