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
        self.array.append(value)
        self.size += 1
    
    def popback(self):
        # remove item from end of array
        self.array.pop()
    
    def resize(self):
        # create a new capacity 
        new_capacity = self.capacity * 2

        # create a new temp array
        temp_array = [None] * new_capacity

        # copy items from one to the other
        for item in self.array:
            temp_array[item] = item

        # update the new capacity

        # update the new array
    
    def getSize(self):
        pass
    
    def getCapacity(self):
        pass
