# Hill cipher decryption tool

# Sevastian Zare

# 28 assignment

# Decrypt the Hill cipher:

# the ciphertext is: ZUIAZHZUSCYQOXEFFICVCPDGEMIBPTEZIMMRQTXMEIYDBEJPBXUOUMZUUYSCEUASTRCCVBQKGBDJZNGAPORZYQSZLUYQ    
# the key is: [6, 17, 17, 5]

# Decryption. 
# Decrypting with the Hill cipher is built on the following operation: 
# D(K, C) = (K^(-1) *C) mod 26 
# Where K is our key matrix and C is the ciphertext in vector form. 
# Matrix multiplying the inverse of the key matrix with the ciphertext produces the decrypted plaintext.

# python code implementation

def decrypt(ciphertext, key):
    # convert the ciphertext to a vector
    ciphertext = [ord(c) - ord('A') for c in ciphertext]
    # convert the key to a matrix
    key = [ord(c) - ord('A') for c in key]
    key = [key[:2], key[2:]]
    # calculate the inverse of the key matrix
    det = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    det = det % 26
    for i in range(26):
        if (det * i) % 26 == 1:
            det = i
            break
    key[0][0], key[1][1] = key[1][1], key[0][0]
    key[0][1] *= -1
    key[1][0] *= -1
    for i in range(2):
        for j in range(2):
            key[i][j] *= det
            key[i][j] %= 26
    # multiply the inverse of the key with the ciphertext
    plaintext = [0, 0]
    for i in range(2):
        for j in range(2):
            plaintext[i] += key[i][j] * ciphertext[j]
            plaintext[i] %= 26
    # convert the plaintext back to letters
    plaintext = [chr(p + ord('A')) for p in plaintext]
    return ''.join(plaintext)

# main function
def main():
    ciphertext = 'ZUIAZHZUSCYQOXEFFICVCPDGEMIBPTEZIMMRQTXMEIYDBEJPBXUOUMZUUYSCEUASTRCCVBQKGBDJZNGAPORZYQSZLUYQ'
    key = 'FQQE'
    plaintext = decrypt(ciphertext, key)
    print(plaintext)

if __name__ == '__main__':
    main()