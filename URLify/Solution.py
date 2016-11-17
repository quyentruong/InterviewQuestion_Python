# Quyen Truong
# 11/16/2016

# Write a method to replace all spaces in a string with '%20

def replace_space(s):
    char = list(s.strip())
    space = 0
    for c in char:
        if c == ' ':
            space += 1

    char_new = [''] * (len(s) + space * 2)
    index = 0
    for c in char:
        if c == ' ':
            char_new[index] = '%'
            char_new[index + 1] = '2'
            char_new[index + 2] = '0'
            index += 3
        else:
            char_new[index] = c
            index += 1
    return ''.join(char_new)
