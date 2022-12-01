class Product:
    def __init__(self,rest,name,price,type,adicional,quantity):
        self.rest=rest
        self.name=name
        self.price=price
        self.type=type
        self.adicional=adicional
        self.quantity=quantity

    def show_product(self):
        product=self.rest+'//'+self.name+'//'+self.price+'//'+self.type+'//'+self.adicional+'//'+self.quantity
        return product
