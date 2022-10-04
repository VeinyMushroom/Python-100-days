from turtle import Turtle, Screen
turt = Turtle()
turt.speed('fastest')
screen = Screen()
screen.listen()

def WMove():
    turt.forward(10)
screen.onkey(key="w", fun=WMove)

def SMove():
    turt.back(10)
screen.onkey(key="s", fun=SMove)

def DTurn():
    turt.right(10)
screen.onkey(key="d", fun=DTurn)

def ATurn():
    turt.left(10)
screen.onkey(key="a", fun=ATurn)


screen.exitonclick()
