def score(word: str) -> int:
    score = ['', 'AEIOULNRST', 'DG', 'BCMP', 'FHVWY', 'K', '', '', 'JX', '', 'QZ']
    res = []
    for c in word.upper():
        for i, e in enumerate(score):
            if c in e:
                res.append(i)
                continue
    return sum(res)
