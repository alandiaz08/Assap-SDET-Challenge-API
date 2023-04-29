import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_alphanumeric_string(length):
    letters_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_digits) for i in range(length))


