class Appartement:

    def __init__(self, pieces):
        """
        @pre  : une liste de pièces de cet appartement
        @post : un Appartement contenant une liste de pièces.
        """
        self.pieces = pieces

    def consommation(self):
        """
        @pre  : -
        @post : Retourne la consommation moyenne journalière de l'appartement en kWh/jour
        """
        consommation_totale = 0
        for p in self.pieces:
            consommation_totale += p.consommation()
        return consommation_totale

class Piece:
    def __init__(self, nom, lampes, heures=0):
        """
        @pre  : un nom de la pièce
                une liste de lampes de la pièce
                un nombre d'heures d'utilisation moyenne par jour (0 par défaut)
        @post : une Piece d'un appartement
        """
        ### CODE NON FOURNI ###

    def consommation(self):
        """
        @pre  : -
        @post : Retourne la consommation moyenne journalière de la piece en kWh/jour.
                La consommation moyenne journalière est simplement la somme de la consommation moyenne journalière de chaque lampe.
                Une lampe de X watt qui reste allumée en moyenne H heures par jour donne une consommation moyenne journalière de (X / 1000) * H kWh/jour.
        """
        ### CODE NON FOURNI ###

class Lampe:

    def __init__(self, type_lampe, puissance):
        """
        @pre  : un type de lampe et un puissance en W
        @post : une Lampe ayant un type et un puissance en W
        """
        ### CODE NON FOURNI ###

    def puissance(self):
        """
        @pre  : -
        @post : Retourne la puissance de la lampe en W
        """
        ### CODE NON FOURNI ###

class AmpouleClassique(Lampe):
    def __init__(self):
        super().__init__("Lampe à incandescence", 60)

class AmpouleBasse(Lampe):
    def __init__(self):
        super().__init__("Ampoule basse consommation", 12)

class TubeFluorescent(Lampe):
    def __init__(self):
        super().__init__("Tube fluorescente", 45)

class LED(Lampe):
    def __init__(self):
        super().__init__("LED", 9)
import math as m
class Couloir(Piece):
    def __init__(self, longueur):
        nom = "Couloir " + str(longueur) + "m"
        heures = 2
        nb_tubes = m.ceil(longueur/5)   # elle me permet d'arrondir mes nombres vers le haut (la méthode ceil par exemple math.ceil(3.2) -> 4)
        lampes= []
        for i in range(nb_tubes):
            lampes.append(TubeFluorescent())
        super().__init__(nom, lampes, heures)
