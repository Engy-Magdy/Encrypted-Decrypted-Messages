#Greeting
print("""
***************************************
Welcom to decrypted & encrypted program
****************************************
""")
#importing
import string
#Choose encrypted or decrypted
your_choice=input("Do you want an encrypted message (E.M) or decrypted message (D.M)?\n").lower()

# The function when you chose encrypted
def encrypted_message(message,shift):
        alphabet=string.ascii_lowercase
        encrypted_message=""
        for letter in message:
            if letter.lower() in alphabet:
                original_position=alphabet.index(letter.lower())
                new_position=(original_position+shift)%26
                encrypted_letter=alphabet[new_position]
                if letter.isupper():
                    encrypted_letter=encrypted_letter.upper()
                encrypted_message+=encrypted_letter
            else:
                encrypted_message+=letter
        print("""
***************************
This your encrypted message
****************************""")
        
        print(encrypted_message)
    
# The function when you chose decrypted
def decrypted_message(message,shift):
        alphabet=string.ascii_lowercase
        decrypted_message=""
        for letter in message:
            if letter.lower() in alphabet:
              original_position=alphabet.index(letter.lower())
              new_position=(original_position-shift)%26
              decrypted_letter=alphabet[new_position]
              if letter.isupper():
                decrypted_letter=decrypted_letter.upper()
              decrypted_message+=decrypted_letter
            else:
              decrypted_message+=letter
        print("""
***************************
This your decrypted message
****************************
""")      
        print(decrypted_message)
#your_inputs
your_message=input("Please,Type your message:\n")
shift_number=int(input("please,Type a shift number:\n"))
if your_choice=="encrypted" or your_choice== "e.m":
    encrypted_message(message=your_message,shift=shift_number)
elif your_choice=="decrypted"or your_choice=="d.m":
    decrypted_message(message=your_message,shift=shift_number)
else:
    print(f"Sorry {your_choice} is invalid choice")



