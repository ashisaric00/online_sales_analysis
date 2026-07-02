class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def total_price(self):
        return sum(p.price * p.quantity for p in self.cart_items)

    def show_cart(self):
        for p in self.cart_items:
            print(p.name, p.price, p.quantity)