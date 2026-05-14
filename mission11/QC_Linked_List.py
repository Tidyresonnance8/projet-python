class Node:
    def __init__(self,cargo=None,next=None,previous=None):
        self.cargo = cargo
        self.next = next
        self.previous = previous

    def get_value(self):
        return self.cargo
    
    def get_next(self):
        return self.next
    
    def get_previous(self):
        return self.previous
    
    def set_next(self,cargo):
        self.next = cargo

    def set_previous(self,cargo):
        self.previous = cargo

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def add(self,cargo):
        new_node = Node(cargo)
        if self.head is None:
            self.head = new_node
            self.last = new_node
        else:
            self.last.set_next(new_node)
            new_node.set_previous(self.last)
            self.last = new_node
        self.length += 1

    def get_reverse(self):
        if self.head is None:
            return ""
        result = ""
        current = self.last
        while current is not None:
            result += current.get_value()
            current = current.get_previous()
        return result