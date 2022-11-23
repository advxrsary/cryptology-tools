import numpy as np

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# convert ciphertext to alphabet numbers
def cipher_alphabet2num(cipher):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher = cipher.upper()
    cipher = [alphabet.index(c) for c in cipher]
    return cipher


# convert numbers to vectors
def numcipher2vector(cipher, n):
    cipher = np.reshape(cipher, (-1, n))
    cipher = cipher.transpose()
    return cipher


def main():
    ciphertext = 'ZUIAZHZUSCYQOXEFFICVCPDGEMIBPTEZIMMRQTXMEIYDBEJPBXUOUMZUUYSCEUASTRCCVBQKGBDJZNGAPORZYQSZLUYQ'

    # key matrix, 2x2
    key = np.array([[6, 17], [17, 5]])
    inv = np.linalg.inv(key)
    n = 2

    cipher = cipher_alphabet2num(ciphertext)
    cipher = numcipher2vector(cipher, n)

    # multiply inverse of key matrix with ciphertext, mod 26
    plaintext = np.matmul(inv, cipher)
    plaintext = plaintext % 26

    # convert numbers to alphabet
    plaintext = plaintext.flatten()
    plaintext = [alphabet[int(i)] for i in plaintext]
    plaintext = ''.join(plaintext)
    print(plaintext)


if __name__ == "__main__":
    main()
