#! /bin/python3

# Sevastian Zare
# Cryptology Tools
# All-in-one Tools for Cryptology

# This is a file that runs all the tools.

import caesar
import enigma
import feistel
import hill

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
        caesar.caesar.main()
    elif choice == 2:
        hill.hill()
    elif choice == 3:
        feistel.main()
    elif choice == 4:
        enigma.enigma()
    else:
        print('Invalid choice!')

if __name__ == "__main__":
    main()