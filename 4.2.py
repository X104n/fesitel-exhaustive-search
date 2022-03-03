import keySearcher as a
import sys
import enc_py3 as e
import dec_py3 as d

def listMaker():
    xList = {}
    key = "0000000000000000"
    keyArray = a.staconverter(key)

    while(keyArray[0] != 2):
        sys.argv[2] = a.atsconverter(keyArray)
        output = e.main()

        xList[output] = a.atsconverter(keyArray)
        a.incrementKey(keyArray)
        print(a.atsconverter(keyArray))
    return xList

def decrypt(k):
    sys.argv[2] = a.atsconverter(k)
    return d.main()

if __name__ == "__main__":

    sys.argv.append("1")
    sys.argv.append("2")

    plainText = "10101010101010101010101010101010"
    cipher = "11000110100010110110000001101110"
    decKey = "0000000000000000"
    decKeyArray = a.staconverter(decKey)

    sys.argv[1] = plainText

    xList = listMaker()

    sys.argv[1] = cipher

    for i in range(len(xList)):
        middleCipher = decrypt(decKeyArray)
        if middleCipher in xList:
            print("Found the key")
            print(xList[middleCipher])
            print(a.atsconverter(decKeyArray))
            break
        else:
            a.incrementKey(decKeyArray)
            print(a.atsconverter(decKeyArray))
            