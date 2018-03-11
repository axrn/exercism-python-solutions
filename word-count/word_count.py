from collections import Counter
import re


def word_count(phrase):
    return Counter(filter(None, re.split("[\W_]", phrase.lower())))
