s = input()
new_str = ''

for i in s:
    if i not in new_str and i != ' ':
        new_str += i

print(new_str)
