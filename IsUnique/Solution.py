# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


def check(s):
    letter = [0] * 128
    char = list(s)
    for c in char:
        letter[ord(c)] += 1
        if (letter[ord(c)] > 1):
            return False
    return True
