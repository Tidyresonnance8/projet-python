class Node:
    def __init__(self,s):
        self.s = s
        self.next = None
        self.previous = None

    def get_text(self):
        return self.s
    
    def set_text(self, s):
        self.s = s

    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next

    def get_previous(self):
        return self.previous
    
    def set_previous(self, previous):
        self.previous = previous

class Tape:
    def __init__(self):
        self.head = None
        self.last = None
        self.current = None
        self.length = 0

    def previous(self):
        if self.current is not None and self.current.get_previous() is not None:
            self.current = self.current.get_previous()
            return self.current.get_text()
        return None
    
    def next(self):
        if self.current is not None and self.current.get_next() is not None:
            self.current = self.current.get_next()
            return self.current.get_text()
        return None
    
    def get_length(self):
        return self.length
    
    def add(self, s):
        new_node = Node(s)
        if self.head is None:
            self.head = new_node
            self.last = new_node
            self.current = new_node
        else:
            self.last.set_next(new_node)
            new_node.set_previous(self.last)
            self.last = new_node
        self.length += 1

    def write(self, s):
        if self.current is not None:
            self.current.set_text(s)

    def read(self):
        if self.current is not None:
            return self.current.get_text()
        return None
    