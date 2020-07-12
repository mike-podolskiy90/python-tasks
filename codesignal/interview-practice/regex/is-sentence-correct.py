import re


def is_sentence_correct(sentence):
    pattern = "^[A-Z][^.!?]*[.!?]$"
    return re.match(pattern, sentence) is not None


print(is_sentence_correct("This is an example of *correct* sentence."))
print(is_sentence_correct("!this sentence is TOTALLY incorrecT"))
print(is_sentence_correct("Almost correct sentence"))
print(is_sentence_correct("Something is !wrong! here."))
print(is_sentence_correct("Time to roll!!!"))
print(is_sentence_correct("This one is okay though, isn't it?"))
