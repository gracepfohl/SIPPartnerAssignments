
from random import *


#Create the list of words you want to choose from.
appetizers = ["Chips and Salsa", "Chips and Queso", "Soft Pretzels",]
entrees = ["Chicken Wings", "Sandwich", "Burger"]
drinks = ["soda", "coffee", "milk", "water"]
desserts = ["cake", "brownie", "cupcake", "ice cream"]
#Generates a random integer.
x = randint(0, len(appetizers)-1)
y = randint(0, len(entrees)-1)
z = randint(0, len(drinks)-1)
a = randint(0, len(desserts)-1)

print(appetizers[x])
print(entrees[y])
print(drinks[z])
print(desserts[a])
