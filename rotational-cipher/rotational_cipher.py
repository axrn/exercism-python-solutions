import string


def rotate(text: str, key: int) -> str:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    rot_lower = ''.join(lowercase[(lowercase.index(x) + key) % 26] for x in lowercase)
    rot_upper = ''.join(uppercase[(uppercase.index(x) + key) % 26] for x in uppercase)

    trans_table = ''.maketrans(lowercase + uppercase, rot_lower + rot_upper)
    return text.translate(trans_table)
