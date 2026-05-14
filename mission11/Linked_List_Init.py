class Node:
    """ Represents a Node in a LinkedList data structure. """

    def __init__(self, cargo=None, next=None):
        """
        Creates a new Node object.
        @pre:  -
        @post: A new Node object has been initialised.
               A node can contain a cargo and a reference to another node.
               If none of these are given, the node is initialised with
               empty cargo (None) and no reference (None).
        """
        self.__cargo = cargo
        self.__next  = next
        
def __init__(self, lst):
    self.__length = 0
    self.__head = None
    for i in reversed(lst):
        self.__head = Node(i, self.__head)
        self.__length += 1