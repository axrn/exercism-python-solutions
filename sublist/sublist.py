SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)


def check_lists(first_list, second_list):

    first = str(first_list)[1:-1]
    second = str(second_list)[1:-1]

    if first == second:
        return EQUAL

    if first in second:
        return SUBLIST

    if second in first:
        return SUPERLIST

    return UNEQUAL
