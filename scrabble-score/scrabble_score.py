def score(word: str) -> int:
    SCORE = {'AEIOULNRST': 1,
             'DG': 2,
             'BCMP': 3,
             'FHVWY': 4,
             'K': 5,
             'JX': 8,
             'QZ': 10}
    res = 0
    for char in word.upper():
        for s in SCORE.keys():
            if char in s:
                res += SCORE[s]
                continue
    return res
