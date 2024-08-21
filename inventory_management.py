product_names = []

def add_product_to_list(product_name):
    """Add a product to the product list."""
    if product_name not in product_names:
        product_names.append(product_name)
        print(f"Product '{product_name}' added to list.")
    else:
        print(f"Product '{product_name}' is already in the list.")

def remove_product_from_list(product_name):
    """Remove a product from the product list."""
    if product_name in product_names:
        product_names.remove(product_name)
        print(f"Product '{product_name}' removed from list.")
    else:
        print(f"Product '{product_name}' not found in the list.")

def update_product_in_list(old_name, new_name):
    """Update a product name in the product list."""
    if old_name in product_names:
        index = product_names.index(old_name)
        product_names[index] = new_name
        print(f"Product '{old_name}' updated to '{new_name}'.")
    else:
        print(f"Product '{old_name}' not found in the list.")

product_details = {}

def add_product_to_dict(name, quantity, price):
    """Add or update
