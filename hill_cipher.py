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

def det(key, n):
    # key 
    a, b, c, d = key
    # modulus
    n = 26
    # determinant
    dt = 1/(a*d - b*c) % n

    return dt

def calc_inverse(dt, key, n):
    # inverse of key
    inv = [dt * key[3], -dt * key[1], -dt * key[2], dt * key[0]]
    return inv

def multiply(inv_key, ciphertext, n):
    # key
    a, b, c, d = inv_key
    # ciphertext
    w, x, y, z = ciphertext

    # modulus
    n = 26

    # plaintext
    q = (a*x + b*y) % n
    r = (c*x + d*y) % n
    s = (a*z + b*w) % n
    t = (c*z + d*w) % n

    return q, r, s, t

def main():
    # key
    key = [6, 17, 17, 5]
    print("key: ", key)

    # determinant
    dt = det(key, 26)
    print("det: ", dt)

    # inverse of key
    inv = calc_inverse(dt, key, 26)
    print("inverse: ", inv)

    # ciphertext first 4 letters
    # ZUIAZHZUSCYQOXEFFICVCPDGEMIBPTEZIMMRQTXMEIYDBEJPBXUOUMZUUYSCEUASTRCCVBQKGBDJZNGAPORZYQSZLUYQ
    ciphertext = [25, 20, 8, 0]
    print("ciphertext: ", ciphertext)

    # plaintext
    plaintext = multiply(inv, ciphertext, 26)
    print("plaintext: ", plaintext)

if __name__ == "__main__":
    main()

