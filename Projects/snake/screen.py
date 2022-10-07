import threading
import turtle as t
def draw_grid():
    """Will create a 1200 by 1200 grid using a turtle called grid. The thickness of the lines is 2 and the space in between the lines is 8(lines included)"""
    
    #setting up the sceen
    screen = t.Screen()
    screen.bgcolor()
    screen.title("Snake game")
    screen.mode("world")
    screen.reset()
    screen.setworldcoordinates(llx=-650, lly=-650, urx=650, ury=650)
    
    #Setting up grid drawer
    grid = t.Turtle(visible=False)
    grid.speed(0)
    grid.pensize(2)


    
    #Draws veritcal lines
    for coord in range(0, 1201, 30):
        grid.setheading(90)
        grid.penup()
        grid.setpos(x=600 - coord, y=-600)
        grid.pendown()
        grid.forward(1200)

    #Draws Horizontal lines
    for coord in range(0, 1201, 30):
        grid.penup()
        grid.setpos(x=600, y=-600 + coord)
        grid.pendown()
        grid.setheading(180)
        grid.forward(1200)

    screen.exitonclick()