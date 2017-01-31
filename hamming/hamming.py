def distance(dna1='', dna2=''):
    return len([x + y for x, y in zip(dna1, dna2) if x != y])