from Data_structures.LinkedList import SinglyLinkedList

# Create an instance of SinglyLinkedList
ll = SinglyLinkedList()

# Test appending elements
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Expected Output: 1 -> 2 -> 3 -> None.

# Test prepending elements
ll.prepend(0)
ll.append(4)
ll.display()  # Expected Output: 0 -> 1 -> 2 -> 3 -> 4 -> None.

# Test deleting elements
ll.delete(2)
ll.display()  # Expected Output: 0 -> 1 -> 3 -> 4 -> None.

ll.delete(0)
ll.display()  # Expected Output: 1 -> 3 -> 4 -> None.

ll.delete(3)
ll.display()  # Expected Output: 1 -> 4 -> None.

# Edge case: deleting from an empty list
try:
    ll.delete(1)
    ll.delete(4)
    ll.delete(1)  # This should raise an exception
except IndexError as e:
    print(e)  # Expected Output: The list is empty.
