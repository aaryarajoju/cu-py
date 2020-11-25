# EXPERIMENT - 2
# TASK - 1 : WAP to take word input from user and display the input in jumbled form

import random

word = input ("Enter a word: ")
word = list(word)
random.shuffle(word)
word = "".join(word)

print(word)
