from turtle import Turtle, Screen # imports the Turtle and Screen class that's inside the turtle module

#Create a new Turtle OBJECT named cutu_the_turtle
cutu = Turtle()
# print(cutu_the_turtle) #window opens but dissapears
cutu.shape("turtle") #makes the arrow change into a turtle
cutu.color("dark cyan")

#How to make the object do certain things/FUNCTIONS
#TO DRAW AN EQUILATERAL TRIANGLE WITH SIDES 100

for _ in range(3):
    cutu.pencolor("cyan")
    cutu.forward(100)
    cutu.right(90)
    cutu.right(30)
#TO DRAW AN SQUARE WITH SIDES 100
for _ in range(4):
    cutu.pencolor("red")
    cutu.forward(100)
    cutu.right(90)













screen  = Screen()
screen.exitonclick() #makes the window stay longer #THIS NEEDS TO BE AT THE END OF THE CODE *