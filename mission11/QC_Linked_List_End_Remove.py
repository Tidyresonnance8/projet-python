class Node:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None

    def next(self):
        return self.next
    
    def set_next(self,node):
        self.__next = node

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__length = 0

    def remove_from_end(self):
        if self.__head is None:
            return
        if self.__head.next() is None:
            self.__head = None
            self.__length -= 1
            return
        current = self.__head
        while current.next().next() is not None:
            current = current.next()
        current.set_next(None)
        self.__length -= 1

