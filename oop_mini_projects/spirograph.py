import random
import turtle as t

tim = t.Turtle()

def random_color():
    red = random.randint(0,255)/255.0
    green = random.randint(0,255)/255.0
    blue = random.randint(0,255)/255.0
    color  = (red, green , blue)
    return color

tim.speed("fastest")

def spiro(size):
    for i in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)

spiro(5)

screen = t.Screen()
screen.exitonclick()