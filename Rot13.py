from string import ascii_lowercase, ascii_uppercase

alphabet = ascii_lowercase + ascii_uppercase


def shift_letter(letter: str, shift=13):
    def sign(x):
        return 1 if x >= 0 else -1

    if letter not in alphabet:
        return letter
    new_ord = ord(letter) + shift
    if letter in ascii_uppercase:
        return chr(ord(letter) + shift * sign(90 - new_ord))
    return chr(ord(letter) + shift * sign(122 - new_ord))


def rot13(message: str) -> str:
    return ''.join([shift_letter(c, shift=13) for c in message])