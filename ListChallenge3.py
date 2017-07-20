
from random import *
#this is a fake haiku because real haikus are 5-7-5 not 5-3-5
five_syllable = ["Welcome to coding", "Hello this is code", "How is it going"]
three_syllable = ["You are here", "Fun is here", "This is fun"]


x = randint(0, len(five_syllable)-1)
y = randint(0, len(three_syllable)-1)
z = randint(0, len(five_syllable)-1)
print(five_syllable[x])
print(three_syllable[y])
print(five_syllable[z])
