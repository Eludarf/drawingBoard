from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
n = 0


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_counter_clock_w():
    global n
    n += 10
    tim.setheading(n)


def rotate_clock_w():
    global n
    n -= 10
    tim.setheading(n)


def clear():
    global n
    tim.clear()
    screen.resetscreen()
    n = 0


screen.listen()
screen.onkey(key="a", fun=rotate_counter_clock_w)
screen.onkey(key="d", fun=rotate_clock_w)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear)
screen.exitonclick()


