def check(a, b):
    # Check to make sure two strings are different by 1 in length
    if abs(len(a) - len(b)) > 1:
        return False

    if len(a) < len(b):
        s1 = a
        s2 = b
    else:
        s1 = b
        s2 = a

    index1 = 0
    index2 = 0
    found_difference = False
    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if found_difference:
                return False
            found_difference = True

            if len(s1) == len(s2):
                index1 += 1
        else:
            index1 += 1
        index2 += 1
    return True
