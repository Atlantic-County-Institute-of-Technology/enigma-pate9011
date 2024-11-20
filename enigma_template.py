# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: riskypaddle
# created: 11.18.2024
# last update:  11.18.2024
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"

# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message(dinput):
        basic_input = input("Enter a rotation cipher key (Press Enter for a random value): ")

        if basic_input.strip() == "":
            rotation = random.randint(1, 25)  # Random value between 1 and 25
        else:
            rotation = int(basic_input) % 26  # Ensure rotation is within 0-25

        encoded_message = ""

        for char in dinput:
            if char.isalpha():  # Check if the character is a letter
                # Shift character, rap around if necessary
                shifted_char = chr((ord(char) - ord('a') + rotation) % 26 + ord('a'))
                encoded_message += shifted_char
            else:
                encoded_message += char  # Non-alphabetic characters remain unchanged
        leaving = (f"Original: {dinput}\nUsed key of {rotation} to create:\n{encoded_message}")
        print(leaving)
        basic_input=input(f"Please select an option:\n"
                            f"[1]: Write/Overwrite file\n"
                            f"[2]: Exit\n")
        if int(basic_input) == 1:
            newfile=input("Enter pre-existing file name or create a name")
            f = open(newfile, "w")
            f.write(leaving)
            f.close()
            return("Done added:\n"+ leaving)
        else:
            return("Sucessfully Exited")
pass

# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file(file):
    print(encode_message(file))
    pass

# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    pass

# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):
   pass


# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            oinput = input("What would you like to be ciphered?").lower()
            print(encode_message(oinput))
        elif selection == "2":
            readW = input("What file would you like to be encoded")
            try:
                x = open(readW, "r")
                f= (x.read())
                encode_file(f)
            except FileNotFoundError:
                print(f"Error: The file '{readW}' was not found.")
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()