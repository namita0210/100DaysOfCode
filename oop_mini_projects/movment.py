import random
import turtle as t

tim = t.Turtle()

colors = ['red','yellow','blue','green','pink','brown','black','grey','silver','red']
directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")

for i in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))