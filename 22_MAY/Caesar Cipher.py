alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(input_text, shift_amount, direction):
  end_text = ""
  for letter in input_text:
    position = alphabet.index(letter)
    if direction == "encode":
      new_position = position + shift_amount
    elif direction == "decode":
      new_position = position - shift_amount
    else:
      print(f"{direction} is an invalid input for direction, please enter 'encode' to encrypt, type 'decode' to decrypt")
    end_text += alphabet[new_position]
    print(f"The {direction}d text: {end_text}")
  

caesar(input_text = text, shift_amount = shift, direction = direction)
