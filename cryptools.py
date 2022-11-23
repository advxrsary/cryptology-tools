#! /bin/python3

# Sevastian Zare
# Cryptology Tools
# All-in-one Tools for Cryptology

# This is a file that runs all the tools.

import sys
import os
sys.path.insert(0, os.getcwd())

from feistel import feistel
from caesar import affine
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
        affine.main()
    elif choice == 2:
        hill.main()
    elif choice == 3:
        feistel.main()
    elif choice == 4:
        enigma.main()
    else:
        print('Invalid choice!')

if __name__ == "__main__":
    main()