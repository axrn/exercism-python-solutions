def to_rna(dna: str) -> str:
    TRANSLATION_TABLE = str.maketrans("GCTA", "CGAU")
    if not all(ord(x) in TRANSLATION_TABLE for x in dna):
        raise ValueError

    return dna.translate(TRANSLATION_TABLE)
