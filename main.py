from turtle import Turtle, Screen

#Create a new Turtle OBJECT named cutu_the_turtle
cutu_the_turtle = Turtle()
# print(cutu_the_turtle) #window opens but dissapears
cutu_the_turtle.shape("turtle") #makes the arrow change into a turtle
cutu_the_turtle.color("dark cyan")

#How to make the object do certain things/FUNCTIONS
for _ in range(4):
    cutu_the_turtle.forward(100) #moves forward by a 100 paces
    cutu_the_turtle.left(90.0) #turns right by 90 degress











screen  = Screen()
screen.exitonclick() #makes the window stay longer