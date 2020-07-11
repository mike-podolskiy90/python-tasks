def rotate_image(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(len(arr)):
        for j in range(0, n // 2):
            arr[i][j], arr[i][n - 1 - j] = arr[i][n - 1 - j], arr[i][j]

    return arr


arr_to_rotate = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotate_image(arr_to_rotate))
