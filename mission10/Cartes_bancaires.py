class CarteBancaire:

    def __init__(self, titulaire, numero):
        """
        @pre  : titulaire un string représentant le nom du titulaire
                de la carte
                numero un string représentant le numéro de la carte
                bancaire.
        @post : Une carte bancaire avec un titulaire et un numéro
        """
        self.titulaire = titulaire
        self.numero = numero

    def payer(self, montant):
        """Méthode à redéfinir dans les sous-classes"""
        raise NotImplementedError("Cette méthode doit être implémentée dans les classes filles")

    def __str__(self):
        """
        @pre  : -
        @post : Retourne un string représentant la carte bancaire sous
                le format "Titulaire : XXXX, Numéro : XXXX".
        """
        return "Titulaire : " + self.titulaire + ", Numéro : " + self.numero
    
class CarteDebit(CarteBancaire):
    def __init__(self, titulaire, numero, solde):
        """
        @pre  : titulaire un string représentant le nom du titulaire
                de la carte
                numero un string représentant le numéro de la carte
                bancaire.
                solde un entier positif
        @post : Une carte de débit avec un titulaire, un numéro et un solde
        """
        super().__init__(titulaire, numero)
        self.solde = solde

    def payer(self, montant):
        """
        @pre  : montant un entier positif
        @post : Si le montant est inférieur ou égal au solde restant,
                retir le montant au solde et retourne True.
                Sinon, ne change pas le solde et retourne False
        """
        if montant <= self.solde:
            self.solde -= montant
            return True
        return False

    def __str__(self):
        """
        @pre  : -
        @post : Retourne un string représentant la carte de débit sous
                le format "Titulaire : XXXX, Numéro : XXXX, Solde : XXXX€".
        """
        return super().__str__() + ", Solde : " + str(self.solde) + "€"


class CarteCredit(CarteBancaire):
    def __init__(self, titulaire, numero, limite):
        """
        @pre  : titulaire un string représentant le nom du titulaire
                de la carte
                numero un string représentant le numéro de la carte
                bancaire.
                limite un entier positif représentant la limite
                maximale de la carte de débit.
        @post : Une carte de crédit avec un titulaire, un numéro et une limite
        """
        super().__init__(titulaire, numero)
        self.limite = limite
        self.credit = 0

    def payer(self, montant):
        """
        @pre  : montant un entier positif
        @post : Si la somme du crédit utilisé jusqu'à présent et le
                montant est inférieure ou égale à la limite, augmente
                le crédit utilisé du montant et retourne True.
                Sinon, ne change pas le crédit utilisé et retourne False.
        """
        somme = self.credit + montant
        if somme <= self.limite:
            self.credit += montant
            return True
        return False

    def rembourser(self, montant):
        """
        @pre  : montant un entier positif
        @post : Réduit le crédit utilisé de montant. Le crédit utilisé
                doit rester supérieur ou égal à 0.
        """
        self.credit -= montant
        if self.credit < 0:
            self.credit = 0 

    def __str__(self):
        """
        @pre  : -
        @post : Retourne un string représentant la carte de crédit sous
                le format "Titulaire : XXXX, Numéro : XXXX, Crédit utilisé : XXXX/limite€".
        """
        return super().__str__() + ", Crédit utilisé : " + str(self.credit) + "/" + str(self.limite) + "€"


c = CarteBancaire("Alice", "123")
print(c) # Titulaire : Alice, Numéro : 123

# créer une carte débit avec solde de 50 euros
giro = CarteDebit("Bill", "001", 50)
print(giro)  # Titulaire : Bill, Numéro : 001, Solde : 50€
giro.payer(20)  # Retourne True car le montant est inférieur ou égal au solde restant
print(giro)  # Titulaire : Bill, Numéro : 001, Solde : 30€
giro.payer(45)  # Retourne False car le montant est supérieur au solde restant
print(giro)  # Titulaire : Bill, Numéro : 001, Solde : 30€

# créer une carte de crédit (visa) avec limite 1000
visa = CarteCredit("Alice", "123", 1000)
print(visa)  # Titulaire : Alice, Numéro : 123, Crédit utilisé : 0/1000€

# créer une carte de crédit (mastercard) avec limite 2000
mastercard = CarteCredit("Bob", "252", 2000)
print(mastercard)  # Titulaire : Bob, Numéro : 252, Crédit utilisé : 0/2000€

# créee une carte de crédit (american express) avec limite 5000
amex = CarteCredit("Charles", "103", 5000)
print(amex)  # Titulaire : Charles, Numéro : 103, Crédit utilisé : 0/5000€
amex.payer(250)  # Retourne True car le montant est inférieur ou égal au montant restant pour atteindre la limite
print(amex)  # Titulaire : Charles, Numéro : 103, Crédit utilisé : 250/5000€
amex.payer(4900)  # Retourne False car le montant est supérieur au montant restant pour atteindre la limite
print(amex)  # Titulaire : Charles, Numéro : 103, Crédit utilisé : 250/5000€
amex.rembourser(100)
print(amex)  # Titulaire : Charles, Numéro : 103, Crédit utilisé : 150/5000€
amex.rembourser(500)
print(amex)  # Titulaire : Charles, Numéro : 103, Crédit utilisé : 0/5000€