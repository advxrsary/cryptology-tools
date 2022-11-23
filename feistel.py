# 1. Feistel cipher, 3 iterations, the key =[227, 35, 140]
# Decrypt the ciper in EBC mode 

# Sage Math code:
# def iter (M, k,f):
#     r=M[1]
#     x = 1-M[0]^^eval(f)
#     return [x, r]

# f='(r|k)^((k//16)&r)'
# M=[186, 253]
# k=227
# iter (M,k, f)
# chr(253)+chr(186)



# Cipher = [[66, 253], [89, 229], [66, 226], [69, 237], [68, 250], [75, 234], [88, 246], [66, 226], [91, 225], [71, 224], [73, 234], [73, 235], [93, 227], [95, 249], [65, 248], [89, 231], [95, 225], [87, 224], [72, 224], [66, 253], [72, 228], [78, 228], [78, 242], [77, 242], [95, 233], [79, 236], [79, 242], [74, 235], [95, 237], [93, 247], [93, 225], [78, 232], [67, 252], [65, 227], [47, 147]]
# Keys = [227, 35, 140]
# Feistel Network formula: Rm = Rm-2 xor F(Km, Rm-1), R-1 = L0
# M is a single pair from the cipher
# k is a single key value from the keys
# f is the function to be applied to M and k
# Each iteration should result in a new cipher text list

# Keys should be applied in reverse order
# At the end interchanging the left and right parts of the cipher text

# Python code:

def iter (M, k,f):
    r = M[1]
    l = M[0] ^ eval(f)
    return [r, l]

def last_iter (M, k,f):
    r = M[1]
    l = M[0] ^ eval(f)
    return [l, r]


def main():
    cipher = [[66, 253], [89, 229], [66, 226], [69, 237], [68, 250], [75, 234], [88, 246], [66, 226], [91, 225], [71, 224], [73, 234], [73, 235], [93, 227], [95, 249], [65, 248], [89, 231], [95, 225], [87, 224], [72, 224], [66, 253], [72, 228], [78, 228], [78, 242], [77, 242], [95, 233], [79, 236], [79, 242], [74, 235], [95, 237], [93, 247], [93, 225], [78, 232], [67, 252], [65, 227], [47, 147]]
    keys = [227, 35, 140]
    f = '(r|k)^((k//16)&r)'
    for i in range(len(cipher)):
        # first iteration
        cipher[i] = iter(cipher[i], keys[2], f)
        # second iteration
        cipher[i] = iter(cipher[i], keys[1], f)
        # third iteration
        cipher[i] = last_iter(cipher[i], keys[0], f)
        print(chr(cipher[i][0])+chr(cipher[i][1]), end='')
    print()

if __name__ == "__main__":
    main()