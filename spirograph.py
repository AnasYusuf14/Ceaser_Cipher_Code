import turtle as t
t.colormode(255)
import random
timmy =t.Turtle()
timmy.speed(0)
timmy.pensize(1)
def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_tuple =(r , g ,b)
    return my_tuple
size_of_gap = 5
for _ in range(int(360/size_of_gap)):
    timmy.color(rand_color())
    timmy.circle(100)
    currunt_head = timmy.heading()
    timmy.setheading(currunt_head+size_of_gap)

screen = t.Screen()
screen.exitonclick()
