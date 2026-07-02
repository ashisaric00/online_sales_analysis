from product import Product
from product_manager import ProductManager
from cart import Cart

pm = ProductManager()

p1 = Product("Laptop", 1000, 2)
p2 = Product("Mouse", 20, 5)
p3 = Product("Keyboard", 50, 3)

pm.add_product(p1)
pm.add_product(p2)
pm.add_product(p3)

pm.show_products()
print("Total inventory value:", pm.total_value())

cart = Cart()
cart.add_to_cart(p1)
cart.add_to_cart(p2)

print("Cart total:", cart.total_price())
cart.show_cart()