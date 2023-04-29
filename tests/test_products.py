import requests

from tests.test_auth import URL
from utils import ramdon_string_generator_utils, register_and_login_utils
from utils.products_utils import get_product_by_name, get_cart_info, add_product_to_cart


class TestDemoProducts:

    def test_add_product_to_cart(self):
        # Register a new random user
        user = ramdon_string_generator_utils.generate_random_string(7)
        password = ramdon_string_generator_utils.generate_random_string(7)
        user_name = register_and_login_utils.register_user(user, password)
        register_and_login_utils.login_user(user_name, password)

        # Get a random product name using the authenticated user's username
        product_name = get_product_by_name(user_name)

        # Add the random product to the user's cart
        products_path = "/products/"
        add_path = "/add"
        url = f"{URL}/{user_name}{products_path}{product_name}{add_path}"
        headers = {'accept': 'application/xml', 'Content-Type': 'application/json'}
        data = {'quantity': 1}

        response = requests.post(url, headers=headers, json=data)
        assert response.status_code == 200

    def test_get_cart_info(self):
        # Register a new random user
        user = ramdon_string_generator_utils.generate_random_string(7)
        password = ramdon_string_generator_utils.generate_random_string(7)
        user_name = register_and_login_utils.register_user(user, password)
        register_and_login_utils.login_user(user_name, password)

        # Get the authenticated user's cart info
        products_cart_path = "/products/cart"
        url = f"{URL}/{user_name}{products_cart_path}"
        headers = {'accept': 'application/json'}

        response = requests.get(url, headers=headers)
        assert response.status_code == 200

        # Verify the response body
        expected_response_body = get_cart_info(user, password)
        assert response.json() == expected_response_body

    def test_remove_product_from_cart(self):
        # Register a new random user
        user = ramdon_string_generator_utils.generate_random_string(7)
        password = ramdon_string_generator_utils.generate_random_string(7)
        user_name = register_and_login_utils.register_user(user, password)
        register_and_login_utils.login_user(user_name, password)

        # Get a random product name using the authenticated user's username
        product_name = get_product_by_name(user_name)

        # Add the random product to the user's cart
        add_product_to_cart(user_name, product_name)

        # Remove the product from the user's cart
        products_cart_path = "/products/cart/"
        remove_path = "/remove"
        url = f"{URL}/{user_name}{products_cart_path}{product_name}{remove_path}"
        headers = {'accept': 'application/xml'}

        response = requests.post(url, headers=headers)
        assert response.status_code == 200

    def test_checkout_cart(self):
        # Arrange
        expected_response = "Checkout successful!"
        # Register a new random user
        user = ramdon_string_generator_utils.generate_random_string(7)
        password = ramdon_string_generator_utils.generate_random_string(7)
        user_name = register_and_login_utils.register_user(user, password)
        register_and_login_utils.login_user(user_name, password)

        # Get a random product name using the authenticated user's username
        product_name = get_product_by_name(user_name)

        # Add the random product to the user's cart
        add_product_to_cart(user_name, product_name)

        # Checkout the user's cart
        path = "/products/cart/checkout"
        checkout_url = f"{URL}/{user_name}{path}"
        headers = {'accept': 'application/json'}

        response = requests.post(checkout_url, headers=headers)
        assert response.status_code == 200

        # Assert that the response contains the product added to the cart
        assert expected_response in response.text
