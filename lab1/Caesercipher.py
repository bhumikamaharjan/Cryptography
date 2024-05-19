def caesar_cipher(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine if it's uppercase or lowercase and get its position in the alphabet
            if char.isupper():
                h = ord(char) - ord('A')
            else:
                h = ord(char) - ord('a')

            # Applying the Caesar cipher formula
            encrypted_char = chr((h + key) % 26 + ord('A') if char.isupper() else (h + key) % 26 + ord('a'))
            encrypted_text += encrypted_char
        else:
            # Not a letter? leave it unchanged
            encrypted_text += char
    return encrypted_text


def caesar_decipher(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine if it's uppercase or lowercase and get its position in the alphabet
            if char.isupper():
                h = ord(char) - ord('A')
            else:
                h = ord(char) - ord('a')

            # Applying the Caesar cipher decryption formula
            decrypted_char = chr((h - key) % 26 + ord('A') if char.isupper() else (h - key) % 26 + ord('a'))
            decrypted_text += decrypted_char
        else:
            # Not a letter? leave it unchanged
            decrypted_text += char
    return decrypted_text


plaintext = input("Enter Plaintext: ")
key = int(input("Enter Key: "))

encrypted_text = caesar_cipher(plaintext, key)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_decipher(encrypted_text, key)
print("Decrypted text:", decrypted_text)
