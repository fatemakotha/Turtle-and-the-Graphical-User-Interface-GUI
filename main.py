from turtle import Turtle, Screen # imports the Turtle and Screen class that's inside the turtle module

#Create a new Turtle OBJECT named cutu_the_turtle
cutu = Turtle()
# print(cutu_the_turtle) #window opens but dissapears
cutu.shape("turtle") #makes the arrow change into a turtle
cutu.color("dark cyan")

#How to make the object do certain things/FUNCTIONS
for _ in range(15):
    cutu.pencolor("black") #changes the color of the drawing pen
    cutu.forward(10) #moves forward by 10 paces
    cutu.penup() #is used to stop the drawing.
    cutu.forward(10) #moves forward by 10 paces
    cutu.pendown() #is used to continue the drawing.










screen  = Screen()
screen.exitonclick() #makes the window stay longer #THIS NEEDS TO BE AT THE END OF THE CODE *