def on_square(n: int) -> int:
    if not 1 <= n <= 64:
        raise ValueError('1..64')
    return 2 ** (n - 1)


def total_after(n: int) -> int:
    if not 1 <= n <= 64:
        raise ValueError('1..64')
    return 2 ** n - 1
