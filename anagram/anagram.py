def detect_anagrams(word: str, possible_anagrams: list) -> list:
    word_low = word.lower()

    def is_anagram(candidate: str):
        candidate_low = candidate.lower()
        return word_low != candidate_low and sorted(word_low) == sorted(candidate_low)

    return list(filter(is_anagram, possible_anagrams))
