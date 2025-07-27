from collections import defaultdict

class Product:
    _products = []

    def __init__(self, product_id, name, price, category, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity
        Product._products.append(self)

    def get_product_info(self):
        return f"{self.name} (${self.price}) - {self.category} - Stock: {self.stock_quantity}"

    @classmethod
    def get_total_products(cls):
        return len(cls._products)

    def reduce_stock(self, quantity):
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            return True
        return False

    @classmethod
    def get_most_popular_category(cls):
        category_sales = defaultdict(int)
        for product in cls._products:
            category_sales[product.category] += product.stock_quantity
        if not category_sales:
            return None
        return min(category_sales.items(), key=lambda x: x[1])[0]


class Customer:
    _total_revenue = 0

    def __init__(self, customer_id, name, email, customer_type):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.customer_type = customer_type

    def get_discount_rate(self):
        if self.customer_type == "premium":
            return 20
        elif self.customer_type == "gold":
            return 10
        return 0

    @classmethod
    def add_to_revenue(cls, amount):
        cls._total_revenue += amount

    @classmethod
    def get_total_revenue(cls):
        return round(cls._total_revenue, 2)

    def __str__(self):
        return f"{self.name} ({self.customer_type})"


class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer
        self.items = {}

    def add_item(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id]["quantity"] += quantity
        else:
            self.items[product.product_id] = {
                "product": product,
                "quantity": quantity
            }

    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def clear_cart(self):
        self.items.clear()

    def get_total_items(self):
        return sum(item["quantity"] for item in self.items.values())

    def get_cart_items(self):
        return [item["product"].name for item in self.items.values()]

    def get_subtotal(self):
        return round(sum(item["product"].price * item["quantity"] for item in self.items.values()), 2)

    def calculate_total(self):
        subtotal = self.get_subtotal()
        discount = self.customer.get_discount_rate()
        return round(subtotal * (1 - discount / 100), 2)

    def place_order(self):
        # Check stock and deduct
        for item in self.items.values():
            if item["product"].stock_quantity < item["quantity"]:
                return "Order failed: Insufficient stock"

        for item in self.items.values():
            item["product"].reduce_stock(item["quantity"])

        total = self.calculate_total()
        Customer.add_to_revenue(total)
        self.clear_cart()
        return "Order placed successfully"


laptop = Product("P001", "Gaming Laptop", 1299.99, "Electronics", 10)
book = Product("P002", "Python Programming", 49.99, "Books", 25)
shirt = Product("P003", "Cotton T-Shirt", 19.99, "Clothing", 50)

print(f"Product info: {laptop.get_product_info()}")
print(f"Total products in system: {Product.get_total_products()}")

customer = Customer("C001", "John Doe", "john@email.com", "premium")
cart = ShoppingCart(customer)

print(f"Customer: {customer}")
print(f"Customer discount: {customer.get_discount_rate()}%")

cart.add_item(laptop, 1)
cart.add_item(book, 2)
cart.add_item(shirt, 3)

print(f"Cart total items: {cart.get_total_items()}")
print(f"Cart subtotal: ${cart.get_subtotal()}")

final_total = cart.calculate_total()
print(f"Final total with ({customer.get_discount_rate()}% discount): ${final_total}")

print(f"Laptop stock before order: {laptop.stock_quantity}")
order_result = cart.place_order()
print(f"Order result: {order_result}")
print(f"Laptop stock after order: {laptop.stock_quantity}")

popular_category = Product.get_most_popular_category()
print(f"Most popular category: {popular_category}")

total_revenue = Customer.get_total_revenue()
print(f"Total revenue: ${total_revenue}")

cart.add_item(book, 1)
cart.remove_item("P002")
print(f"Items after removal: {cart.get_cart_items()}")

cart.clear_cart()
print(f"Items after clearing: {cart.get_total_items()}")
