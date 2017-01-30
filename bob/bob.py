def hey(what):
    if what.isupper():
        return 'Whoa, chill out!'
    if what.rstrip().endswith('?'):
        return 'Sure.'
    if what.isspace() or what == '':
        return 'Fine. Be that way!'
    return 'Whatever.'