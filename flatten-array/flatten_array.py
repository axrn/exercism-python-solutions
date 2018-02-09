def flatten(iterable: list) -> list:
    for i, x in enumerate(iterable):
        if isinstance(x, (list, tuple)):
            return flatten(iterable[:i] + list(x) + iterable[i + 1:])

    return [x for x in iterable if x is not None]
