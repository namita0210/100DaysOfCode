def decode_the_cipher():
    pass

def encode_the_text(org_text, shift):
    cipher_text = ""
    for letter in org_text:
        shifted_pos = alphabet.index(letter) + shift
        if(shifted_pos<=25):
            cipher_text += alphabet[shifted_pos]
        else:
            shifted_pos = shifted_pos - 26
            cipher_text += alphabet[shifted_pos]    
    return print(f"-------------\nEncoded Text: {cipher_text}\n----------------")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

direction = input("Enter the function that you want to perform: \n").lower()

text = input(f"Enter the text that you want to {direction}\n")

if direction == "encode":
    shift = int(input("Enter the number of spaces by which you want to shift: \n"))
    encode_the_text(text,shift)
else:
    decode_the_cipher()    

