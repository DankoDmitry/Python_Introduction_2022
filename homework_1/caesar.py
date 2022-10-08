from string import ascii_uppercase, ascii_lowercase



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

    alfabet = ascii_lowercase * 2 + ascii_uppercase * 2

    dict = {}
    for letter in alfabet:
        if letter not in dict:
            dict[letter] = alfabet[alfabet.find(letter) + shift]

    ciphertext = ''

    for i in plaintext:
        if i in dict.keys():
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

    alfabet = ascii_lowercase * 2 + ascii_uppercase * 2

    alfabet = alfabet[::-1]
    

    dict = {}
    for letter in alfabet:
        if letter not in dict:
            dict[letter] = alfabet[alfabet.find(letter) + shift]

    plaintext = ''

    for i in ciphertext:
        if i in dict.keys():
            plaintext += dict[i]
        else: 
            plaintext += i
    
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

