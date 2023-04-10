"""
Created on 1/8/23

@author: Adeildo Vieira Silva Neto.
"""


def isVowel(ch):
    """
    Returns True if ch is a vowel and False if it is not a vowel.
    """
    if ch.lower() == "a" or ch.lower() == "e" or ch.lower() == "i" or \
            ch.lower() \
            == "o" or ch.lower() == "u" or ch.lower() == "y":
        return True


def isFrstVowel(ch):
    """
    Returns True if first character is a vowel and False if it is not.
    """
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        return True


def encrypt(w):
    """
    Takes a string and converts it to PigLatin using the helper functions above.
    """
    lst = list(w)
    if isFrstVowel(lst[0].lower()) == True:
        return w + "-way"
    elif lst[0].lower() == "q":
        for i in lst:
            if i.lower() == "a" or i.lower() == "e" or i.lower() == "i" or \
                    i.lower() == "o":
                return w[lst.index(i):] + "-" + w[:lst.index(i)] + "ay"
    elif lst[0].lower() == "y":
        return w[1:] + "-" + w[0] + "ay"
    else:
        for i in lst:
            if isVowel(i) == True:
                index = w.index(i)
                return w[index:] + "-" + w[:index] + "ay"
        return w + "-way"


def decrypt(w):
    """
    Function that takes a PigLatin string, converting it back to the original
    using while loop with if statements, slicing, and concatenation methods.
    """
    lst = list(w)
    i = 0
    while i < len(lst):
        if lst[i] == "-":
            if w[i + 1:] == "way":
                return w[:i]
            else:
                return w[i + 1:-2] + w[:i]
        i += 1


if __name__ == '__main__':
    pass
