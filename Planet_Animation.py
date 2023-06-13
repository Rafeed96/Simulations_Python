import turtle
import time

wn = turtle.Screen()
wn.title("Solar System")
wn.bgpic("E:\Projects\Repositories\Python\Simulations_Python\Images\Black.png")
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

mercury.setheading(0)
venus.setheading(45)
earth.setheading(90)
mars.setheading(135)
jupiter.setheading(180)
jupiter_spot.setheading(180)
saturn.setheading(225)
uranus.setheading(270)
neptune.setheading(315)

wn.tracer(10)


def orbits():
    mercury.fd(5)
    mercury.lt(2.4)
    venus.fd(5)
    venus.lt(1.8)
    earth.fd(5)
    earth.lt(1.4)
    moon.goto(earth.xcor(), earth.ycor())
    moon.fd(35)
    moon.rt(5)
    mars.fd(5)
    mars.lt(1.1)
    jupiter.fd(5)
    jupiter.lt(0.9)
    jupiter_spot.fd(5)
    jupiter_spot.lt(0.9)
    saturn.fd(5)
    saturn.lt(0.76)
    uranus.fd(5)
    uranus.lt(0.67)
    neptune.fd(5)
    neptune.lt(0.61)


def Game():
    mercury_x = str(mercury.xcor())
    mercury_y = str(mercury.ycor())
    venus_x = str(venus.xcor())
    venus_y = str(venus.ycor())
    earth_x = str(earth.xcor())
    earth_y = str(earth.ycor())
    moon_x = str(moon.xcor())
    moon_y = str(moon.ycor())
    mars_x = str(mars.xcor())
    mars_y = str(mars.ycor())
    jupiter_x = str(jupiter.xcor())
    jupiter_y = str(jupiter.ycor())
    saturn_x = str(saturn.xcor())
    saturn_y = str(saturn.ycor())
    uranus_x = str(uranus.xcor())
    uranus_y = str(uranus.ycor())
    neptune_x = str(neptune.xcor())
    neptune_y = str(neptune.ycor())

    pen.goto(-850, 450)
    pen.color("yellow")
    pen.goto(-700, 450)
    pen.color("dark red")
    pen.goto(-850, 350)
    pen.color("dark gray")
    pen.goto(-850, 250)
    pen.color("white")
    pen.goto(-850, 150)
    pen.color("turquoise")
    pen.goto(-850, 50)
    pen.color("light gray")
    pen.goto(-850, -50)
    pen.color("#FF0000")
    pen.goto(-850, -150)
    pen.color("#8B4513")
    pen.goto(-850, -250)
    pen.color("light yellow")
    pen.goto(-850, -350)
    pen.color("light blue")
    pen.goto(-850, -450)
    pen.color("blue")


while True:
    orbits()
    Game()
    saturn_ring.clear()
    saturn_ring.goto(saturn.xcor()-1, saturn.ycor()-45)
    saturn_ring.circle(42)
    wn.update()

wn.mainloop()