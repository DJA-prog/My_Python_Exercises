import binascii
#ascii to bin
bina = bin(int(binascii.hexlify('hello'), 16))
print(bina)
#bin to ascii
n = int('00110100001100101011011000110110001101111', 2)
text = binascii.unhexlify('%x' % n)
print(text)
