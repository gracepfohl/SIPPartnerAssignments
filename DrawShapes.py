from turtle import * #imports entire turtle library already created
import math

# Name your Turtle.



### Write your code below:
#this draws a square
#how do i loop this to user input? Helpppppppppp

def Draw_Shape(num_sides): #num_sides=argument and parameter
    # Set Up your screen and starting position.
    turtle = Turtle() #calls Turtle function
    setup(1000,800) #Refers to size of turtle
    x_pos = 0 #start location of turtle
    y_pos = 0 #start location of turtle
    turtle.penup() #makes turtle to move without drawing a line

    turtle.setposition(x_pos, y_pos)
    turtle.pendown() #allows turtle to draw again
    angle = 360 / num_sides #formula for angle of a shape

    for side in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)

user_input = input("How many sides do you wnat in your shape?")
user_input = int(user_input)

Draw_Shape(user_input)


# Closes window on click.
exitonclick()
