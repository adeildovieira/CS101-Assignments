"""
Created on 1/8/23

@author: Adeildo Vieira Silva Neto (av259).
"""

import os.path

shift = 3
lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = lower_alph.upper()
shifted_lower = lower_alph[3:] + lower_alph[:3]
shifted_upper = upper_alph[3:] + upper_alph[:3]

def setShift(integer):
    """
    Function that takes in an integer containing 3 global variables that makes
    the caesar cipher shift for other functions that are specified.
    """
    global shift, shifted_lower, shifted_upper
    shift = integer
    shifted_lower = lower_alph[integer:] + lower_alph[:integer]
    shifted_upper = upper_alph[integer:] + upper_alph[:integer]


def encrypt(w):
    """
    This is a function that takes a string and uses the given shift returning
    the string with the given shift statement.
    """
    encryptednewstring = ""
    for ch in w:
        if ch in lower_alph:
            encryptednewstring += shifted_lower[lower_alph.index(ch)]
        elif ch in upper_alph:
            encryptednewstring += shifted_upper[upper_alph.index(ch)]
        else:
            encryptednewstring += ch
    return encryptednewstring

def findShift(st):
    """
    Function that finds the shift for string that has been encrypted by caesar
    cipher shift.
    """
    file = os.path.join("data", "lowerwords.txt")
    f = open(file)
    wordsClean = [w.strip() for w in f.read().split()]
    maxCount = 0
    shift = 0
    for i in range(26):
        count = 0
        setShift(i)
        lst = [encrypt(w) for w in st.split()]
        for w in lst:
            if w.lower() in wordsClean:
                count +=1
        if count > maxCount:
            maxCount = count
            shift = 26 - i
    return shift


if __name__ == '__main__':
    pass
