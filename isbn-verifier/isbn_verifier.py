def verify(isbn: str) -> bool:
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False

    try:
        all_digits = [int(x) for x in isbn[:9]] + [10 if isbn[9] == 'X' else int(isbn[9])]
    except:
        return False

    return 0 == sum(x * (10 - i) for i, x in enumerate(all_digits)) % 11
