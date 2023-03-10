class CashRegister:

    TAXES_DECIMAL = 0.05

    def __init__(self, cashier):
        self.cashier = cashier
        self.products = {}

    def add_product(self, new_product, quantity=1):
        # new_products is a dictionary.
        self.products[new_product["name"]] = {
            "price": new_product["price"],
            "quantity": quantity
        }

    def show_products(self):
        print(self.products)

    def remove_product(self, product):
        # product is a string with the name of the product.
        del self.products[product]
    
    def update_price(self, product, new_price):
        # product is a string with the name of the product.
        self.products[product]["price"] = new_price

    def find_subtotal(self):
        subtotal = 0
        for product_info in self.products.values():
            subtotal += product_info["price"] * product_info["quantity"]
        return subtotal

    def print_subtotal(self):
        print(self.find_subtotal())

    def find_taxes(self):
        return round(self.find_subtotal() * CashRegister.TAXES_DECIMAL, 2)

    def print_taxes(self):
        print(f"Taxes: {self.find_taxes()}")
    
    def find_total(self):
        return round(self.find_subtotal() + self.find_taxes(), 2)

    def print_total(self):
        print(f"Total: {self.find_total()}")

    def clear_purchase(self):
        self.products.clear()


# Create the instance
my_cash_register = CashRegister("Nora")

# Create the products
product_1 = {"name": "Pizza", "price": 3.54}
product_2 = {"name": "Chocolate", "price": 6.32}
product_3 = {"name": "Pasta", "price": 2.31}

# Add the products
my_cash_register.add_product(product_1)
my_cash_register.add_product(product_2, 3)
my_cash_register.add_product(product_3, 10)

my_cash_register.show_products()

# Remove a product
my_cash_register.remove_product("Pizza")
my_cash_register.show_products()

# Update the price of a product
my_cash_register.update_price("Pasta", 5.67)
my_cash_register.show_products()

# Print the subtotal, taxes, and total
my_cash_register.print_subtotal()
my_cash_register.print_taxes()
my_cash_register.print_total()

# Clear the purchase
my_cash_register.clear_purchase()
my_cash_register.show_products()
