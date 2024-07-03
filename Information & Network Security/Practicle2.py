#implement monoalphabetic cipher encryption-decryption


normal_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

coded_char = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O',
              'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
              'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

def string_encryption(s):
    encrypted_string = ""
    for char in s:
        if char.lower() in normal_char:
            encrypted_string += coded_char[normal_char.index(char.lower())]
        else:
            encrypted_string += char
    return encrypted_string

def string_decryption(s):
    decrypted_string = ""
    for char in s:
        if char in coded_char:
            decrypted_string += normal_char[coded_char.index(char)]
        else:
            decrypted_string += char
    return decrypted_string

if __name__ == "__main__":
    plain_text = input("Enter the plain text to encrypt: ")
    print("Plain text:", plain_text)
    
    encrypted_message = string_encryption(plain_text.lower())
    print("Encrypted message:", encrypted_message)
    
    decrypted_message = string_decryption(encrypted_message)
    print("Decrypted message:", decrypted_message)
normal_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

coded_char = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O',
              'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
              'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

def string_encryption(s):
    encrypted_string = ""
    for char in s:
        if char.lower() in normal_char:
            encrypted_string += coded_char[normal_char.index(char.lower())]
        else:
            encrypted_string += char
    return encrypted_string

def string_decryption(s):
    decrypted_string = ""
    for char in s:
        if char in coded_char:
            decrypted_string += normal_char[coded_char.index(char)]
        else:
            decrypted_string += char
    return decrypted_string

if __name__ == "__main__":
    plain_text = input("Enter the plain text to encrypt: ")
    print("Plain text:", plain_text)
    
    encrypted_message = string_encryption(plain_text.lower())
    print("Encrypted message:", encrypted_message)
    
    decrypted_message = string_decryption(encrypted_message)
    print("Decrypted message:", decrypted_message)
