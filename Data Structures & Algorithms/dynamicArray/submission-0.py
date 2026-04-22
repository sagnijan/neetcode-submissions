class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = []
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        index = self.array[i]
        return index

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        # if the array is full, we call resize
        if self.size == self.capacity:
            self.resize()
        
        self.array.append(n)
        
        # match size with length of array
        if self.size < len(self.array):
            self.size += 1
        

    def popback(self) -> int:
        last_item = self.array.pop()
        self.size -= 1
        return last_item

    def resize(self) -> None:
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity