import numpy as np

alphabet = 'abcdefghijklmnopqrstuvwxyz'

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower().replace(" ", "")
key_matrix = np.array([[3, 3], [2, 5]])  # 2x2 key matrix for simplicity

def mod_inv_matrix(matrix, modulus):
    determinant = int(np.round(np.linalg.det(matrix)))
    determinant_mod_inv = pow(determinant, -1, modulus)
    matrix_mod_inv = (
        determinant_mod_inv * np.round(determinant * np.linalg.inv(matrix)).astype(int)
    ) % modulus
    return matrix_mod_inv

def text_to_numbers(text):
    return [alphabet.index(char) for char in text]

def numbers_to_text(numbers):
    return ''.join(alphabet[num % 26] for num in numbers)

def encrypt(plain_text, key_matrix):
    n = len(key_matrix)
    if len(plain_text) % n != 0:
        plain_text += 'x' * (n - len(plain_text) % n)  # Padding with 'x'
    plain_text_numbers = text_to_numbers(plain_text)
    cipher_text_numbers = []

    for i in range(0, len(plain_text_numbers), n):
        chunk = plain_text_numbers[i:i + n]
        chunk_vector = np.array(chunk).reshape((n, 1))
        encrypted_vector = np.dot(key_matrix, chunk_vector) % 26
        cipher_text_numbers.extend(encrypted_vector.flatten().tolist())

    cipher_text = numbers_to_text(cipher_text_numbers)
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, key_matrix):
    n = len(key_matrix)
    cipher_text_numbers = text_to_numbers(cipher_text)
    key_matrix_inv = mod_inv_matrix(key_matrix, 26)
    plain_text_numbers = []

    for i in range(0, len(cipher_text_numbers), n):
        chunk = cipher_text_numbers[i:i + n]
        chunk_vector = np.array(chunk).reshape((n, 1))
        decrypted_vector = np.dot(key_matrix_inv, chunk_vector) % 26
        plain_text_numbers.extend(decrypted_vector.flatten().tolist())

    plain_text = numbers_to_text(plain_text_numbers).rstrip('x')
    print(f"The decoded text is {plain_text}")

def main():
    if direction == 'encode':
        encrypt(plain_text=text, key_matrix=key_matrix)
    elif direction == 'decode':
        decrypt(cipher_text=text, key_matrix=key_matrix)
    else:
        print("Error!")

if __name__ == "__main__":
    main()
