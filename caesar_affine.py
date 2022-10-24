# Sevastian Zare

# 28 assignment 
# 1. Decrypt the affine Ceasar cipher:

# AIMCG BKOLK VBCLA NPIMM CAITI 
# LKMUK AIMCS JKLBK LCPKP CGBCK 
# PBOMC KXLLI TPILC GLUXN IPMKL 
# UIX  

        

# manual decryption
def affine_decrypt(ciphertext, a, b):
    plaintext = ''
    for c in ciphertext:
        if c.isalpha():
            x = ord(c) - ord('A')
            x = (a * x - b) % 26
            plaintext += chr(x + ord('A'))
        else:
            plaintext += c
    return plaintext

# automatic decryption with brute force and filter
def calc_keys(ciphertext):
    for l1 in range(1, 26):
        if 26 % l1 != 0:
            for l2 in range(0, 26):
                plaintext = affine_decrypt(ciphertext, l1, l2)
                if plaintext.startswith(''):
                    print(l1, l2, plaintext)

def main():
    ciphertext = 'ZUIAZHZUSCYQOXEFFICVCPDGEMIBPTEZIMMRQTXMEIYDBEJPBXUOUMZUUYSCEUASTRCCVBQKGBDJZNGAPORZYQSZLUYQ'
    calc_keys(ciphertext)
    

if __name__ == "__main__":
    main()