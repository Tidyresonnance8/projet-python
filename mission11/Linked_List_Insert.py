class LinkedList:
    pass

class Node:
    def set_next(self,node):
        self.__next = node

def insert(self, s):
    new_node = Node(s)
    if self.__head is None and s < self.__head.value():
        new_node.set_next(self.__head)
        self.__head = new_node
    else:
        current = self.__head
        while current.next() is not None and current.next().value() < s:
            current = current.next()
        new_node.set_next(current.next())
        current.set_next(new_node)
    self.__length += 1
