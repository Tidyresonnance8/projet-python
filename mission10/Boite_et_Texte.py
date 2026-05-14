class Box:
    def __init__(self, longueur, largeur):
        """
        @pre  : longeur et largeur sont des entiers positifs
        @post : Crée une boîte rectangulaire d'une certaine `longueur` et `largeur`
        """
        self.__longueur = longueur
        self.__largeur = largeur

    def longueur(self) :
        """Retourne la longueur de cette boîte"""
        return self.__longueur

    def largeur(self) :
        """Retourne la largeur de cette boîte"""
        return self.__largeur

    def __eq__(self, box):
        """
        @pre  :  `box` une instance de la classe `Box`
        @post : Retourne True si `box`a la même longueur et largeur
                que la boîte courante
        """
        if type(box) is Box:
            return self.__longueur == box.longueur and self.__largeur == box.largeur
        return False
    
    def __str__(self):
        """
        @pre  :  -
        @post : Retourne la chaîne de caractères: 'Box: [longueur] x [largeur]',
                où [longueur] et [largeur] sont remplacés par
                leurs valeurs respectives.
        """
        return "Box: {} x {}".format(self.longueur(), self.largeur())
    
class TextBox(Box):
    def __init__(self, longueur, largeur, texte):
        super().__init__(longueur, largeur)
        self.texte = texte 

    def __eq__(self, textbox):
        if type(textbox) is TextBox:
            return super().__eq__(textbox) and self.texte == textbox.texte
        return False
    
    def __str__(self):
        return super().__str__() + ", Text: " + str(self.texte)
    

print(Box(7, 5))
t1 = TextBox(7, 5, "texte")
print(t1)  # affiche: "Box: 7 x 5, Text: texte"
t2 = TextBox(7, 5, "text3")
t1 == t2  # retourne False
t3 = TextBox(7, 5, "texte")
t1 == t3  # retourne True