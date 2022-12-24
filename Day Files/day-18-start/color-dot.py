from PIL import Image
import turtle as t
import random
# import colorgram
import main 


colors = main.pix_val
screen = t.Screen()
t.colormode(255)

timmy = t.Turtle()
timmy.shape('classic')
timmy.speed('fastest')
screen.screensize(300, 300,)

timmy.penup()
timmy.setposition(-200, -200)

for x in range(0, 16):

    for x in range(0, len(main.pix_val)):
        first_color = colors
        rgb = 
        timmy.pencolor((rgb.r, rgb.g, rgb.b))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(25)

    if timmy.xcor() == 200:
        print(timmy.xcor() , "left")
        timmy.left(90)
        timmy.forward(25)
        timmy.left(90)
        timmy.forward(25)
        print(timmy.xcor())
    
    elif timmy.xcor() == -225:
        print(timmy.xcor(), "right")
        timmy.right(90)
        timmy.forward(25)
        timmy.right(90)
        timmy.forward(25)
        print(timmy.xcor())
screen.exitonclick()
