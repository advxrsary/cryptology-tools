# Hill cipher decryption tool
# Sevastian Zare
# 28 assignment
# Decrypt the Hill cipher:

# the ciphertext is: ZUIAZHZUSCYQOXEFFICVCPDGEMIBPTEZIMMRQTXMEIYDBEJPBXUOUMZUUYSCEUASTRCCVBQKGBDJZNGAPORZYQSZLUYQ
# the key is:
# [6, 17, 17, 5]


# Decryption.
# Decrypting with the Hill cipher is built on the following operation:
# D(K, C) = (K^(-1) *C) mod 26
# Where K is our key matrix and C is the ciphertext in vector form.
# Matrix multiplying the inverse of the key matrix with the ciphertext produces the decrypted plaintext.

# python code implementation
import numpy as np

# convert ciphertext to numbers
def cipher_alphabet2num(numcipher):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numcipher = numcipher.replace(' ', '')
    numcipher = numcipher.upper()
    numcipher = [alphabet.index(c) for c in numcipher]
    return numcipher


# determinant
def det(key, n):
    # key
    a, b, c, d = key
    # determinant
    dt = 1/(a*d - c*b) % n
    inverse = dt*d % n, -dt*b % n, -dt*c % n, dt*a % n
    return dt, inverse


def multiply(inv_key, ciphertext, n):
    # key
    a, b, c, d = inv_key
    # ciphertext
    w, x, y, z = ciphertext
    # plaintext
    p = [a*w + b*x % n, c*w + d*x % n, a*y + b*z % n, c*y + d*z % n]
    return p


def main():
    # n
    n = input('Enter modulus: ')

    # key
    key = input('Enter key (split by commas): ')
    key = key.replace('[', '')
    key = key.replace(']', '')
    key = key.replace(' ', '')
    key = key.split(',')

    

    # ciphertext
    ciphertext = input('Enter ciphertext: ')
    ciphertext = ciphertext.replace(' ', '')
    ciphertext = ciphertext.upper()


    # convert ciphertext to numbers
    numcipher = cipher_alphabet2num(ciphertext)

    # convert numbers to vector
    vector = numcipher2vector(numcipher)

    # determinant
    dt, inv_key = det_inv(key, n)

    # plaintext
    plaintext = multiply(inv_key, ciphertext, n)
    print("ciphertext: ", str(ciphertext))
    print("key: ", key, '\n')
    print("numcipher: ", str(numcipher))
    print("vector: ", str(vector), '\n')
    print("determinant: ", dt)
    print("inverse key: ", inv_key, '\n')
    print("plaintext: ", plaintext)


if __name__ == "__main__":
    main()
