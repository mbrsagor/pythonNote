import string
import secrets


def random_key_generator(limit):
    alphabet = string.ascii_letters + string.digits
    key = ''.join(secrets.choice(alphabet) for i in range(limit))
    return key.upper()


if __name__ == '__main__':
    print(random_key_generator(50))
