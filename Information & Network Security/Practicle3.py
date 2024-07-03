#implement playfair cipher encryption-decryption


def generate_playfair_key_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is combined with I
    key = key.upper().replace("J", "I")
    
    # Remove duplicates while preserving order
    key_no_duplicates = ""
    for char in key:
        if char not in key_no_duplicates:
            key_no_duplicates += char

    # Add remaining letters of the alphabet
    key_no_duplicates += ''.join([c for c in alphabet if c not in key_no_duplicates])
    
    matrix = [list(key_no_duplicates[i:i + 5]) for i in range(0, 25, 5)]
    return matrix

def preprocess_text(text):
    text = text.upper().replace('J', 'I')
    text = ''.join([c for c in text if c.isalpha()])
    
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
            if a != b:
                pairs.append(a + b)
                i += 2
            else:
                pairs.append(a + 'X')
                i += 1
        else:
            pairs.append(a + 'X')
            i += 1
    
    return pairs

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

def playfair_encrypt_decrypt(text, key, mode='encrypt'):
    matrix = generate_playfair_key_matrix(key)
    text_pairs = preprocess_text(text)
    result = ''
    
    for a, b in text_pairs:
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        if row_a == row_b:
            if mode == 'encrypt':
                result += matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
            else:
                result += matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            if mode == 'encrypt':
                result += matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
            else:
                result += matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
        else:
            result += matrix[row_a][col_b] + matrix[row_b][col_a]
    
    return result

# Main program
def main():
    message = input("Enter the message: ")
    key = input("Enter the key: ")
    
    encrypted_message = playfair_encrypt_decrypt(message, key, mode='encrypt')
    print(f"Encrypted Message: {encrypted_message}")
    
    decrypted_message = playfair_encrypt_decrypt(encrypted_message, key, mode='decrypt')
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
