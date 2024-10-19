import random

def generate_key(length):
    """Generates a random key of the same length as the plaintext."""
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))

def encrypt_one_time_pad(plaintext, key):
    """Encrypts the plaintext using the One-Time Pad encryption method."""
    ciphertext = []
    for i in range(len(plaintext)):
        # Convert plaintext and key characters to numbers (A=0, B=1, ..., Z=25)
        plain_char = ord(plaintext[i].upper()) - 65
        key_char = ord(key[i].upper()) - 65
        
        # Apply the One-Time Pad formula: (plaintext + key) % 26
        cipher_char = (plain_char + key_char) % 26
        
        # Convert back to a character and append to the ciphertext
        ciphertext.append(chr(cipher_char + 65))
    
    return ''.join(ciphertext)

def decrypt_one_time_pad(ciphertext, key):
    """Decrypts the ciphertext using the One-Time Pad decryption method."""
    plaintext = []
    for i in range(len(ciphertext)):
        # Convert ciphertext and key characters to numbers (A=0, B=1, ..., Z=25)
        cipher_char = ord(ciphertext[i].upper()) - 65
        key_char = ord(key[i].upper()) - 65
        
        # Apply the reverse One-Time Pad formula: (ciphertext - key + 26) % 26
        plain_char = (cipher_char - key_char + 26) % 26
        
        # Convert back to a character and append to the plaintext
        plaintext.append(chr(plain_char + 65))
    
    return ''.join(plaintext)

# Example use:
plaintext = input("Enter a plaintext (A-Z only): ").upper().replace(' ', '')
key = generate_key(len(plaintext))
print("Generated Key:", key)

# Encrypt the message
ciphertext = encrypt_one_time_pad(plaintext, key)
print("Ciphertext:", ciphertext)

# Decrypt the message
decrypted_text = decrypt_one_time_pad(ciphertext, key)
print("Decrypted text:", decrypted_text)
