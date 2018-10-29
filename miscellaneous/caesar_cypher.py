__alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
__chr_num_dict = dict(zip(__alphabet, range(0, len(__alphabet))))
__num_chr_dict = dict(zip(range(0, len(__alphabet)), __alphabet))


def encrypt(sentence, offset=3):
    sentence = sentence.upper()
    new_str = ''
    for char in sentence:
        if char in __chr_num_dict:
            index = (__chr_num_dict[char.upper()] + offset) % len(__alphabet)
            new_str += __num_chr_dict[index]
        else:
            new_str += char
    return new_str


def decrypt(sentence, offset=3):
    sentence = sentence.upper()
    new_str = ''
    for char in sentence:
        if char in __chr_num_dict:
            index = (__chr_num_dict[char.upper()] - offset) % len(__alphabet)
            new_str += __num_chr_dict[index]
        else:
            new_str += char
    return new_str
