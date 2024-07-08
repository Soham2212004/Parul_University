def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vernamCipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        pt_num = ord(string[i]) - ord('A')
        key_num = ord(key[i]) - ord('A')
        x = (pt_num ^ key_num)
        if x >= 26:
            x -= 26
        cipher_text.append(chr(x + ord('A')))
    return "".join(cipher_text)

def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        ct_num = ord(cipher_text[i]) - ord('A')
        key_num = ord(key[i]) - ord('A')
        x = (ct_num ^ key_num)
        if x >= 26:
            x -= 26
        orig_text.append(chr(x + ord('A')))
    return "".join(orig_text)

if __name__ == "__main__":
    string = input("String: ").upper()
    keyword = input("Key: ").upper()
    key = generateKey(string, keyword)
    cipher_text = vernamCipherText(string, key)
    print("Ciphertext:", cipher_text)
    print("Original/Decrypted Text:", originalText(cipher_text, key))
