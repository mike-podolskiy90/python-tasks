arr = [2, 1, 3, 5, 3, 2]


def first_duplicate(a):
    for i in range(len(a)):
        if a[i] < 0:
            return abs(a[i])
        else:
            a[a[i]] *= -1

    return -1


print(first_duplicate(arr))
