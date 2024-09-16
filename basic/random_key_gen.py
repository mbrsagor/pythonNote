import string
import secrets
import random

def random_key_generator(limit):
    alphabet = string.ascii_letters + string.digits
    key = ''.join(secrets.choice(alphabet) for i in range(limit))
    return key.upper()


random_key = random.randint(1000, 9999)
print("Generated random key:", random_key)

random_key = random.getrandbits(128)
print("Generated random 128-bit key:", random_key)


if __name__ == '__main__':
    print(random_key_generator(50))
