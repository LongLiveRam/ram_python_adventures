# make a personal cipher text using randomly shuffled a-z A-Z 0-9 and symbols
# encryption code will be randomized everytime program runs

import random
import string

chars = list(" " + string.punctuation + string.ascii_letters + string.digits)

key = chars.copy()
random.shuffle(key)
plain_text = input("Please enter your phrase: ")
cipher_text = ""
# encrypt
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(cipher_text)
# decrypt

for letter in cipher_text:
    index = key.index(letter)
    print(chars[index], end="")
