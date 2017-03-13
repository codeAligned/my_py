import turtle
import random
import math

i=0
phi=0.0
turtle.speed(100)
while i<100:
    turtle.circle(random.randrange(0,100))
    phi=random.randrange(0,360)
    r=random.randrange(0,200)
    turtle.goto(r*math.sin(phi/57.),r*math.cos(phi/57.))
    print(r*math.sin(phi/57.),r*math.cos(phi/57.))
    i += 1
turtle.textinput("nigga?","huila")