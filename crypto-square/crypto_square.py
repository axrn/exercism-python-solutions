def encode(text: str) -> str:
    normalized = ''.join(x for x in text.lower() if x.isalnum())
    if len(normalized) <= 1:
        return normalized

    r = round(len(normalized) ** 0.5)
    c = round(len(normalized) / r)

    filled = normalized + (r * c - len(normalized)) * ' '

    return ' '.join(filled[start::c] for start in range(c))
