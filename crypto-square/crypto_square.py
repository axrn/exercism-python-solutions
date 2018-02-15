def encode(plain_text: str) -> str:

    normalized = ''.join(x for x in plain_text.lower() if x.isalnum())
    if len(normalized) <= 1:
        return normalized

    r = round(len(normalized) ** 0.5)
    c = r if r * r >= len(normalized) else r + 1

    filled = normalized + ' ' * (r * c - len(normalized))
    chunks = [filled[x: x + c] for x in range(0, r * c, c)]

    res = []
    for i in range(c):
        res.append(''.join(x[i] for x in chunks))

    return ' '.join(res)
