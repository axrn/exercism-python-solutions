def encode(s):
    tmp = [s[0]]
    res = ''

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            tmp[len(tmp)-1] += s[i]
        else:
            tmp.append(s[i])

    for j in tmp:
        if len(j) > 1:
            res += str(len(j)) + j[0]
        else:
            res += j

    return res



def decode(s):
    result = ''
    tmp_i = ''
    for i in range(len(s)):
        if s[i].isdigit():
            tmp_i += s[i]
        else:
            if tmp_i != '':
                result += int(tmp_i) * s[i]
            else:
                result += s[i]
            tmp_i = ''

    return result