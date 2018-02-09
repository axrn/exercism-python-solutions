class Luhn(object):
    def __init__(self, card_num: str) -> None:
        self._card_num = card_num.replace(' ', '')

    def is_valid(self) -> bool:
        if len(self._card_num) <= 1:
            return False

        if not self._card_num.isdigit():
            return False

        all_nums = [int(x) for x in self._card_num]
        a, b = (0, 1) if len(all_nums) % 2 == 0 else (1, 0)
        doubled_nums = sum(x * 2 if x * 2 < 9 else x * 2 - 9 for x in all_nums[a::2])
        other_nums = sum(x for x in all_nums[b::2])

        return (doubled_nums + other_nums) % 10 == 0
