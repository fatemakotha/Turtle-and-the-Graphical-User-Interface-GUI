import random
import turtle
from turtle import Turtle, Screen # imports the Turtle and Screen class that's inside the turtle module
import random
#Create a new Turtle OBJECT named cutu_the_turtle
cutu = Turtle()
# print(cutu_the_turtle) #window opens but dissapears


cutu.shape("turtle") #makes the arrow change into a turtle
cutu.color("dark cyan")
cutu.pensize(10) #increases the width of the pen
#CHANGING the SPEED of the turtle. 0 OR "fastest", 10 OR "fast", 6 OR "normal", 3 OR "slow", 1 OR "slowest" ***
cutu.speed(10) #we can either insert the int or the string. i.e. 0 or "fastest"

# cutu.colormode(255) *** DOES NOT WORK
turtle.colormode(255) #The issue is that your Turtle object (cutu) doesn't have a colormode method. There is one in the turtle module itself though.
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour_tuple = (r, g, b) #created a tuple
    return random_colour_tuple
cutu.forward(100)
directions = [0, 90, 180, 270] #these values are used in setheading() to point north south east west

for _ in range(200):
    cutu.pencolor(random_color()) #used the FUNCTION random_color **
    cutu.forward(30) #moves 30 units
    cutu.setheading(random.choice(directions)) #changes the left&right to the degrees in the direction list




screen  = Screen()
screen.exitonclick() #makes the window stay longer #THIS NEEDS TO BE AT THE END OF THE CODE *