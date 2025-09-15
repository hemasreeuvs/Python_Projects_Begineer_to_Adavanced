alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text+=alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")

# def dencrypt(original_text, shift_amount):
#     output_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         output_text+=alphabet[shifted_position]
    # print(f"Here is the encoded result: {output_text} , result = {output_text}")

#Creating new one function to reduce the repetitive tasks

def caesar(original_text , shift_amount , encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
                shift_amount *= -1
    for letter in original_text:
        if letter  not in alphabet:
            output_text += letter
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        output_text+=alphabet[shifted_position]
    print(f"Here is the encoded result: {encode_or_decode}")   

should_continue = True

while should_continue :
        direction = input("Type encode to encrypt , type decode to decrypt\n").lower()
        shift = int(input("Type the shift number:\n"))
        text = input("Enter the message:\n").lower()

        caesar(original_text = text , shift_amount = shift ,encode_or_decode= direction)
        restart = input ("Typle 'yes' if you want to go again .Otherwise , type 'no' .\n")
        if restart == "no":
             should_continue = False
             print ("Goodbye") 
 

