SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)


def check_lists(first_list, second_list):

    def is_sub(l1: list, l2: list) -> bool:
        if len(l2) < len(l1):
            return False
        for start in range(0, len(l2) - len(l1) + 1):
            if l2[start] != l1[0]:
                continue
            if l2[start: start + len(l1)] == l1:
                return True
        return False

    if first_list == second_list:
        return EQUAL

    if first_list == [] or is_sub(first_list, second_list):
        return SUBLIST

    if second_list == [] or is_sub(second_list, first_list):
        return SUPERLIST

    return UNEQUAL
