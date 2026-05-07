class Command:
    quantite = 0
    prix = 0

    def __init__(self, id_buyer, id_item, quantity, price):
        self.id_buyer = id_buyer
        self.id_item = id_item
        self.quantity = quantity
        self.price = price
        Command.quantite += 1
        Command.prix += (price * quantity)

    def get_price(self):
        return self.quantity * self.price
    
    def __str__(self):
        return "{}, {} : {} * {} = {}".format(self.id_buyer, self.id_item, self.price, self.quantity, self.get_price())
    
    @classmethod
    def get_number_total_command(cls):
        return cls.quantite

    @classmethod
    def get_total_price(cls):
        return cls.prix
