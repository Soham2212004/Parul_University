def caesar_cipher(text, shift, decrypt=False):
    shifted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            if decrypt:
                shifted = ord(char) - shift
            else:
                shifted = ord(char) + shift
            
            if char.islower():
                if decrypt and shifted < ord('a'):
                    shifted += 26
                elif not decrypt and shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if decrypt and shifted < ord('A'):
                    shifted += 26
                elif not decrypt and shifted > ord('Z'):
                    shifted -= 26
            
            shifted_text += chr(shifted)
        else:
            shifted_text += char  # Non-alphabetic characters remain unchanged
    return shifted_text

# Get user input for text, mode (encryption or decryption), and shift amount
plain_text = input("Enter text: ")
while True:
    mode = input("Enter 'e' for encryption or 'd' for decryption: ").lower()
    if mode == 'e' or mode == 'd':
        break
    else:
        print("Invalid input. Please enter 'e' for encryption or 'd' for decryption.")

while True:
    try:
        shift_amount = int(input("Enter the shift amount (integer): "))
        break
    except ValueError:
        print("Please enter a valid integer.")

# Perform encryption or decryption based on user input
if mode == 'e':
    encrypted_text = caesar_cipher(plain_text, shift_amount)
    print("Encrypted:", encrypted_text)
elif mode == 'd':
    decrypted_text = caesar_cipher(plain_text, shift_amount, decrypt=True)
    print("Decrypted:", decrypted_text)
