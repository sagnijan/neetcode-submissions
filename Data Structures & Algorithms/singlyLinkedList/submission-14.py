        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None     
    
    def get(self, index: int) -> int:
        #first make a loop traversing list
        current = self.head
        counter = 0
        while current:
            if counter == index:
                return current.value
            current = current.next
            counter += 1
        return -1

    def insertHead(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
            return

        newhead = Node(val)
        newhead.next = self.head
        self.head = newhead        


    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head          
            return
        newtail = Node(val)
        self.tail.next = newtail
        self.tail = newtail


    def remove(self, index: int) -> bool:
        current = self.head
        counter = 0
        while current:
            if index == 0:
                self.head = self.head.next
                return True
            if counter == index - 1:
                if current.next:
                    if current.next == self.tail:
                        self.tail = current
                    current.next = current.next.next
                    return True
            current = current.next
            counter += 1
        return False

    def getValues(self) -> List[int]:
        list_values = []
        current = self.head
        while current:
            list_values.append(current.value)
            current = current.next
            
        return list_values
