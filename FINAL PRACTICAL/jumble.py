import random

word: str = input ("Enter a word: ")

word = list(word)
random.shuffle(word)
word = "".join(word)

print(word)
