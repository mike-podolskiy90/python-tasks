s = input()
arr = s.split()

max_str_pos = []
max_length = len(arr[0])

for i in range(len(arr)):
    if len(arr[i]) > max_length:
        max_length = len(arr[i])
        max_str_pos = [i]
    elif len(arr[i]) == max_length:
        max_str_pos.append(i)

for i in max_str_pos:
    print(i + 1)
