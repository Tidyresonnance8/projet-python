class Animal:

    def __init__(self, name):
        self.name = name
        self.diurnal = None
        self.nb_legs = None
        self.asleep = False

    def sleep(self):
        if self.asleep:
            raise RuntimeError("l'animal est déjà entrain de dormir")
        self.asleep = True
        
    def wake_up(self):
        if not self.asleep:
            raise RuntimeError("l'animal est déjà reveillé")
        self.asleep = False

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.diurnal = True
        self.nb_legs = 4

    def roar():
        print("ROARRR!!!")

class Owl(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.diurnal = False
        self.nb_legs = 2

    def fly():
        pass

class Giraffe(Animal):
    def __init__(self, name, neck_length):
        super().__init__(name)
        self.diurnal = True
        self.nb_legs = 4
        if not isinstance(neck_length, (int, float)) or neck_length < 0:
            raise ValueError("la valeur est invalide")
        self.neck_length = neck_length

class Zoo:
    def __init__(self):
        self.animals = []
    def add_animal(self,animal):
        if not isinstance(animal,Animal):
            raise ValueError("ce n'est pas un animal")
        self.animals.append(animal)
        
def create_my_zoo():
    my_zoo = Zoo()
    lion = Lion("Simba")
    owl = Owl("Hedwige")
    g1 = Giraffe("Melmane",3)
    g2 = Giraffe("Sophie",4)
    my_zoo.add_animal(lion)
    my_zoo.add_animal(owl)
    my_zoo.add_animal(g1)
    my_zoo.add_animal(g2)
    return my_zoo
    