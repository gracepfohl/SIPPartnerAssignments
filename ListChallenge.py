
from random import *


#Create the list of words you want to choose from.
name_list = ["Grace", "Sam", "Sonna", "Joyce", "Sara", "Carla", "Hannah", "Lily", "Polly"]

#Generates a random integer.
x = randint(0, len(name_list)-1)
print (name_list[x])
