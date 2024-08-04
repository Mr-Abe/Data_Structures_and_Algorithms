class DynamicArray:
    def __init__(self, capacity):
        # create size, capacity, and array
        self.size = 0
        self.capacity = capacity
        self.array = [None] * capacity

    
    def get(self, index):
        # check the validity of the index
        ### assert self.size >= index is the wrong way
        # check validity by ensuring index is above 0 but less than array size
        if 0 <= index > self.size:
            # return the item at the index
            return self.array[index]

        # error handling        
        else:
            raise IndexError("Index out of bounds")

    
    def set(self, index, value):
        # Check validity of the index
        if 0 <= index < self.size:
            # place value at index
            self.array[index] = value
        
        # error handling
        else:
            raise IndexError("Index out of bounds")

    
    def pushback(self, value):
        # check the space in array
        if self.capacity == self.size:
            self.resize()
        # add item to end of array
        self.array[self.size] = value

        # update size of array
        self.size += 1
    
    def popback(self):
        # check if array is empy
        if self.size == 0:
            raise IndexError('Trying to remove from empty array.')
        else:
            # remove item from end of array
            value = self.array[self.size-1]

            # update array size
            self.size -= 1

            return value
    
    def resize(self):
        # create a new capacity 
        new_capacity = self.capacity * 2

        # create a new temp array
        temp_array = [None] * new_capacity

        # copy items from one to the other
        for i in range (self.size):
            temp_array[i] = self.array[i]

        # update the new capacity
        self.capacity = new_capacity

        # update the new array
        self.array = temp_array
    
    def getSize(self):
        return self.size
    
    def getCapacity(self):
        return self.capacity
