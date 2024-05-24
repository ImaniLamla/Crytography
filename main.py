'''
SOURCES:
#https://pynative.com/python-generate-random-string/#h-how-to-create-a-random-string-in-python
#https://docs.python.org/3/library/string.html#
#https://www.w3schools.com/python/ref_random_choice.asp
#https://www.tutorialspoint.com/caesar-cipher-in-cryptography
#https://www.w3schools.com/python/ref_func_ord.asp
#https://stackoverflow.com/questions/59233846/caesar-cipher-for-numbers-in-c

EQUATION: https://codedamn.com/news/cryptography/caesar-cipher-introduction

NEW INFORMATION LEARNED:
* string.ascii_letters = concatenation of ascii lower and uppercase
* string.digits = stores all digits 1-9
* choice() = method returns a randomly selected element from the specified sequence
* string.join() = takes all items in an iterable and joins them into one string
* ord() = gets numeric value for the character
* chr() = converts numeric value into its char
'''

import random # used to generate random strings and numbers
import string # used to access string methods

random_strings = []     #declare a list that will contain the randomly generated strings
encrypted_strings = []  #declare a list that will contain the encrypted strings

'''
This method generates the random strings. It uses the random.choice method to return a randomly selected element from a string containing the 
alphabet in upper and lowercase as well as digits 0-9 inclusive. It appends each randomly chosen character to a string variable that will 
store the random  string.
'''
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))   #will add each character length or 7 times
    return random_string                                                        #returns the string

'''
This method uses the random number generated between 0-1 to display the direction shift and negate the key if the shift is to the left.
'''
def check_shift(direction, shift):
    print("Shift value: ", shift)
    if direction == 0:                   # 0 = right(positive) shift so the characters move forward
        print("Shift Direction: Right")
        key = shift                      # the key stays the same (positive)

    elif direction == 1:                 # 1 = left(negative) shift so the characters move backward
        print("Shift Direction: Left")
        key = shift * -1                 # negate the key by multiplying it by -1
    print()

    return key                           # returns the key

'''
This method encrypts the random strings using the Caesar Cipher on the upper and lowercase alphabet as well as the digits. 
'''
def encrypt(direction, shift):

    cipher = ''                             # stores the encrypted string

    key = check_shift(direction, shift)     # calls the check_shift method to negate the key if necessary

    for i in random_strings:                # iterates through the elements of the list
        for j in i:                         # iterates through each character in the string

            ascii = ord(j)                  # converts the character into its numeric/ascii value

            if j.isdigit():                 # runs if the character is a digit
                ascii = (ascii - ord('0') + key) % 10 + ord('0')

            elif j.isupper():               # runs if the character is uppercase
                ascii = (ascii - ord('A') + key) % 26 + ord('A')
            else:                           # runs if the character is lowercase
                ascii = (ascii - ord('a') + key) % 26 + ord('a')

            cipher += chr(ascii)            # converts the numeric value back into a char and appends it to the ciphered string

        encrypted_strings.append(cipher)    # appends each new ciphered string to the list containing the encrypted strings
        cipher = ""                         #clears cipher

'''
This method displays the original strings alongside their encrypted ciphers.
'''
def display():

    print(f'{"Original"}{"Encrypted":>15}')
    print()
    for i in range(50):
        print(f'{random_strings[i]}{encrypted_strings[i]:>15}')
    print()
    print("List length: ", len(random_strings), "elements")

if __name__ == '__main__':                       # main method

    direction_shift = random.randint(0,1)  # generates a random number (0-1) for the direction shift, 0 = right shift 1 = left shift
    place_shift = random.randint(1, 10)    # generates a random number (1-10) that dictates how many places each character shifts

    for i in range(50):                          # this loop populates the random_strings list with 50 randomly generated strings
        random_strings.append(generate_random_string(7)) #calls the generate_random_strings method to generate strings 7 characters long

    encrypt(direction_shift, place_shift)         # calls the encrypt method to encrypt the original strings using the Caesar Cipher

    display()                                    # calls the display method to display the 2 lists of strings alongside each other