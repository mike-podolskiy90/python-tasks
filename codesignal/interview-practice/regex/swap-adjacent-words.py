import re


def swap_adjacent_words(s):
    return re.sub("([A-Za-z]+)([ ]+)([A-Za-z]+)", "\\3\\2\\1", s)


print(swap_adjacent_words("CodeFight On"))
print(swap_adjacent_words("How are you today guys"))
print(swap_adjacent_words("IAmALongStringWithNoWhiteSpaceCharacters"))
print(swap_adjacent_words("A b C D e F g h I j"))
print(swap_adjacent_words(""))
