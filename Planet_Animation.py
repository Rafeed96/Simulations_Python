import turtle
import time

wn = turtle.Screen()
wn.title("Solar System")
wn.bgpic("https://images.unsplash.com/photo-1544656376-ffe19d4b7353?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YmxhY2slMjBza3l8ZW58MHx8MHx8fDA%3D&w=1000&q=80")
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
