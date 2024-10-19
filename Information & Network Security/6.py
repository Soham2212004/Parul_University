def encrypt_transposition_cipher(plaintext, key):
    # Initialize variables
    ciphertext = [''] * key
    
    # Loop through each column in the ciphertext
    for column in range(key):
        pointer = column
        
        # Add every key-th character in the column to the ciphertext
        while pointer < len(plaintext):
            ciphertext[column] += plaintext[pointer]
            pointer += key
    
    # Join the columns to get the final ciphertext
    return ''.join(ciphertext)

def decrypt_transposition_cipher(ciphertext, key):
    # Calculate the number of rows
    num_rows = len(ciphertext) // key
    num_full_columns = len(ciphertext) % key
    
    # Initialize an empty list to store the rows of the plaintext
    plaintext = [''] * num_rows
    
    # Variables to track the position in the ciphertext
    column = 0
    row = 0
    
    # Decrypt by reversing the transposition process
    for char in ciphertext:
        plaintext[row] += char
        row += 1
        
        if (row == num_rows) or (row == num_rows - 1 and column >= num_full_columns):
            row = 0
            column += 1
    
    # Join the rows to recover the original plaintext
    return ''.join(plaintext)

# Example use:
plaintext = input("Enter a plaintext: ")
key = int(input("Enter a key (positive integer): "))

# Encrypt the message
ciphertext = encrypt_transposition_cipher(plaintext, key)
print("Ciphertext:", ciphertext)

# Decrypt the message
decrypted_text = decrypt_transposition_cipher(ciphertext, key)
print("Decrypted text:", decrypted_text)
