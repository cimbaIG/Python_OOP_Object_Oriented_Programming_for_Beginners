class CashRegister:
    
    def __init__(self, cashier: str):
        self._cashier = cashier
        self._products = []
        
    @property
    def cashier(self):
        return self._cashier
    
    @property
    def products(self):
        return self._products
    
    def add_product(self, product_name: str, product_price: float, quantity=1):
        self._products.append({'name': product_name, 
                               'price': product_price*quantity,
                               'quantity': quantity})
        return self
        
    def show_products(self):
        return self._products    
    
    def remove_product(self, product_name: str):
        for product in self._products:
            if product["name"] == product_name:
                self._products.remove(product)

    def purchase_total(self):
        total = 0
        for product in self._products:
            total += product["price"]
        return round(total,2)
    
    def purchase_tax(self):
        return round(0.05 * self.purchase_total(),2)
    
    def purchase_subtotal(self):
        return self.purchase_total() - self.purchase_tax()
    
    def clear_purchase(self):
        self._products.clear()


# Define an instance with Giovanni as cashier    
cash_register = CashRegister('Giovanni')

# Add three different products to purchases
cash_register.add_product("Old Spice", 3.0, 2)\
             .add_product("Toblerone", 4.0)\
             .add_product("Coca Cola Zero", 2.0)
# Print current products
print("Products:", cash_register.show_products())

# Calculate purchase total (including taxes)
total = cash_register.purchase_total()
# Print subtotal
print("Total price (including tax):", total)

# Calculate tax
tax = cash_register.purchase_tax()
# Print tax
print("Tax:", tax)

# Calculate subtotal price
subtotal  = cash_register.purchase_subtotal()
# Print subtotal
print("Price without tax:", subtotal)

# Remove product from list of products
cash_register.remove_product("Toblerone")
# Print current products
print("Products:", cash_register.show_products())

# Clear all products
cash_register.clear_purchase()
# Print current products
print("Products:", cash_register.show_products())
