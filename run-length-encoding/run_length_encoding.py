def encode(string):
    tmp = [string[0]]
    res = ''

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            tmp[len(tmp) - 1] += string[i]
        else:
            tmp.append(string[i])

    for j in tmp:
        if len(j) > 1:
            res += str(len(j)) + j[0]
        else:
            res += j

    return res


def decode(string):
    result = ''
    tmp_i = ''
    for i in range(len(string)):
        if string[i].isdigit():
            tmp_i += string[i]
        else:
            if tmp_i != '':
                result += int(tmp_i) * string[i]
            else:
                result += string[i]
            tmp_i = ''

    return result
