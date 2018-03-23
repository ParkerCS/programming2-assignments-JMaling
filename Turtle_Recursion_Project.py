# H-TREE RECURSION
import turtle
import random
my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape("classic")
my_turtle.width(2)
my_screen = turtle.Screen()
my_screen.bgcolor("white")
my_turtle.speed(0)

def htree_recursion(x, y, side_length, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + (side_length / 2), y)
        my_turtle.goto(x + (side_length / 2), y + (side_length / 2))
        my_turtle.goto(x + (side_length / 2), y - (side_length / 2))
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x - (side_length / 2), y)
        my_turtle.goto(x - (side_length / 2), y + (side_length / 2))
        my_turtle.goto(x - (side_length / 2), y - (side_length / 2))
        htree_recursion(x + (side_length / 2), y + (side_length / 2), side_length / 2, depth - 1)
        htree_recursion(x + (side_length / 2), y - (side_length / 2), side_length / 2, depth - 1)
        htree_recursion(x - (side_length / 2), y + (side_length / 2), side_length / 2, depth - 1)
        htree_recursion(x - (side_length / 2), y - (side_length / 2), side_length / 2, depth - 1)
htree_recursion(0, 0, 150, 2)

my_screen.clear()

my_turtle.goto(-200, -200)
def escher_fractal(side_length, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.down()
        my_turtle.forward(side_length)
        my_turtle.left(90)
        my_turtle.forward(side_length)
        my_turtle.left(90)
        my_turtle.forward(side_length)
        my_turtle.left(90)
        my_turtle.forward(side_length)
        my_turtle.left(90)
        my_turtle.forward(side_length / 2)
        my_turtle.left(45)
        escher_fractal((((side_length / 2) ** 2) + ((side_length / 2) ** 2)) ** .5, depth - 1)
escher_fractal(400, 4)

my_screen.clear()

def random_fractal(radius, iterations):
    my_turtle.up()
    my_turtle.goto(200, -100)
    my_turtle.down()
    for i in range(iterations):
        for j in range(180):
            my_turtle.forward(radius / 20)
            my_turtle.left(4)
            if j >= 60:
                my_turtle.forward(radius / 40)

random_fractal(100, 5)


my_screen.exitonclick()