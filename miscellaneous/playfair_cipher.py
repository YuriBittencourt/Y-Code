import string
import unicodedata
import sys


class PlayfairCipher:
    def __init__(self, key, alphabet_keys=string.ascii_lowercase, switch_keys=('j', 'i')):
        """
        :param key: string that will be used as a base for the matrix
        :param alphabet_keys: alphabet we will use (by default, we use our roman alphabet)
        :param switch_keys:  a tuple of the letter to be switched to another letter (by default, we switch 'j' to 'i')
        """
        # sanitize key and replace the removed letter
        self.key = sanitize_string(key)
        self.key = self.key.replace(switch_keys[0], switch_keys[1])

        if not self.key.isalpha():
            raise ValueError("The input key must contain only letters.")

        # Remove the letter chosen above from our alphabet
        self.alphabet_keys = alphabet_keys.replace(switch_keys[0], "")
        self.switch_keys = switch_keys

        # build matrix
        self.key = self.build_matrix()

    def encrypt(self, message):
        """
        encrypt a message with the playfair cipher using the key-matrix provided during the class instance construction
        :param message: string to be encrypted
        :return: encrypted string
        """
        # Sanitize our message
        message = sanitize_string(message)

        # Replacing the removed letter
        message = message.replace(self.switch_keys[0], self.switch_keys[1])

        # safety checks
        if not message:
            raise ValueError("Empty message string.")

        if not message.isalpha():
            raise ValueError("The input message must contain only letters.")

        # Separate in digrams
        digrams = ""

        # String must have a size greater than or equal to 2 and must be checked so that each digram doesn't have
        # the same letter
        if len(message) >= 2:
            for letter in message:
                # There's a catch here, we need to add an 'x' to the digram if the two letters of the digram were the
                # same. to do that it just verify the length (if it is odd then it knows the last letter of the
                # digrams string is the first letter of the digram) and check if the letters are the same,
                # if they are, add the x
                if len(digrams) % 2 != 0 and letter == digrams[-1]:
                    digrams += 'x'

                digrams += letter

        # If the string size is odd, append an 'x' in the end to form another digram, this verification will also
        # take care of strings with size of one character
        if len(digrams) % 2 != 0:
            digrams += "x"

        result = []
        # Encrypt each digram
        for i in range(0, len(digrams), 2):
            # let's find the indexes of the letters in the matrix
            # for short the first element index will be called first_index,
            # likewise the second will be second_index
            first_index = second_index = None

            # iterate over the matrix
            for line in range(0, len(self.key)):
                for col in range(0, len(self.key[0])):

                    # after finding the indexes we break out of the loop
                    if first_index and second_index:
                        break

                    if self.key[line][col] == digrams[i]:
                        first_index = (line, col)
                        continue

                    if self.key[line][col] == digrams[i + 1]:
                        second_index = (line, col)

            # If the letters appear on the same line of the matrix, replace them with the letters to their immediate
            # right respectively, wrapping around to the left side if the original letter was on the right side of
            # the line
            if first_index[0] == second_index[0]:
                result.append(self.key[first_index[0]][(first_index[1] + 1) % len(self.key[0])] + \
                              self.key[second_index[0]][(second_index[1] + 1) % len(self.key[0])])
                continue

            # If the letters appear on the same column of the matrix, replace them with the letters immediately below
            # respectively, wrapping around to the top side of the column if the original letter was on the bottom
            # side of the column.

            if first_index[1] == second_index[1]:
                result.append(self.key[(first_index[0] + 1) % len(self.key)][first_index[1]] + \
                              self.key[(second_index[0] + 1) % len(self.key)][second_index[1]])
                continue

            # If the letters are not on the same row or column, replace them with the letters on the same row
            # respectively but at the other pair of corners of the rectangle defined by the original pair.

            result.append(self.key[first_index[0]][second_index[1]] + \
                          self.key[second_index[0]][first_index[1]])

        return " ".join(result)

    def decrypt(self, message):
        """
        decrypt a message back to plaintext
        :param message: encrypted string
        :return: decrypted string
        """

        # the decrypt is basically the encrypt with the rules reversed, that is to say, if the two letters are in the
        # same line, replace them with their immediate left (in encrypt it was immediate right), that applies to the
        # other rules as well, following this logic it is possible to decrypt the message by encrypting the message with
        # the key matrix with its columns and lines reversed and then removing 'x' characters between same letters

        # Sanitize our message
        message = sanitize_string(message)

        # safety checks
        if not message:
            raise ValueError("Empty message string.")

        if not message.isalpha():
            raise ValueError("The input message must contain only letters.")

        if len(message) % 2 != 0:
            raise ValueError("Message length not even, may have characters missing.")

        if self.switch_keys[0] in message:
            raise ValueError("Invalid message, it contains the removed letter, which is ", self.switch_keys[0])

        # reverse lines and columns of the key matrix
        self.reverse_key()
        # decrypt
        result = self.encrypt(message)
        # de-reverse lines and columns of the key matrix
        self.reverse_key()

        # please take note that the result string may have some 'x's out of place, it's not trivial to remove them
        # my initial idea was: check the immediate neighboring letters and if they were the same simply remove 'x' but
        # what would happens in cases like the word 'exercise'? the result would be 'ex er ci se' and removing that 'x'
        # would mess the word, so it's better to let them there.

        return result

    def reverse_key(self):
        """
        method that reverses the columns and lines of the key matrix
        :return: a 5x5 matrix with the lines and columns reversed
        """
        # reverse columns
        self.key.reverse()

        # reverse lines
        for i in range(0, len(self.key)):
            self.key[i] = self.key[i][::-1]

    def build_matrix(self):
        """
        build as 5x5 matrix based on the input key (given in the constructor of the class)
        :return: 5x5 matrix with no repeated letters
        """

        # Let's remove duplicates
        remaining_keys = self.alphabet_keys
        for letter in self.key:
            if letter in remaining_keys:
                # If it is in the alphabet_keys, we should remove it from the alphabet
                remaining_keys = remaining_keys.replace(letter, "", 1)
            else:
                # If it is not, that is because we already removed earlier and should
                # remove the duplicate from our key

                # Find the index of the second occurrence, then slice and concatenate it.
                duplicated_index = self.key.index(letter, self.key.index(letter) + 1)
                self.key = self.key[0:duplicated_index] + self.key[duplicated_index + 1:]

        self.key = self.key + remaining_keys
        # Now our key has all the 25 letters and each letter occurring just once.
        # Let's break our key into a 5x5 matrix
        # First let's break our key into 5 strings of size 5
        matrix = [self.key[5 * i:5 * (i + 1)] for i in range(0, 5)]

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
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print("execute the script with the following arguments: " +
              "\n \t OPTION KEY MESSAGE " +
              "\n \t where:" +
              "\n \t \t OPTION can be -e to encrypt or -d to decrypt" +
              "\n \t \t KEY is the encryption/decryption key, and must be a not empty string with only roman letters" +
              "\n \t \t MESSAGE is the message to be encrypted/decrypted and must be a not empty string with only "
              "roman letters")
        exit(0)
    if len(sys.argv) != 4:
        print("Invalid number of parameters")
        exit(0)

    cipher = PlayfairCipher(sys.argv[2])
    if sys.argv[1] == '-e':
        print(cipher.encrypt(sys.argv[3]))
        exit(0)

    if sys.argv[1] == '-d':
        print(cipher.decrypt(sys.argv[3]))
        exit(0)

    print("invalid option '{}'".format(sys.argv[1]))
