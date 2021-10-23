from turtle import Turtle, Screen

tim_turtle = Turtle()
screen = Screen()


def move_forward():
        tim_turtle.forward(30)

def move_backward():
        tim_turtle.backward(30)
def clockwise():
        tim_turtle.right(50)
def anti_clockwise():
        tim_turtle.left(50)
def clear_and_reset():
        tim_turtle.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=anti_clockwise)
screen.onkey(key="c", fun=clear_and_reset)
screen.exitonclick()
