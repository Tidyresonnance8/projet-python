def is_every_child_here(first_child):
    if first_child is None:
        return False
    current = first_child
    while True:
        current = current.next
        if current is None:
            return False
        if current == first_child:
            return True
        