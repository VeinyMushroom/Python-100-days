from shutil import move
import turtle as t

tim = t.Turtle()
screen = t.Screen()
screen.listen()

def move_forwards():
    tim.forward(10)

screen.onkey(key="d", fun=move_forwards)

screen.exitonclick()

