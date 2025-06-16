import string

characters = string.ascii_letters 

def letters_to_num(s):
    d = {c: i for i, c in enumerate(characters)}
    n = 0
    for c in s:
        n = n * 52 + d[c]
    return n

def split_three_parts(s):
    parts = s.split('-')
    parts += [''] * (3 - len(parts))
    return tuple(parts[:3])

def check_correct(s):
    parts = split_three_parts(s)

    if letters_to_num(parts[2]) < 1:
        return False
    
    if (
        any(char not in characters for char in parts[0]) or
        any(char not in characters for char in parts[1])
    ):
        return False
    
    return True