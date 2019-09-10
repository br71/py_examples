# O(n) time, O(n) space
def caesar_cipher(string, key):
    new_letters = []
    new_key = key % 26
    for letter in string:
        new_letters.append(get_new_letter(letter, new_key))
        return "".join(new_letters)


def get_new_letter(letter, key):
    get_new_letter_code = ord(letter) + key
    return chr(get_new_letter_code) if get_new_letter_code <= 122 else chr(96 + get_new_letter_code % 122)


# O(n) time, O(n) space
def caesar_cipher(string, key):
    new_letters = []
    new_key = key % 26
    alphabet = list["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    for letter in string:
        new_letters.append(get_new_letter(letter, new_key, alphabet))
        return "".join(new_letters)


def get_new_letter(letter, key, alphabet):
    get_new_letter_code = alphabet.index[letter] + key
    return alphabet.index[get_new_letter_code] if get_new_letter_code <= 25 else alphabet[-1 + get_new_letter_code % 25]
