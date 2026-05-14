class CircularLinkedList :

    class Node:
        def __init__(self,cargo=None,next=None):
            """ Initialises a new Node object. """
            self.__cargo = cargo
            self.__next  = next

        def value(self):
            """ Returns the value of the cargo contained in this node. """
            return self.__cargo

        def next(self):
            """ Returns the next node to which this node links. """
            return self.__next

        def set_next(self,node):
            """ Sets the next node to which this node links to a new node. """
            self.__next = node

    def __init__(self):
        """ Initialises a new empty circular linked list.
        @pre:  -
        @post: A new circular linked list with no nodes has been initialised.
                The first pointer refers to None.
        """
        self.__first = None       # pointer to the first node
        self.__last  = None       # pointer to the last node

    def get_first(self):
        """ Returns the first node of this circular linked list.
        @pre:  -
        @post: Returns a reference to the first node of this circular linked list,
                or None if the circular linked list contains no nodes.
        """
        return self.__first

    def get_last(self):
        """ Returns the last node of this circular linked list.
        @pre:  -
        @post: Returns a reference to the last node of this circular linked list,
                or None if the circular linked list contains no nodes.
        """
        return self.__last

    def add(self, cargo):
        """ Adds new Node with given cargo to front of this circular linked list.
        @pre:  self is a (possibly empty) CircularLinkedList.
        @post: A new Node object is created with the given cargo.
                This new Node is added to the front of the circular linked list.
                The head of the list now points to this new node.
                The last node now points to this new node.
        """
        node = self.Node(cargo,self.get_first())
        self.__first = node
        if self.get_last() == None :   # when this was the first element being added,
            self.__last = node     # set the last pointer to this new node
        self.get_last().set_next(node)


    def remove(self, cargo):
        """ Removes a node with given cargo from the circular linked list. """
    
        # Cas 1 : liste vide
        if self.__first is None:
            return None
    
        # Cas 2 : liste à un seul élément
        # (le piège de l'auto-référence : __first.next() == __first)
        if self.__first is self.__last:
            if self.__first.value() == cargo:
                removed = self.__first
                self.__first = None
                self.__last = None
                removed.set_next(None)
                return removed
            else:
                return None
    
        # Cas 3 : la tête correspond (et il y a plusieurs éléments)
        if self.__first.value() == cargo:
            removed = self.__first
            self.__first = self.__first.next()
            self.__last.set_next(self.__first)   # on rebranche __last sur la nouvelle tête
            removed.set_next(None)
            return removed
    
        # Cas 4 : on cherche le prédécesseur dans le reste de la liste
        # Condition d'arrêt circulaire : on s'arrête quand on est revenu à __first,
        # ce qui signifie qu'on a fait le tour complet sans trouver.
        current = self.__first
        while current.next() is not self.__first and current.next().value() != cargo:
            current = current.next()
    
        # Si on est revenu à __first, la valeur n'est pas dans la liste
        if current.next() is self.__first:
            return None
    
        # Sinon current.next() est le nœud à supprimer
        removed = current.next()
        current.set_next(removed.next())
        if removed is self.__last:           # si on a supprimé le dernier, mettre à jour __last
            self.__last = current
        removed.set_next(None)
        return removed


    def removeAll(self, cargo):
        """ Removes all nodes with given cargo from the circular linked list. """
        while self.remove(cargo) is not None:
            pass