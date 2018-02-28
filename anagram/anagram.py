def detect_anagrams(sample: str, words: list) -> list:
    low_sample = sample.lower()
    return [x for x in words if low_sample != x.lower() and sorted(low_sample) == sorted(x.lower())]
