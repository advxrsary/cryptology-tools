def iter (M, k,f):
    r = M[1]
    l = M[0] ^ eval(f)
    return [r, l]

def last_iter (M, k,f):
    r = M[1]
    l = M[0] ^ eval(f)
    return [l, r]


def main():
    cipher = eval(input('Enter ciphertext (single line): '))
    # Example of input: [[66, 253], [89, 229], [66, 226], [69, 237], [68, 250], [75, 234], [88, 246], [66, 226], [91, 225], [71, 224], [73, 234], [73, 235], [93, 227], [95, 249], [65, 248], [89, 231], [95, 225], [87, 224], [72, 224], [66, 253], [72, 228], [78, 228], [78, 242], [77, 242], [95, 233], [79, 236], [79, 242], [74, 235], [95, 237], [93, 247], [93, 225], [78, 232], [67, 252], [65, 227], [47, 147]]
    keys = eval(input('Enter keys (single line): '))
    # Example of input: [227, 35, 140]
    # In your formula replace all m's with r's
    # before: (m|k)^((k//16)&m)
    # after:  (r|k)^((k//16)&r)
    f = input('Enter f: ')
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