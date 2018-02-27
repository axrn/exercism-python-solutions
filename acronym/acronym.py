def abbreviate(words: str) -> str:
    return ''.join(x for x in words.title() if x.isupper())
