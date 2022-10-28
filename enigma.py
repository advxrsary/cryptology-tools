alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def numerify(text):
    res = []
    for letter in text:
        if letter != ' ':
            res.append(alphabet.index(letter))
    return res

def stringify(numbers):
    res = ''
    for number in numbers:
        letter = alphabet[number]
        res += letter
    return res

def rot(m, a):
    return (a+m) % len(alphabet)

def rsubst(rot, a):
    return rot.index(a)

def deEnigma(key, L1, L2, ciphertext):
    cipherVals = numerify(ciphertext)
    messageVals = []
    m1 = key[0]
    m2 = key[1]
    rIdx = 0

    for cipherVal in cipherVals:
        val = cipherVal
        val = rot(m2, val)
        val = rsubst(L2, val)
        val = rot(-m2, val)
        val = rot(m1, val)
        val = rsubst(L1, val)
        val = rot(-m1, val)

        m1 += 1
        rIdx += 1
        if (rIdx % len(alphabet)) == 0:
            m2 += 1

        messageVals.append(val)
    


    return stringify(messageVals)

def key_brute_force(ciphertext, L1, L2):
    for m1 in range(len(alphabet)):
        for m2 in range(len(alphabet)):
            key = [m1, m2]
            message = deEnigma(key, L1, L2, ciphertext)
            if '' in message:
                print(key, message, '\n')

def main():
    key = [6, 14]
    L_1=[10, 2, 11, 18, 8, 20, 19, 25, 23, 1, 15, 9, 14, 6, 24, 0, 17, 7, 22, 21, 4, 12, 5, 3, 16, 13]
    L_2=[14, 2, 7, 20, 18, 9, 19, 25, 23, 1, 13, 17, 22, 5, 3, 0, 24, 8, 21, 10, 11, 12, 15, 4, 6, 16]
    R =[2, 4, 0, 6, 1, 11, 3, 8, 7, 13, 16, 5, 15, 9, 18, 12, 10, 19, 14, 17, 25, 22, 21, 24, 23, 20]
    ciphertext = "NRKFL FIWVO BFKQK UJOGW ZHTBX TSNEO QWTZX LLTOT KEWGM OFKMX KABMO AVLKB KNRTV IDQXD QUYOG GQSRV BDDKO OXGNG WTDGC BNUON ENAOG LMQVQ GEXCN ZTVGH LWQNK ZZXCL YKMQO FJDJG LMUNI VUAKV QLBNW TIXQJ LOFGX ZXBVH PSUQA CKTKG ZCAQM VTDWL GWBFE AYZFY HHJTL TIFJG JVSCN DJSRN RIOFL DZJKP QKYHO ZTMZB XAKLH DSOJA EDLBC OUNJN OJAGZ WVMPS YDCOM XJVUZ GOSOL VJSFX LBBIF TRKRV BMPED XEHCV RQWFV EQUCZ HQLPQ GUMKD NJXLF BHMQE FVYFL PJFQA QZQUV JZHFN DAJQO WRUVH ZQYHC JGWBP PNFQJ PUGYZ FPJFH BODBU ZKKYB DFKOT SAKPN CPCRV"
    # reflection
    print(deEnigma(key, L_1, L_2, ciphertext))

if __name__ == "__main__":
    main()