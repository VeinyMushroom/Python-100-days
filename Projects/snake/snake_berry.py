import turtle as t
import random as r
from Projects.snake.screen import draw_grid

import screen

draw_grid()

berry = t.Turtle()
berry.color("red")
berry.shape("square")
berry.shapesize(8,8)
berry.penup()
berry.setpos(r.randrange(-600, 600, 2), 0)