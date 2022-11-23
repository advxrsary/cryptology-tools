# Sevastian Zare
# Cryptology Tools
# Caesar Affine Cipher encryption-decryption tool

# To use this tool, run file named tools.py


# encryption
def affine_encrypt(plaintext, a, b):
    ciphertext = ''
    for c in plaintext:
        if c.isalpha():
            x = ord(c) - ord('A')
            x = (a * x + b) % 26
            ciphertext += chr(x + ord('A'))
        else:
            ciphertext += c
    return ciphertext

# manual decryption
def affine_decrypt(ciphertext, a, b):
    plaintext = ''
    ciphertext = ciphertext.replace(' ', '')
    for c in ciphertext:
        if c.isalpha():
            x = ord(c) - ord('A')
            x = (a * x - b) % 26
            plaintext += chr(x + ord('A'))
        else:
            plaintext += c
    return plaintext

# automatic decryption with brute force and filter
def calc_keys(ciphertext, chars=''):
    for l1 in range(1, 26):
        if 26 % l1 != 0:
            for l2 in range(0, 26):
                plaintext = affine_decrypt(ciphertext, l1, l2)
                if plaintext.startswith(chars):
                    print(l1, l2, plaintext)

# manual ciphertext input
def main():
    ciphertext = input('Enter ciphertext (single line): ')
    chars = input(
        'Enter the first characters of the plaintext (leave empty for all results): ')
    calc_keys(ciphertext, chars)


if __name__ == "__main__":
    main()
