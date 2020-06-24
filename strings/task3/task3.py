s = input("String: ")
subst_to_replace = input("Substring to replace: ")
new_substr = input("New substring: ")

found = False
n = 0
for i in range(len(s)):
    n = s.find(subst_to_replace, n)
    if n == -1:
        break
    else:
        found = True
        s = s[:n] + new_substr + s[n + len(subst_to_replace):]

if found:
    print(s)
else:
    print("Substring is absent: ", subst_to_replace)
