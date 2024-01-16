import random

print(random.randint(1, 10)) # нам нужен только randint, его можно импортировать отдельно

from random import randint as RI
print(RI(1, 10))
