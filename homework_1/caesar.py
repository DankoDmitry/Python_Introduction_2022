from random import randint
import typing as tp
import string

from pyparsing import sgl_quoted_string

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    
    alfabet = string.ascii_letters + '0123456789'

    dict = {}
    for i in range(62):
        if i < 62 - shift:
            dict[alfabet[i]] = alfabet[i + shift]
        else:
            dict[alfabet[i]] = alfabet[i + shift - 62]

    ciphertext = ''

    for i in plaintext:
        if (i != ' ' and i != '.' and i != ',' and i != "'" and i != "-"):
            ciphertext += dict[i]
        else: 
            ciphertext += i

    # PUT YOUR CODE HERE
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""

    alfabet = string.ascii_letters + '0123456789'

    dict = {}
    for i in range(62):
        if i > shift - 1:
            dict[alfabet[i]] = alfabet[i - shift]
        else:
            dict[alfabet[i]] = alfabet[i - shift + 62]

    plaintext = ''

    for i in ciphertext:
        if (i != ' ' and i != '.' and i != ',' and i != "'" and i != "-"):
            plaintext += dict[i]
        else: 
            plaintext += i

    # PUT YOUR CODE HERE
    return plaintext


def caesar_breaker_brute_force(ciphertext: str) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0

    for i in range(63):
        text = decrypt_caesar(ciphertext, i)
        if 'the' in text or 'The' in text:
            best_shift = i

    # PUT YOUR CODE HERE
    return best_shift


# print(string.ascii_letters)
# print(type(string.ascii_letters))
# print(string.ascii_letters[51])
# print(len(string.ascii_letters))

text = "I've got a family. It is small. We are a family of four. I've got a father, a mother and a brother. I haven't got a sister. My father is.an engineer. He works in a plant. My mother is a teacher. She works at school. My brother is little. He doesn't go to school. He goes to a kindergarten. He is four.I like to play. I have got many toys. I have got a teddy-bear, dolls, a ball, a toy monkey and a doll's house. I like the doll's house very much. It is big. It is pink and nice."

shift = randint(0, 62)

encrypt = encrypt_caesar(text, shift)

print(shift, " => ", caesar_breaker_brute_force(encrypt))