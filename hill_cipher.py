# Hill cipher decryption tool

# Sevastian Zare

# 28 assignment

# Decrypt the Hill cipher:

# the ciphertext is: ZUIAZHZUSCYQOXEFFICVCPDGEMIBPTEZIMMRQTXMEIYDBEJPBXUOUMZUUYSCEUASTRCCVBQKGBDJZNGAPORZYQSZLUYQ    
# the key is: 
# [6, 17] 
# [17, 5]


# Decryption. 
# Decrypting with the Hill cipher is built on the following operation: 
# D(K, C) = (K^(-1) *C) mod 26 
# Where K is our key matrix and C is the ciphertext in vector form. 
# Matrix multiplying the inverse of the key matrix with the ciphertext produces the decrypted plaintext.

# python code implementation
import numpy as np

def det_inv(key, n):
    # key 
    a, b, c, d = key
    # determinant
    dt = 1/(a*d - c*b) % n
    inverse = dt*d%n, -dt*b%n, -dt*c%n, dt*a%n
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
    n = 26

    # key
    key = [6, 17, 17, 5]
    print("key: ", key)

    # ciphertext
    ciphertext = [25, 20, 8, 0]
    print("ciphertext: ", ciphertext)

    # determinant
    dt, inv_key = det_inv(key, n)
    print("determinant: ", dt)
    print("inverse key: ", inv_key)
    
    # plaintext
    plaintext = multiply(inv_key, ciphertext, n)
    print("plaintext: ", plaintext)


if __name__ == "__main__":
    main()


