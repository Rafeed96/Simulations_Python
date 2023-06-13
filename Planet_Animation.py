import turtle
import time

wn = turtle.Screen()
wn.title("Solar System")
wn.bgpic("E:\Projects\Repositories\Python\Simulations_Python\Images\Black_Sky.jpg")
wn.setup(width=1750, height=1000)

pen = turtle.Turtle()
pen.ht()
pen.pu()

sun = turtle.Turtle()
sun.shape('circle')
sun.shapesize(stretch_len=8, stretch_wid=8)
sun.color('yellow')
sun.pu()
sun.goto(300, 0)

mercury = turtle.Turtle()
mercury.shape('circle')
mercury.shapesize(stretch_len=1.2, stretch_wid=1.2)
mercury.color('dark gray')
mercury.pu()
mercury.goto(300, -105)
mercury.pensize(5)
mercury.pd()

venus = turtle.Turtle()
venus.shape('circle')
venus.shapesize(stretch_len=1.5, stretch_wid=1.5)
venus.color('white')
venus.pu()
venus.goto(420, -95)
venus.pensize(5)
venus.pd()
