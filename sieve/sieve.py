from typing import Iterable


def lazy_sieve(limit: int) -> Iterable[int]:
    denied = set()
    for i in range(2, limit + 1):
        if i not in denied:
            denied.update(x for x in range(i, limit + 1, i))
            yield i


def sieve(limit: int) -> list:
    return [x for x in lazy_sieve(limit)]
