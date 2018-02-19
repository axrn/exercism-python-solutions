from random import choice
from string import ascii_uppercase, digits


class Robot(object):
    _used_names = set()

    def __init__(self):
        self._name = Robot._generate_name()

    def reset(self):
        self.__init__()

    @staticmethod
    def _generate_name() -> str:
        def random_name():
            return ''.join([choice(ascii_uppercase) for _ in range(2)] + [choice(digits) for _ in range(3)])

        possible_name = random_name()
        while possible_name in Robot._used_names:
            possible_name = random_name()
        Robot._used_names.add(possible_name)

        return possible_name

    @property
    def name(self):
        return self._name
