import dec_py3 as d
import enc_py3 as e
import sys

plainText = "10101010101010101010101010101010"
cipher = "11000110100010110110000001101110"

encKey1 = "0010000101011010"
encKey2 = "0011001101011101"

sys.argv.append("")
sys.argv.append("")

sys.argv[1] = plainText
sys.argv[2] = encKey1

a = e.main()

sys.argv[1] = a
sys.argv[2] = encKey2

b = e.main()

print(b)


