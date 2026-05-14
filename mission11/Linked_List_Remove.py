def remove(self):
    if self.__head is not None:
        self.__head = self.__head.next()
        self.__length -= 1