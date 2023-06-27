import turtle

from itertools import cycle
colors=cycle(['pink','peach puff','grey','hot pink','light blue','lawn green'])

def draw_circle(size,angle,shift,):
  turtle.bgcolor(next(colors))
  turtle.pencolor(next(colors))
  turtle.circle(size)
  turtle.right(angle)
  turtle.forward(shift)
  draw_circle(size+5,angle+1,shift+1)

turtle.bgcolor('white')
turtle.speed('fast')
turtle.pensize(40)
draw_circle(28,0,1)
