a_string = "abc"
a_byte_array = bytearray(a_string, "utf8")
byte_list = []

for byte in a_byte_array:
    binary_representation = bin(byte)
    byte_list.append(binary_representation)


print(byte_list)
