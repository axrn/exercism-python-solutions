def distance(dna_1: str, dna_2: str) -> int:
    if len(dna_1) != len(dna_2):
        raise ValueError("one strand longer")

    return sum(1 for x, y in zip(dna_1, dna_2) if x != y)
