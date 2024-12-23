def decode_the_cipher(cipher , shift):
    text = ""
    for letter in cipher:
        correct_pos = alphabet.index(letter) - shift
        if (correct_pos < 0):
            temp = correct_pos
            correct_pos = 26 + temp 
        text += alphabet[correct_pos]
    return text

def encode_the_text(org_text, shift):
    cipher_text = ""
    for letter in org_text:
        shifted_pos = alphabet.index(letter) + shift
        if(shifted_pos<=25):
            cipher_text += alphabet[shifted_pos]
        else:
            shifted_pos = shifted_pos - 26
            cipher_text += alphabet[shifted_pos]    
    return cipher_text

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

direction = input("Enter the function that you want to perform: \n").lower()

if direction == "encode":
    text = input(f"Enter the text that you want to {direction}\n")
    shift = int(input("Enter the number of spaces by which you want to shift: \n"))
    print(f"--------------------\n{encode_the_text(text,shift)}\n-------------------------")
else:
    cipher = input(f"Enter the cipher that you want to {direction}\n")
    shift = int(input("Enter the number of spaces by which you want to shift: \n"))
    print(f"----------------\n{decode_the_cipher(cipher, shift)}\n--------------------")    

