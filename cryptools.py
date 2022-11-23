#! /bin/python3

# Sevastian Zare
# Cryptology Tools
# All-in-one Tools for Cryptology

# This is a file that runs all the tools.

import sys
import os
sys.path.insert(0, os.getcwd())

from feistel import ebc
from affine import affine
from hill import hill
from enigma import enigma

def main():
    print('''
    Welcome to Cryptology Tools!
    This is a file that runs all the tools.
    ''')
    print('''
    1. Caesar Affine Cipher
    2. Hill Cipher
    3. Feistel Cipher
    4. Enigma Cipher
    ''')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        decrypt_affine()
    elif choice == 2:
        hill.main()
    elif choice == 3:
        ebc.main()
    elif choice == 4:
        enigma.main()
    else:
        print('Invalid choice!')

def decrypt_affine():
    ciphertext = input('Enter ciphertext (single line): ')
    chars = input(
        'Enter the first characters of the plaintext (leave empty for all results): ')
    affine.calc_keys(ciphertext, chars)

if __name__ == "__main__":
    main()