import keySearcher as a
import sys
import enc_py3 as e
import dec_py3 as d

def correctKey(k1, k2, c, p) -> bool:
    
    # Here we need to first test the first key then use the output of the first network as input for the next network
    # And if we get the right cipher text we have found the right pair of keys

    output1 = [] # Uses the enc.py to find the output

    output2 = [] # Uses k2 and output1 to find the final ciphertext

    # And if output2 corresponds to c we have found our pair

    if(output2 == c):
        return True
    else:
        return False

def listMaker(p):
    xList = {}
    key = "0000000000000000"
    keyArray = a.staconverter(key)

    sys.argv[1] = a.atsconverter(p)

    while(keyArray[0] != 2):
        sys.argv[2] = a.atsconverter(keyArray)
        output = e.main()

        xList[output] = a.atsconverter(keyArray)
        a.incrementKey(keyArray)
        print(keyArray)
    return xList

def decrypt(c, k):
    sys.argv[1] = a.atsconverter(c)
    sys.argv[2] = a.atsconverter(k)
    return d.main()









import itertools
lst = list(itertools.product([0, 1], repeat=16))

def tupleToString(tuple):
    tupleString = ""

    for x in range (len(tuple)):
        tupleString += str(tuple[x])
    return tupleString



def keyTableEnc():
    keyTableWorking = {}

    for x in range (len(lst)):
        keySide = tupleToString(lst[x])
        sys.argv[2] = keySide
        encSide = e.main()
        keyTableWorking[encSide] = keySide
        print(keySide)

    return keyTableWorking

sys.argv.append("1")
sys.argv.append("2")
plainText = "10101010101010101010101010101010"
sys.argv[1] = plainText


print("Creating table.")
xList = keyTableEnc()
print("Table finished.")








if __name__ == "__main__":

    sys.argv.append("1")
    sys.argv.append("2")

    plainText = "10101010101010101010101010101010"
    cipher = "11000110100010110110000001101110"
    decKey = "0000000000000000"


    plainTextArray = a.staconverter(plainText)
    cipherArray = a.staconverter(cipher)
    decKeyArray = a.staconverter(decKey)

    #xList = #listMaker(plainTextArray)

    for i in range(len(xList)):
        x123 = decrypt(cipherArray, decKeyArray)
        if x123 in xList:
            print("Found the key")
            print(xList[x123])
            print(decKeyArray)
            break
        else:
            decKey = a.staconverter(decKeyArray)
            decKey = a.incrementKey(decKeyArray)
            decKey = a.atsconverter(decKeyArray)
            

