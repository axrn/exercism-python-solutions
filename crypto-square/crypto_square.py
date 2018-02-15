def encode(plain_text: str) -> str:
    normalized = ''.join(x for x in plain_text.lower() if x.isalnum())
    if len(normalized) <= 1:
        return normalized

    r = round(len(normalized) ** 0.5)
    c = r if r * r >= len(normalized) else r + 1

    filled = normalized + ' ' * (r * c - len(normalized))

    return ' '.join(filled[start::c] for start in range(c))
