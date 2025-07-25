# shopping_cart_manager.py

def add_item(cart, item):
    cart.append(item)
    print(f'"{item}" added to cart.')

def remove_item(cart, item):
    if item in cart:
        cart.remove(item)
        print(f'"{item}" removed from cart.')
    else:
        print(f'"{item}" not found in cart.')

def remove_last_item(cart):
    if cart:
        removed = cart.pop()
        print(f'Last item "{removed}" removed from cart.')
    else:
        print("Cart is already empty.")

def display_sorted_cart(cart):
    if cart:
        print("Cart items in alphabetical order:")
        for item in sorted(cart):
            print(item)
    else:
        print("Cart is empty.")

def display_cart_with_indices(cart):
    if cart:
        print("Current cart contents:")
        for idx, item in enumerate(cart):
            print(f"{idx}: {item}")
    else:
        print("Cart is empty.")

def run_sample_operations():
    cart = []

    # Step 1: Add items
    add_item(cart, "apples")
    add_item(cart, "bread")
    add_item(cart, "milk")
    add_item(cart, "eggs")

    # Step 2: Remove a specific item
    remove_item(cart, "bread")

    # Step 3: Remove last added item
    remove_last_item(cart)

    # Step 4: Display sorted items
    display_sorted_cart(cart)

    # Step 5: Display cart with indices
    display_cart_with_indices(cart)

if __name__ == "__main__":
    run_sample_operations()
