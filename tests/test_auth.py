import requests
from utils import ramdon_string_generator_utils
from utils import register_and_login_utils

URL = 'http://localhost:5000'


class TestDemoAuthentication:

    def test_user_registration(self):
        user = ramdon_string_generator_utils.generate_random_string(7)
        password = ramdon_string_generator_utils.generate_random_string(7)
        data = {'username': user, 'password': password}
        headers = {'Content-Type': 'application/json', 'accept': 'application/xml'}
        path = "/users/register"

        response = requests.post(URL + path, json=data, headers=headers)

        # Assert the status code
        assert response.status_code == 200
        # Assert the status response
        assert response.text == '"User created successfully"\n'

    def test_user_login(self):
        user = ramdon_string_generator_utils.generate_random_string(7)
        password = ramdon_string_generator_utils.generate_random_string(7)
        user_name = register_and_login_utils.register_user(user, password)

        data = {'username': user_name, 'password': password}
        headers = {'Content-Type': 'application/json', 'accept': 'application/xml'}
        path = "/users/login"

        response = requests.post(URL + path, json=data, headers=headers)

        # Assert the status code
        assert response.status_code == 200
        # Assert the status response
        assert response.text == '"Login succeeded."\n'

    def test_user_logout(self):
        user = ramdon_string_generator_utils.generate_random_string(7)
        password = ramdon_string_generator_utils.generate_random_string(7)
        user_name = register_and_login_utils.register_user(user, password)
        register_and_login_utils.login_user(user_name, password)

        data = {'username': user_name}
        headers = {'Content-Type': 'application/json', 'accept': 'application/xml'}
        path = "/users/logout"

        response = requests.post(URL + path, json=data, headers=headers)

        # Assert the status code
        assert response.status_code == 200
        # Assert the status response
        assert response.text == '"Logout succeeded."\n'

    def test_get_full_inventory(self):
        # Register a new random user
        user = ramdon_string_generator_utils.generate_random_string(7)
        password = ramdon_string_generator_utils.generate_random_string(7)
        user_name = register_and_login_utils.register_user(user, password)
        register_and_login_utils.login_user(user_name, password)

        # Get the full inventory using the authenticated user's username
        path = "products"
        url = f"{URL}/{user_name}/{path}"
        headers = {'accept': 'application/json'}

        response = requests.get(url, headers=headers)
        assert response.status_code == 200

        # Assert the inventory
        inventory = response.json()
        assert len(inventory) == 3

        for item in inventory:
            assert 'product_name' in item
            assert 'product_qty' in item
            assert 'product_descr' in item
            assert isinstance(item['product_name'], str)
            assert isinstance(item['product_qty'], int)
            assert isinstance(item['product_descr'], str)
