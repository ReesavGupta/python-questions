products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [999.99, 25.50, 75.00, 299.99]
quantities = [5, 20, 15, 8]

def create_product_price_pair ():
    for i in zip(products, prices):
        print(i)

def calculate_total_prices():
    for product, price, quantity in zip(products, prices, quantities):
        print(f"Total price for {product} is {price * quantity}")

def build_product_catalog():
    catalog = {}
    for product, price, quantity in zip(products, prices, quantities):
        catalog[product] = {
            "price": price,
            "quantity":quantity 
        }
    print(catalog)

def find_low_stock_products():
    for product, price, quantity in zip(products, prices, quantities):
        if quantity < 10:
            print(f"{product} quantity : {quantity} ")

if __name__ == "__main__":
    create_product_price_pair()
    calculate_total_prices()
    build_product_catalog()
    find_low_stock_products()