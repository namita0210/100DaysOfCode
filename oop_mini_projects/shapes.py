import turtle as t
import random

tim = t.Turtle()

colors = ['red','yellow','blue','green','pink','brown','black','grey','silver','red']

def create_shape(n_sides):
    angle = 360/n_sides
    for i in range(n_sides):
        tim.forward(500)
        tim.right(angle)
    
for shape_side in range(3,11):
    tim.fillcolor(random.choice(colors))
    create_shape(shape_side)    
