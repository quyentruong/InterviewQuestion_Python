def check(a, b):
    # Check if two strings have same length
    if len(a) != len(b):
        return False

    # Create list ASCII
    letter = [0] * 128

    # Store each char of string a in the list ASCII
    char_a = list(a)
    for c in char_a:
        letter[ord(c)] += 1

    # Check if each char of string b in the list ASCII
    # if not false
    char_b = list(b)
    for c in char_b:
        letter[ord(c)] -= 1
        if letter[ord(c)] < 0:
            return False
    return True
