from array import array
import string
import sys
import enc_py3 as b

def staconverter(string) -> array:
    result = []
    for i in range(len(string)):
        if string[i] == '0':
            result.append(0)
        else:
            result.append(1)
    return result

def atsconverter(a) -> string:
    result = ""
    for i in range(len(a)):
        if a[i] == 0:
            result = result + "0"
        else:
            result = result + "1"
    return result

def incrementKey(k) -> array:
    k[15] = k[15] + 1
    for i in range(len(k)-2, -1 , -1):
        if(k[i+1] == 2):
            k[i+1] = k[i+1] % 2
            k[i] = k[i] + 1
    return k

def correctKey(k, c, p) -> bool:

    # Plug in the plaintext and the key
    # If the output ciphertext does not correspond to the given ciphertext
    # The we return flase, if it is the same return the value true
    sys.argv[1] = atsconverter(p)
    sys.argv[2] = atsconverter(k)
    output = b.main() # Output of the enc.py0
    if(output == atsconverter(c)):
        return True
    else:
        return False
    
if __name__ == "__main__":

    sys.argv.append("1")
    sys.argv.append("2")

    plainText = "10101010101010101010101010101010"
    key = "0000000000000000"
    cipher = "11110100011101010101100111111110"

    plainTextArray = staconverter(plainText)
    keyArray = staconverter(key)
    cipherArray = staconverter(cipher)

    while True:
        if(correctKey(keyArray, cipherArray, plainTextArray)):
            print("Found the key")
            print("The key is: " , keyArray)
            break
        else:
            keyArray = incrementKey(keyArray)
        
