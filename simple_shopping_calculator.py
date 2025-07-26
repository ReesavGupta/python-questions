items = ["item1", "item2", "item3"]

price = []
quantity = []

for item in items: 
    price.append(input(f"Enter the price of {item}:"))
    quantity.append(input(f"Enter the quantity of {item}:"))

for item, each_price, each_quantity in zip(items, price, quantity):
    print(f"{item}: {each_quantity} x {each_price} = {int(each_quantity) * int(each_price)}")