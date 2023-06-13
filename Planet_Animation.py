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

earth = turtle.Turtle()
earth.shape('circle')
earth.shapesize(stretch_len=2, stretch_wid=2)
earth.color('turquoise')
earth.pu()
earth.goto(500, 20)
earth.pensize(5)
earth.pd()

moon = turtle.Turtle()
moon.shape('circle')
moon.shapesize(stretch_len=1, stretch_wid=1)
moon.color('light gray')
moon.pu()
moon.goto(earth.xcor(), earth.ycor())
moon.fd(35)

mars = turtle.Turtle()
mars.shape('circle')
mars.shapesize(stretch_len=1.3, stretch_wid=1.3)
mars.color('#FF0000')
mars.pu()
mars.goto(480, 175)
mars.pensize(5)
mars.pd()

jupiter = turtle.Turtle()
jupiter.shape('circle')
jupiter.shapesize(stretch_len=3.5, stretch_wid=3.5)
jupiter.color('#884513')
jupiter.pu()
jupiter.goto(300, 305)
jupiter.pensize(5)
jupiter.pd()

jupiter_spot = turtle.Turtle()
jupiter_spot.shape('circle')
jupiter_spot.shapesize(stretch_len=0.8, stretch_wid=0.8)
jupiter_spot.color('dark red')
jupiter_spot.pu()
jupiter_spot.goto(285, 300)

saturn = turtle.Turtle()
saturn.shape('circle')
saturn.shapesize(stretch_len=3, stretch_wid=3)
saturn.color('light yellow')
saturn.pu()
saturn.goto(45, 255)
saturn.pensize(5)
saturn.pd()

saturn_ring = turtle.Turtle()
saturn_ring.ht()
saturn_ring.color('#ab604a')
saturn_ring.pu()
saturn_ring.goto(45, 213)
saturn_ring.pensize(4)
saturn_ring.pd()
saturn_ring.circle(42)

uranus = turtle.Turtle()
uranus.shape('circle')
uranus.shapesize(stretch_len=2.6, stretch_wid=2.6)
uranus.color('light blue')
uranus.pu()
uranus.goto(-150, 0)
uranus.pensize(5)
uranus.pd()

neptune = turtle.Turtle()
neptune.shape('circle')
neptune.shapesize(stretch_len=2.3, stretch_wid=2.3)
neptune.color('blue')
neptune.pu()
neptune.goto(-50, -325)
neptune.pensize(5)
neptune.pd()


