from string import ascii_uppercase, ascii_lowercase, ascii_letters

# def encrypt_vigenere(plaintext: str, keyword: str) -> str:
#     """
#     Encrypts plaintext using a Vigenere cipher.

#     >>> encrypt_vigenere("PYTHON", "A")
#     'PYTHON'
#     >>> encrypt_vigenere("python", "a")
#     'python'
#     >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
#     'LXFOPVEFRNHR'
#     """
#     ciphertext = ""
    
#     alfabet = string.ascii_lowercase
#     alfabet_upper = string.ascii_uppercase

#     dict = {}
#     for letter in keyword:
#         if letter.isupper():
#             dict[letter] = alfabet_upper.find(letter)
#         else:
#             dict[letter] = alfabet.find(letter)

#     lene = len(alfabet)
    
#     i = 0
#     N = len(keyword)

#     for letter in plaintext:
#         if i == N:
#             i = 0
#         if letter in dict:
#             if letter.isupper():
#                 sum = alfabet_upper.find(letter) + dict[keyword[i]]
#                 if (sum < lene):
#                     ciphertext += alfabet_upper[sum]
#                 else: 
#                     ciphertext += alfabet_upper[sum - lene]
#             else:
#                 sum = alfabet.find(letter) + dict[keyword[i]]
#                 if (sum < lene):
#                     ciphertext += alfabet[sum]
#                 else: 
#                     ciphertext += alfabet[sum - lene]
#         else:
#             ciphertext += letter

#         i += 1

#     return ciphertext


# def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
#     """
#     Decrypts a ciphertext using a Vigenere cipher.

#     >>> decrypt_vigenere("PYTHON", "A")
#     'PYTHON'
#     >>> decrypt_vigenere("python", "a")
#     'python'
#     >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
#     'ATTACKATDAWN'
#     """
#     plaintext = ""
    
#     alfabet = string.ascii_lowercase
#     alfabet_upper = string.ascii_uppercase

#     dict = {}
#     for letter in keyword:
#         if letter.isupper():
#             dict[letter] = alfabet_upper.find(letter)
#         else:
#             dict[letter] = alfabet.find(letter)

#     lene = len(alfabet)
    
#     N = len(keyword)
#     i = 0

#     for letter in ciphertext:
#         if i == N:
#             i = 0

#         print(i)

#         if letter.isupper():
#             sum = alfabet_upper.find(letter) - dict[keyword[i]]
#             if (sum < lene):
#                 plaintext += alfabet_upper[sum]
#             else: 
#                 plaintext += alfabet_upper[sum + lene]
#         else:
#             sum = alfabet.find(letter) + dict[keyword[i]]
#             if (sum < lene):
#                 plaintext += alfabet[sum]
#             else: 
#                 plaintext += alfabet[sum - lene]

#         i += 1

#     return plaintext


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    
    alfabet = ascii_lowercase * 2
    alfabet_upper = ascii_uppercase * 2

    shift = [ascii_lowercase.find(i) for i in keyword.lower()]

    i = 0
    N = len(shift)

    for letter in plaintext:
        if i == N:
            i = 0
        if letter in ascii_letters:
            if letter.isupper():
                ciphertext += alfabet_upper[ascii_uppercase.find(letter) + shift[i]]
            else:
                ciphertext += alfabet[ascii_lowercase.find(letter) + shift[i]]
        else:
            ciphertext += letter


        i += 1

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    
    alfabet = ascii_lowercase * 2
    alfabet_upper = ascii_uppercase * 2

    shift = [ascii_lowercase.find(i) for i in keyword.lower()]

    i = 0
    N = len(shift)

    for letter in ciphertext:
        if i == N:
            i = 0
        if letter in ascii_letters:
            if letter.isupper():
                plaintext += alfabet_upper[ascii_uppercase.find(letter) - shift[i]]
            else:
                plaintext += alfabet[ascii_lowercase.find(letter) - shift[i]]
        else:
            plaintext += letter


        i += 1

    return plaintext


print(decrypt_vigenere("tfvzzvwkeaqv lq aqvpzf", "lsci"))