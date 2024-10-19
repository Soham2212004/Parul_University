import numpy as np
def create_key_matrix(key, n):
    key_matrix = [[0] * n for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            key_matrix[i][j] = ord(key[k]) % 65
            k += 1
    return np.array(key_matrix)

def process_text(text, n):
    text = text.upper().replace(" ", "")
    while len(text) % n != 0:
        text += 'X'
    return text
def text_to_matrix(text, n):
    text_matrix = []
    for i in range(0, len(text), n):
        text_matrix.append([ord(char) % 65 for char in text[i:i+n]])
    return np.array(text_matrix).T
def matrix_to_text(matrix):
    text = ""
    for i in range(matrix.shape[1]):
        for j in range(matrix.shape[0]):
            text += chr(matrix[j, i] + 65)
    return text
def encrypt(plaintext, key_matrix):
    n = key_matrix.shape[0]
    plaintext = process_text(plaintext, n)
    plaintext_matrix = text_to_matrix(plaintext, n)
    ciphertext_matrix = np.dot(key_matrix, plaintext_matrix) % 26
    return matrix_to_text(ciphertext_matrix)
def mod_inverse(matrix, modulus):
    determinant = int(np.round(np.linalg.det(matrix)))
    determinant_inv = pow(determinant, -1, modulus)
    matrix_modulus_inv = determinant_inv * np.round(determinant * np.linalg.inv(matrix)).astype(int) % modulus
    return matrix_modulus_inv
def decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    ciphertext_matrix = text_to_matrix(ciphertext, n)
    key_matrix_inv = mod_inverse(key_matrix, 26)
    plaintext_matrix = np.dot(key_matrix_inv, ciphertext_matrix) % 26
    return matrix_to_text(plaintext_matrix)
if __name__ == "__main__":
    key = input("Enter the key (a string of 9/16/25 letters for 3x3/4x4/5x5 matrix): ").upper().replace(" ", "")
    n = int(len(key)**0.5)
    if n not in [3, 4, 5] or len(key) != n**2:
        print("Invalid key length! Please enter a valid key.")
    else:
        key_matrix = create_key_matrix(key, n)     
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
        if choice.lower() == 'e':
            plaintext = input("Enter the plaintext: ").upper().replace(" ", "")
            ciphertext = encrypt(plaintext, key_matrix)
            print(f"Plaintext: {plaintext}")
            print(f"Ciphertext: {ciphertext}")
        elif choice.lower() == 'd':
            ciphertext = input("Enter the ciphertext: ").upper().replace(" ", "")
            plaintext = decrypt(ciphertext, key_matrix)
            print(f"Ciphertext: {ciphertext}")
            print(f"Plaintext: {plaintext}")
        else:
            print("Invalid choice! Please enter 'e' for encryption or 'd' for decryption.")
