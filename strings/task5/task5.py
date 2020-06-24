s = input()

while (pos := s.find(" ")) != -1:
    s = s[0:pos] + s[pos + 1:]

print(s)

is_palindrome = True
for i in range(len(s) // 2):
    if s[i] != s[-1-i]:
        is_palindrome = False
        break

print(is_palindrome)
