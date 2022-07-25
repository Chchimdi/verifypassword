
def check_pwd(password):
    symbols = '~`!@#$%^&*()_+-='
    len0 = False
    length = False
    lower = False
    upper = False
    digit = False
    sym = False

    if len(password) == 0:
        return len0

    if len(password) not in range(8, 21):
        return length

    if not any(char.islower() for char in password):
        return lower

    if not any(char.isupper() for char in password):
        return upper

    if not any(char.isdigit() for char in password):
        return digit

    for char in password:
        if char not in symbols:
            return sym

    return True
