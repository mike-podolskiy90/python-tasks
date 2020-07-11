def rotate_image(arr):
    return rotate_image_internal(arr, 0, len(arr), len(arr))


def rotate_image_internal(arr, i, length, sub_length):
    n = sub_length - 1

    for j in range(i, i + n):
        temp_a = arr[i][j]
        temp_b = arr[j][length - 1 - i]
        temp_c = arr[length - 1 - i][length - 1 - j]
        temp_d = arr[length - 1 - j][i]

        arr[i][j] = temp_d
        arr[j][length - 1 - i] = temp_a
        arr[length - 1 - i][length - 1 - j] = temp_b
        arr[length - 1 - j][i] = temp_c

    if sub_length - 2 > 1:
        rotate_image_internal(arr, i + 1, length, sub_length - 2)

    return arr


arr_to_rotate = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotate_image(arr_to_rotate))
