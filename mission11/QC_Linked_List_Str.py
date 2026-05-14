def __str__(self):
    s = "[ "
    current = self.__head
    while current is not None:
        s += str(current.value()) + " "
        current = current.next()
    s += "]"
    return s