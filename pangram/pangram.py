def is_pangram(sentence):
    alphabet = map(chr, range(ord('a'), ord('z')+1))
    sentence = sorted(set(x for x in sentence.lower() if x.isalpha()))
    return sentence == alphabet