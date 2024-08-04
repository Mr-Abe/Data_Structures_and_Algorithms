from Data_structures.Stack import Stack

numbers = Stack()
amount_of_items = numbers.size()
print (f'Before adding items to my stack the length is {amount_of_items}!', end='\n\n')

for i in range (100):
    numbers.push(i)
    i += 1

amount_of_items = numbers.size()
print (f'After adding items to my stack the length is {amount_of_items}, can you see the difference!', end='\n\n')

peek = numbers.peek()
print (f'Using Peek I can see the most recent item added/item at the top of the stack is {peek}', end='\n\n')