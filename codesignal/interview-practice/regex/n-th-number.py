import re


def nth_number(s, n):
    pattern = "(?:\\D*\\d+){" + str(n - 1) + "}\\D*[0]*(\\d+)"
    return re.match(pattern, s).group(1)


assert(nth_number("8one 003number 201numbers li-000233le number444", 4) == "233")
assert(nth_number("some023020 num ber 033 02103 32 meh peh beh 4328 ", 5) == "4328")
assert(nth_number("007 is an awesome agent", 1) == "7")
assert(nth_number("Everyone hates error 404", 1) == "404")
assert(nth_number("LaS003920tP3rEt4t04Yte0023s3t", 4) == "4")
assert(nth_number("=_aaYiM*}&0077|D))ztIV00012432748730156644204805614898523099655216oio0854102350044141_|YDL0584511290939644184700867021026771007612398051168360441323oIc:G*0204864749576405915~wqgN0037594999439741539584332{F&wjxiLy-mE", 4) == "584511290939644184700867021026771007612398051168360441323")
