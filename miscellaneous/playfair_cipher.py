import string
import unicodedata
import sys


# Constant values
ALPHABET_KEYS = string.ascii_lowercase
# To use 25 letters we remove letter J, and use letter I instead.
# Should another letter be removed, change the tuple below.
# First value is the removed letter, and second value is the letter to be used instead
SWITCH_KEYS = ('j', 'i')

# Remove the letter chosen above from our alphabet
ALPHABET_KEYS = ALPHABET_KEYS.replace(SWITCH_KEYS[0], "")


def encrypt(message, key):
    matrix = build_matrix(key)
    return matrix


def decrypt(message, key):
    matrix = build_matrix(key)
    return matrix


def build_matrix(key):
    # Sanitize key
    key = key.lower().replace(" ", "")
    key = remove_accents(key)

    # Replacing the the removed letter
    key = key.replace(SWITCH_KEYS[0], SWITCH_KEYS[1])

    # Let's remove duplicates
    remaining_keys = ALPHABET_KEYS
    for letter in key:
        if letter in remaining_keys:
            # If it is in the alphabet_keys, we should remove it from the alphabet
            remaining_keys = remaining_keys.replace(letter, "", 1)
        else:
            # If it is not, that is because we already removed earlier and should
            # remove the duplicate from our key

            # Find the index of the second occurrence, then slice and concatenate it.
            duplicated_index = key.index(letter, key.index(letter) + 1)
            key = key[0:duplicated_index] + key[duplicated_index + 1:]

    key = key + remaining_keys
    # Now our key has all the 25 letters and each letter occurring just once.
    # Let's break our key into a 5x5 matrix
    # First let's break our key into 5 strings of size 5
    matrix = [key[5*i:5*(i+1)] for i in range(0,5)]

    # We have a list of 5 elements and each element has size 5, it can be seen as a 5x%
    # matrix but I will cast each element into a list as well just to make it more cohesive
    matrix = [list(x) for x in matrix]

    return matrix


def remove_accents(text):
    # breaks accents from letters
    text = unicodedata.normalize('NFKD', text)
    # converts to ASCII ignoring errors (that would be caused by the accents)
    text = text.encode('ASCII', 'ignore')
    # convert back to utf-8 and it is done.
    return text.decode('utf-8')


if __name__ == "__main__":
    build_matrix(" OLA MUNDO ")


    #https://en.wikipedia.org/wiki/Playfair_cipher