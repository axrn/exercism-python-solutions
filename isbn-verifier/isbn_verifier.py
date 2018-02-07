import string


def verify(isbn: str) -> bool:
    if not isbn:
        return False

    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False

    if not all(x in string.digits for x in isbn[:9]):
        return False

    if isbn[9] not in string.digits + 'X':
        return False

    all_digits = [int(x) for x in isbn[:9]] + [10 if isbn[9] == 'X' else int(isbn[9])]

    must_be_zero = sum(x * (10 - i) for i, x in enumerate(all_digits)) % 11

    return must_be_zero == 0
