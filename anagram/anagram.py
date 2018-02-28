def detect_anagrams(word: str, possible_anagrams: list) -> list:
    word_low = word.lower()

    def is_anagram(candidate: str) -> bool:
        return word_low != candidate and sorted(word_low) == sorted(candidate)

    return [x for x in possible_anagrams if is_anagram(x.lower())]
