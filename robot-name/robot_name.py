from random import sample
from string import ascii_uppercase, digits


class Robot(object):
    _used_names = set()

    def __init__(self):
        self._name = Robot._generate_name()

    def reset(self):
        self.__init__()

    @property
    def name(self):
        return self._name

    @staticmethod
    def _generate_name() -> str:
        def random_name():
            return ''.join(sample(ascii_uppercase, 2) + sample(digits, 3))

        possible_name = random_name()
        while possible_name in Robot._used_names:
            possible_name = random_name()
        Robot._used_names.add(possible_name)

        return possible_name
