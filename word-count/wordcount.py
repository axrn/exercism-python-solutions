def word_count(phrase):
    import re
    from collections import defaultdict

    dd = defaultdict(int)
    for word in filter(None, re.split("[\W_]", phrase)):
        dd[word] += 1

    return dict(dd)