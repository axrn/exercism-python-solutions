from string import ascii_lowercase
from collections import Counter
from secrets import choice


class Cipher(object):
    """Simple substitution cipher but not for all this tests/exercise"""  # TODO: rewrite

    def __init__(self, key=None):
        self.key = key

        if not self.key:
            self.key = ''.join(choice(ascii_lowercase) for x in range(100))

        key_alphabet = self._make_key_alphabet(self.key)
        self._ENC_TABLE = str.maketrans(ascii_lowercase, key_alphabet)
        self._DEC_TABLE = str.maketrans(key_alphabet, ascii_lowercase)

    def _make_key_alphabet(self, key: str) -> str:
        c = Counter(key)
        rev_key = key[::-1]
        for char, amount in c.items():
            rev_key = rev_key.replace(char, '', amount - 1)

        prep_key = rev_key[::-1]
        prep_alphabet = ascii_lowercase
        for c in prep_key:
            prep_alphabet = prep_alphabet.replace(c, '')

        return prep_key + prep_alphabet

    def _prep(self, s: str) -> str:
        return ''.join(x for x in s.lower() if x.isalpha())

    def encode(self, text: str) -> str:
        return self._prep(text).translate(self._ENC_TABLE)

    def decode(self, text: str) -> str:
        return self._prep(text).translate(self._DEC_TABLE)


class Caesar(object):
    def __init__(self) -> None:
        shifted = ascii_lowercase[3:] + ascii_lowercase[:3]
        self._ENC_TABLE = str.maketrans(ascii_lowercase, shifted)
        self._DEC_TABLE = str.maketrans(shifted, ascii_lowercase)

    def _prep(self, text: str) -> str:
        return ''.join(x for x in text.lower() if x.isalpha())

    def encode(self, text: str) -> str:
        return self._prep(text).translate(self._ENC_TABLE)

    def decode(self, text: str) -> str:
        return self._prep(text).translate(self._DEC_TABLE)
