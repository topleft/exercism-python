
import re

def is_pangram(input):
    unique = []
    input = re.sub('[\W\d\s_]', '', input).lower()
    for char in input:
        if char not in unique:
            unique.append(char)

    if len(unique) is 26:
        return True
    else:
        return False
