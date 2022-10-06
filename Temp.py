
import re
str_ = 'qwer, dfdfdf ,erwrer dfsdfd ,fsdfsdfs'
# a = (str_.split(', '))
# print(a)
print(re.split(" ,|, | |;|,|\n", str_))