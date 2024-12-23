import collections
import random

# Шифр Цезаря
def caesar_encrypt(key, text):
    return ''.join(chr((ord(char) + key) % 65536) for char in text)

def caesar_decrypt(key, text):
    return ''.join(chr((ord(char) - key) % 65536) for char in text)

def caesar_crack(cipher_text):
    counter = collections.Counter(cipher_text)
    most_common_char = counter.most_common(1)[0][0]
    key = (ord(most_common_char) - ord(' ')) % 65536
    return caesar_decrypt(key, cipher_text), key

# Шифр Вернама с использованием XOR
def vernam_encrypt(key, text):
    key_expanded = (key * (len(text) // len(key) + 1))[:len(text)]
    return ''.join(chr(ord(k) ^ ord(t)) for k, t in zip(key_expanded, text))

def vernam_decrypt(key, cipher_text):
    key_expanded = (key * (len(cipher_text) // len(key) + 1))[:len(cipher_text)]
    return ''.join(chr(ord(k) ^ ord(c)) for k, c in zip(key_expanded, cipher_text))

# Демонстрация работы
if __name__ == "__main__":
    # Демонстрация шифра Цезаря
    text = "Hello, World!"
    caesar_key = 5
    cipher_text = caesar_encrypt(caesar_key, text)
    print(f"Caesar Encrypted: {cipher_text}")
    decrypted_text = caesar_decrypt(caesar_key, cipher_text)
    print(f"Caesar Decrypted: {decrypted_text}")

    cracked_text, cracked_key = caesar_crack(cipher_text)
    print(f"Caesar Cracked: {cracked_text} (Key: {cracked_key})")

    # Демонстрация шифра Вернама
    vernam_key = "secret"
    vernam_cipher_text = vernam_encrypt(vernam_key, text)
    print(f"Vernam Encrypted: {vernam_cipher_text}")
    vernam_decrypted_text = vernam_decrypt(vernam_key, vernam_cipher_text)
    print(f"Vernam Decrypted: {vernam_decrypted_text}")
