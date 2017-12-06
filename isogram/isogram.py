def is_isogram(word: str) -> bool:
    prepared_word = [x for x in word.lower() if x.isalpha()]
    return len(prepared_word) == len(set(prepared_word))