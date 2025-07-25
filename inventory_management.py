inventory = {
    "apples" : {"price": 50, "quantity": 100},
    "bananas" : {"price": 0.75, "quantity": 150},
    "oranges" : {"price": 2.00, "quantity": 80}
}

def add_a_new_product(name, price, quantity):
    inventory[name] = {
        "price": price,
        "quantity": quantity
    }
    print(inventory)

def update_product_price(fruit: str):
    for key, value in inventory.items():
        if key == fruit:
            value["price"] = 1
    print(inventory)

def sell_fruits(fruit:str  ,qty: int):
    for key, value in inventory.items():
        if key == fruit:
            inventory[fruit]["quantity"] -= qty 
    print(inventory) 

def calc_total_inventory_value():
    total = 0
    for values in inventory.values():
        price = values["price"]
        qty = values["quantity"]
        total += price * qty

    print(f"The total inventory value is {total:.2f}")     

def find_low_products():
    for key, value in inventory.items():
        if value["quantity"] < 100:
            print(f"{key} has {value['quantity']}")        



if __name__ == "__main__":
    add_a_new_product("pear", 20, 5)
    update_product_price("bananas")
    sell_fruits("apples" , 25)
    calc_total_inventory_value()
    find_low_products()