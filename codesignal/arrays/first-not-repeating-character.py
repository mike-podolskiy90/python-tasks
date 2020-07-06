str = "abacabad"


def first_not_repeating_character(s):
    d = {}
    for c in s:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1

    for c in d.keys():
        if d[c] == 1:
            return c

    return "_"


print(first_not_repeating_character(str))
