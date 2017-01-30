def detect_anagrams(s, w_list):
    s_low = s.lower()
    s_letters = sorted(s_low)

    def is_anogram(word):
        word = word.lower()
        return s_low != word and s_letters == sorted(word)

    return filter(is_anogram, w_list)