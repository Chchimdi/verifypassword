
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

    return True
