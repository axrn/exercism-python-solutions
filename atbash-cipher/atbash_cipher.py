import string


def encode(plain_text: str) -> str:
    prep = ''.join(x for x in plain_text.lower() if x.isalnum())
    table = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])
    result = prep.translate(table)
    return ' '.join(result[x: x + 5] for x in range(0, len(result), 5))


def decode(ciphered_text: str) -> str:
    prep = ''.join(x for x in ciphered_text.lower() if x.isalnum())
    table = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])
    return prep.translate(table)
