import re


def repetition_encryption(letter):
    pattern = "(?i)([a-zA-Z]+)[-0-9,.')(!?/% ]+\\1(?:[-0-9,.')(!?/% ]+|$)"
    regex = re.compile(pattern)
    return len(re.findall(regex, letter))


assert(repetition_encryption("Hi, hi Jane! I'm so. So glad to to finally be able to write - WRITE!! - to you!") == 4)
assert(repetition_encryption("Yo-yo, how's s it going going for ya? Ya is okay, okay'nt ya?") == 5)
assert(repetition_encryption("My friend, friend of mine, I am really-really happy for you! You are amazing, please write me back when you can") == 3)
assert(repetition_encryption("Everything is fine, fine perfectly here. Here I have fun (fun all the day!) days. Although I miss you, so please please, Jane, write, write me whenever you can! Can you do that? That is the only (!!ONLY!!) thing I ask from you, you sunshine.") == 9)
assert(repetition_encryption("Do not notify me about this in the future") == 0)
assert(repetition_encryption("let's s?,play%3with,1symbols88,/symbols") == 2)
