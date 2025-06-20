import string

characters = string.ascii_letters 

server_response_codes = {
    200: 'success',
    400: 'missing element',
    401: 'wrong account',
    402: 'incorrect format',
    403: 'cannot send money to yourself',
    404: 'not enough money for this transaction',
}

def letters_to_num(s: str):
    d = {c: i for i, c in enumerate(characters)}
    n = 0
    for c in s:
        n = n * 52 + d[c]
    return n

def split_three_parts(s: str):
    parts = s.split('-')
    parts += [''] * (3 - len(parts))
    return tuple(parts[:3])

def check_correct(s: str):
    parts = split_three_parts(s)

    if letters_to_num(parts[2]) < 1:
        return False
    
    if (
        any(char not in characters for char in parts[0]) or
        any(char not in characters for char in parts[1])
    ):
        return False
    
    return True

def get_id(s: str):
    parts = split_three_parts(s)

    return letters_to_num(parts[2])