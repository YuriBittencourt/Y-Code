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
    # Sanitize our message
    message = sanitize_string(message)
    key = sanitize_string(key)

    # Replacing the removed letter
    message = message.replace(SWITCH_KEYS[0], SWITCH_KEYS[1])
    key = key.replace(SWITCH_KEYS[0], SWITCH_KEYS[1])

    # safety checks
    if not message:
        raise ValueError("Empty message string.")

    if not message.isalpha():
        raise ValueError("The input message must contain only letters.")

    if not key.isalpha():
        raise ValueError("The input key must contain only letters.")

    # First build the matrix from the key
    matrix = build_matrix(key)

    # Separate in digrams
    digrams = ""

    # String must have a size greater than or equal to 2 and must be checked so that each digram doesn't have
    # the same letter
    if len(message) >= 2:
        for letter in message:
            # There's a catch here, we need to add an 'x' to the digram if the two letters of the digram were the same.
            # to do that it just verify the length (if it is odd then it knows the last letter of the digrams string
            # is the first letter of the digram) and check if the letters are the same, if they are, add the x
            if len(digrams) % 2 != 0 and letter == digrams[-1]:
                digrams += 'x'

            digrams += letter

    # If the string size is odd, append an 'x' in the end to form another digram, this verification will also
    # take care of strings with size of one character
    if len(digrams) % 2 != 0:
        digrams += "x"

    result = ""
    # Encrypt each digram
    for i in range(0, len(digrams), 2):
        # let's find the indexes of the letters in the matrix
        # for short the first element index will be called first_index,
        # likewise the second will be second_index
        first_index = second_index = None

        # iterate over the matrix
        for line in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):

                # after finding the indexes we break out of the loop
                if first_index and second_index:
                    break

                if matrix[line][col] == digrams[i]:
                    first_index = (line, col)
                    continue

                if matrix[line][col] == digrams[i + 1]:
                    second_index = (line, col)

        # If the letters appear on the same line of the matrix, replace them with the letters to their immediate right
        # respectively, wrapping around to the left side if the original letter was on the right side of the line
        if first_index[0] == second_index[0]:
            result += matrix[first_index[0]][(first_index[1] + 1) % len(matrix[0])] + \
                      matrix[second_index[0]][(second_index[1] + 1) % len(matrix[0])]
            continue

        # If the letters appear on the same column of the matrix, replace them with the letters immediately below
        # respectively, wrapping around to the top side of the column if the original letter was on the bottom
        # side of the column.

        if first_index[1] == second_index[1]:
            result += matrix[(first_index[0] + 1) % len(matrix)][first_index[1]] + \
                      matrix[(second_index[0] + 1) % len(matrix)][second_index[1]]
            continue

        # If the letters are not on the same row or column, replace them with the letters on the same row respectively
        # but at the other pair of corners of the rectangle defined by the original pair.

        result += matrix[first_index[0]][second_index[1]] + \
                  matrix[second_index[0]][first_index[1]]

    return result


def decrypt(message, key):
    matrix = build_matrix(key)
    return matrix


def build_matrix(key):
    """
    build as 5x5 matrix based on the input key
    :param key: string that will be used as a base for the matrix
    :return: 5x5 matrix with no repeated letters
    """

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
    matrix = [key[5 * i:5 * (i + 1)] for i in range(0, 5)]

    # We have a list of 5 elements and each element has size 5, it can be seen as a 5x5 matrix
    return matrix


def sanitize_string(txt):
    """
    metodo que limpa a string, transforma em minuscula, retira acentos e espaços
    :param txt: string a ser limpa
    :return: string limpa
    """
    txt = txt.lower().replace(" ", "")
    return remove_accents(txt)


def remove_accents(text):
    """
    metodo que remove os acentos da string
    :param text: string a ser retirada os acentos
    :return: string sem acentos
    """
    # breaks accents from letters
    text = unicodedata.normalize('NFKD', text)
    # converts to ASCII ignoring errors (that would be caused by the accents)
    text = text.encode('ASCII', 'ignore')
    # convert back to utf-8 and it is done.
    return text.decode('utf-8')


if __name__ == "__main__":
    print(encrypt("SPIZZA", "HELLO"))
    print(encrypt("PRIPYAT", "HELLO"))
    print(encrypt("GG", "HELLO"))
    print(encrypt("ÁBJ", "HELLO"))
    print(encrypt("Hide the gold in the tree stump", "playfair example"))

    # https://en.wikipedia.org/wiki/Playfair_cipher
