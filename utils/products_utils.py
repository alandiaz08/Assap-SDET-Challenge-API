import requests
import random
from utils import ramdon_string_generator_utils, register_and_login_utils


def get_product_by_name(user_name):
    url = f"http://localhost:5000/{user_name}/products/{get_random_product_name()}"
    headers = {'accept': 'application/json'}

    # Returns product_name, None otherwise
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        product = response.json()
        return product['product_name']
    else:
        return None


def get_random_product_name():
    # Register a new random user
    user = ramdon_string_generator_utils.generate_random_string(7)
    password = ramdon_string_generator_utils.generate_random_string(7)
    user_name = register_and_login_utils.register_user(user, password)
    register_and_login_utils.login_user(user_name, password)

    # Get the full inventory using the authenticated user's username
    url = f"http://localhost:5000/{user_name}/products"
    headers = {'accept': 'application/json'}

    response = requests.get(url, headers=headers)
    assert response.status_code == 200

    inventory = response.json()
    assert len(inventory) > 0

    # Select a random product from the inventory
    random_product = random.choice(inventory)
    product_name = random_product['product_name']

    return product_name


def get_cart_info(user_name, password):
    # Login the user
    register_and_login_utils.login_user(user_name, password)

    # Make a GET request to retrieve current cart info
    url = f"http://localhost:5000/{user_name}/products/cart"
    headers = {'accept': 'application/xml', 'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    return response.json()


def add_product_to_cart(user_name: str, product_name):
    # Add the given product to the user's cart
    url = f"http://localhost:5000/{user_name}/products/{product_name}/add"
    headers = {'accept': 'application/xml', 'Content-Type': 'application/json'}
    data = {'quantity': 1}

    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 200
