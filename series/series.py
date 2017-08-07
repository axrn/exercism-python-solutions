def slices(s: str, n: int):
    return [list(map(int, s[i: i+n])) for i, _ in enumerate(s) if i <= len(s) - n]
