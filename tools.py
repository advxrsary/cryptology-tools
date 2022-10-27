#! /bin/python3

# Sevastian Zare
# Cryptology Tools
# All-in-one Tools for Cryptology

# This is a file that runs all the tools.

import caesar_affine
import hill_cipher
# import vigenere_cipher
# import playfair_cipher
# import rsa
# import elgamal
# import diffie_hellman
# import aes
# import des
# import blowfish

def main():
    print('''
    Welcome to Cryptology Tools!
    This is a file that runs all the tools.
    ''')
    print('''
    1. Caesar Affine Cipher
    2. Hill Cipher
    3. Vigenere Cipher (unavailable)
    4. Playfair Cipher (unavailable)
    5. RSA (unavailable)
    6. ElGamal (unavailable)
    7. Diffie-Hellman (unavailable)
    8. AES (unavailable)
    9. DES (unavailable)
    10. Blowfish (unavailable)
    ''')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        caesar_affine.main()
    elif choice == 2:
        hill_cipher.main()
    # elif choice == 3:
    #     vigenere_cipher.main()
    # elif choice == 4:
    #     playfair_cipher.main()
    # elif choice == 5:
    #     rsa.main()
    # elif choice == 6:
    #     elgamal.main()
    # elif choice == 7:
    #     diffie_hellman.main()
    # elif choice == 8:
    #     aes.main()
    # elif choice == 9:
    #     des.main()
    # elif choice == 10:
    #     blowfish.main()
    else:
        print('Invalid choice!')

if __name__ == "__main__":
    main()