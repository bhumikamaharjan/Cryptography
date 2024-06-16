import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError('Modular inverse does not exist')
    return x % m


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_keypair(p, q):
    if not is_prime(p) or not is_prime(q):
        raise ValueError("Both numbers must be prime.")

    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            break

    d = mod_inverse(e, phi)
    return (e, n), (d, n)


def encrypt(msg, pub_key):
    e, n = pub_key
    cipher_text = [pow(ord(char), e, n) for char in msg]
    return cipher_text


def decrypt(cipher, pri_key):
    d, n = pri_key
    plain_text = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(plain_text)


if __name__ == "__main__":
    # Input prime numbers p and q manually
    p = int(input("Enter first prime number (p): "))
    q = int(input("Enter second prime number (q): "))

    # Generate key pair
    pub_key, pri_key = generate_keypair(p, q)
    print(f"Public Key (e, n): {pub_key}")
    print(f"Private Key (d, n): {pri_key}")

    # Encrypt and Decrypt
    msg = input("Enter message to encrypt: ")
    print(f"Original Message: {msg}")
    encrypted_msg = encrypt(msg, pub_key)
    print(f"Encrypted Message: {' '.join(map(str, encrypted_msg))}")
    decrypted_msg = decrypt(encrypted_msg, pri_key)
    print(f"Decrypted Message: {decrypted_msg}")
