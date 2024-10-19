import random
from math import gcd

# Function to compute modular inverse using Extended Euclidean Algorithm
def modular_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x
    g, x, _ = egcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

# Function to generate RSA keys (public and private)
def generate_rsa_keys():
    # Step 1: Choose two distinct large prime numbers
    p = 61  # First prime (for simplicity, small prime number used here)
    q = 53  # Second prime

    # Step 2: Compute n = p * q
    n = p * q

    # Step 3: Compute φ(n) = (p - 1)(q - 1)
    phi = (p - 1) * (q - 1)

    # Step 4: Choose an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    e = 17  # Commonly used value for e

    # Step 5: Compute the modular inverse of e mod φ(n) to get the private key exponent d
    d = modular_inverse(e, phi)

    # Public key: (n, e), Private key: (n, d)
    return ((n, e), (n, d))

# Function to encrypt the plaintext using the public key
def encrypt_rsa(plaintext, public_key):
    n, e = public_key
    # Convert each character to its ASCII value, then encrypt using c = (m^e) mod n
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

# Function to decrypt the ciphertext using the private key
def decrypt_rsa(ciphertext, private_key):
    n, d = private_key
    # Decrypt using m = (c^d) mod n, then convert back to character
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

# Example use
if __name__ == "__main__":
    # Step 1: Generate RSA keys
    public_key, private_key = generate_rsa_keys()
    
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # Step 2: Encrypt a message
    plaintext = input("Enter a plaintext message: ")
    ciphertext = encrypt_rsa(plaintext, public_key)
    print("Ciphertext:", ciphertext)

    # Step 3: Decrypt the message
    decrypted_text = decrypt_rsa(ciphertext, private_key)
    print("Decrypted text:", decrypted_text)
