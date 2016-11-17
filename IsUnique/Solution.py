# Quyen Truong
# 11/16/2016

# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


def check(s):
    letter = [0] * 128
    char = list(s)
    # Put each char from string s in list ASC II
    for c in char:
        letter[ord(c)] += 1
        # Check if found more one char
        if letter[ord(c)] > 1:
            return False
    return True
