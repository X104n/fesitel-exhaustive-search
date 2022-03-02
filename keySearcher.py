from array import array
import re
import string
from xmlrpc.client import boolean

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
            result.append("0")
        else:
            result.append("1")
    return result

def incrementKey(k) -> array:
    k[15] = k[15] + 1
    for i in range(len(k)-2, -1 , -1):
        if(k[i+1] == 2):
            k[i+1] = k[i+1] % 2
            k[i] = k[i] + 1
    return k

def correctKey(k, c) -> bool:
    if(k == c):
        return True
    else:
        return False




if __name__ == "__main__":

    plainText = "10101010101010101010101010101010"
    key = "0000000000000000"
    compare = "1111111000011111"
    cipher = "11110100011101010101100111111110"

    plainTextArray = staconverter(plainText)
    keyArray = staconverter(key)
    compareArray = staconverter(compare)
    cipherArray = staconverter(cipher)

    while True:
        if(correctKey(keyArray, compareArray)):
            print("Found the key")
            print("The key is: " , keyArray)
            break
        else:
            keyArray = incrementKey(keyArray)
        

