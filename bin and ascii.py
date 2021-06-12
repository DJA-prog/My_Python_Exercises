import binascii
#ascii to bin
#a_byte_array = bytearray('hello', "utf8")
#bin(int(binascii.hexlify(a_byte_array), 16))
#print(bin(int(binascii.hexlify('hello'), 16)))
#bin to ascii
n = int('0b110100001100101011011000110110001101111', 2)
text = binascii.unhexlify('%x' % n)
print(text)
