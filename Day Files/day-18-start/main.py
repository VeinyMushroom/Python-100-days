from PIL import Image
import turtle

# turtle.colormode(255)
# screen = turtle.Screen()
# t = turtle.Turtle()
# t.speed('fastest')
# screen.screensize(400,400)
# t.penup()
# t.setposition(-189,131)
# turtpos = t.ycor()

im = Image.open('/Users/eleanorextence/Desktop/100 Days Files/Day Files/day-18-start/Super_Mario_64_box_cover.jpg', 'r')
px = im.load()
px_val = dict(key = px[0], value = im.getdata())
print(px_val)
# for tup in pix_val:
#     t.pencolor((tup[0], tup[1], tup[2]))
#     t.pendown
#     t.dot(1)
#     t.penup()
#     t.forward(1)

#     if t.xcor() == 190:
#         t.setposition(-189, turtpos -1)
#         turtpos = t.ycor()




# screen.exitonclick()