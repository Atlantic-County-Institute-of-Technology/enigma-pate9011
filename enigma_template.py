# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: riskypaddle
# created: 11.18.2024
# last update:  11.18.2024
import random


def file_save(leaving):
    print(leaving)
    basic_input = input(f"Please select an option:\n"
                        f"[1]: Write/Overwrite file\n"
                        f"[2]: Exit\n")
    if int(basic_input) == 1:
        newfile = input("Enter pre-existing file name or create a name")
        f = open(newfile, "w")
        f.write(leaving)
        f.close()
        return ("Done added:\n" + leaving)
    else:
        return ("Sucessfully Exited")
pass

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
        print(file_save(leaving))
pass

def decode_file(dinput):
    basic_input = input("Enter a rotation cipher key (Press Enter for a random value): ")
    basic_input=0 if basic_input=="" else int(basic_input)
    if basic_input==0:
        decode_unknown_key(dinput)
    else:
        decoded_text = ""
        for char in dinput:
            if char.isalpha():
                decoded_char = chr((ord(char) - ord('a') - int(basic_input)) % 26 + ord('a'))
                decoded_text += decoded_char
            else:
                decoded_text += char
        leaving = (f"Encoded: {dinput}\nUsed key of {basic_input} to create:\n{decoded_text}")
        print(file_save(leaving))
        return decoded_text

pass


# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(dinput):
    leaving=""
    for x in range(26):
        decoded_text = ""
        for char in dinput:
            if char.isalpha():
                decoded_char = chr((ord(char) - ord('a') - int(x)) % 26 + ord('a'))
                decoded_text += decoded_char
            else:
                decoded_text += char
        leaving = leaving+(f"\nUsed key of {x} to create:\n{decoded_text}")
    print(file_save(leaving))
    return decoded_text
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
                print(encode_message(f))
            except FileNotFoundError:
                print(f"Error: The file '{readW}' was not found.")
        elif selection == "3":
            readW = input("What file would you like to be Decoded")
            try:
                x = open(readW, "r")
                f= (x.read())
                print(decode_file(f))
            except FileNotFoundError:
                print(f"Error: The file '{readW}' was not found.")
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()