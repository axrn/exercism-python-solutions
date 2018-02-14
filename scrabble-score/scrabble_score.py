def score(word: str) -> int:
    SCORE = {'AEIOULNRST': 1,
             'DG': 2,
             'BCMP': 3,
             'FHVWY': 4,
             'K': 5,
             'JX': 8,
             'QZ': 10}
    LETTER_SCORE = {x: i for s, i in SCORE.items() for x in s}
    return sum(LETTER_SCORE[x] for x in word.upper())
