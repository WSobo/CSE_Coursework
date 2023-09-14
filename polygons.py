import turtle


def polygon(size, n: int):
    t.pendown()
    t.begin_fill()
    for i in range(n):
        t.forward(size)
        t.left(360/n)


def polygon_recursive(size, n, level):
    if level == 0:
        return
    else:
        t.forward(size)
        t.left(360 / n)
        polygon_recursive(size, n, level - 1)


if __name__ == '__main__':
    s = turtle.Screen()
    s.setup(800, 400)
    s.bgcolor("white")
    s.title("Turtle Program")

    t = turtle.Turtle()
    t.shape("turtle")
    t.pen(pencolor='dark violet', fillcolor='dark violet', pensize=3, speed=1)

    t.penup()
    t.goto(-150, 0)
    polygon(100, 5)  # should draw a purple pentagon

    t.penup()
    t.goto(150, 0)
    t.color('red')
    t.pendown()
    polygon_recursive(100, 5, 5)  # should draw a red pentagon
