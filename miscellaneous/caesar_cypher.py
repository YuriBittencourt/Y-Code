class caesar_cypher:

    def __init__(self):
        self.__alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__chr_num_dict = dict(zip(self.__alphabet, range(0, len(self.__alphabet))))
        self.__num_chr_dict = dict(zip(range(0, len(self.__alphabet)), self.__alphabet))

    def encrypt(self, sentence, offset=3):
        sentence = sentence.upper()
        new_str = ''
        for char in sentence:
            if char in self.__chr_num_dict:
                index = (self.__chr_num_dict[char.upper()] + offset) % len(self.__alphabet)
                new_str += self.__num_chr_dict[index]
            else:
                new_str += char
        return new_str

    def decrypt(self, sentence, offset=3):
        sentence = sentence.upper()
        new_str = ''
        for char in sentence:
            if char in self.__chr_num_dict:
                index = (self.__chr_num_dict[char.upper()] - offset) % len(self.__alphabet)
                new_str += self.__num_chr_dict[index]
            else:
                new_str += char
        return new_str
