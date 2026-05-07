from math import gcd

class Fraction:
    def __init__(self, numerateur, denominateur):
        """
        @pre  : numerateur est un entier positif
                denominateur est un entier strictement positif
        @post : Une fraction dont le numérateur et le dénominateur ont été simplifié 
                pour représenter la fraction sous sa forme la plus simple.
                Les variables d'instance doivent être inaccessibles en dehors de la classe.
        """
        self.__numerateur = numerateur // gcd(numerateur, denominateur)
        self.__denominateur = denominateur // gcd(numerateur, denominateur)
    
    def __str__(self):
        """
        @pre  : -
        @post : Retourne un string représentant la fraction et sa valeur. 
                Exemple: pour la fraction 3/4 cette méthode retourne "3/4 = 0.75"
        """
        return str(self.__numerateur) + "/" + str(self.__denominateur) + " = " + str(self.__numerateur/self.__denominateur)
  
    def __eq__(self, other):
        """
        @pre  : -
        @post : Retourne True si la fraction courante est égale à la fraction other. 
                Sinon, retourne False.
             
                Indice: Pour éviter toutes les erreurs dues à une erreur de précision 
                        lors d'une division, vous pouvez réarranger les termes de 
                        l'équation pour éviter les divisions (a/b == c/d <=> a*d == c*b).
        """
        if type(other) is Fraction:
            return self.__numerateur * other.__denominateur == self.__denominateur * other.__numerateur
        return False
 
    def __lt__(self, other):
        """
        @pre  : -
        @post : Retourne True si la fraction courante est est plus petite que la fraction other. 
                Sinon, retourne False.
           
                Indice: Pour éviter toutes les erreurs dues à une erreur de précision 
                        lors d'une division, vous pouvez réarranger les termes de 
                        l'équation pour éviter les divisions.
        """
        if type(other) is Fraction:
            return self.__numerateur * other.__denominateur < self.__denominateur * other.__numerateur
        return False

    def __ge__(self, other):
        """
        @pre  : -
        @post : Retourne True si la fraction courante est est plus grande ou égale à la fraction other. 
                Sinon, retourne False.
             
                Indice: Pour éviter toutes les erreurs dues à une erreur de précision 
                        lors d'une division, vous pouvez réarranger les termes de 
                        l'équation pour éviter les divisions.
        """
        if type(other) is Fraction:
            return self.__numerateur * other.__denominateur >= self.__denominateur * other.__numerateur
        return False

    def __add__(self, other):
        """
        @pre  : other est une instance de la classe Fraction
        @post : Retourne une nouvelle fraction qui résulte de l'addition de la 
                fraction courante avec la fraction other.

                Indice: Pour rappel, a/b + c/d == (a*d + c*b)/(b*d)
        """
        new_numerateur = (self.__numerateur * other.__denominateur  + self.__denominateur * other.__numerateur)
        new_denominateur = self.__denominateur * other.__denominateur
        return Fraction(new_numerateur, new_denominateur)