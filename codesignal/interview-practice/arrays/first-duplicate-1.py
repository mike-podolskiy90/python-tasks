arr = [2, 1, 3, 5, 3, 2]


def first_duplicate(a):
    count = [0] * (len(a) + 1)
    for x in a:
        count[x] += 1
        if count[x] > 1:
            return x

    return -1


print(first_duplicate(arr))
