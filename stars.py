import turtle


def star(size, n, d=2):
    t.pendown()
    t.begin_fill()
    for _ in range(n):
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.penup()


def star_recursive(size, n, level, d=2):
    if level == 0:
        return
    else:
        t.forward(size)
        t.right((360-((n-2)*180/n)))
        star_recursive(size, n, level - 1, d)


# main program
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
    star(100, 5, 2)  # should draw a purple pentagram (5-pointed star)

    t.penup()
    t.goto(150, 0)
    t.color('red')
    t.pendown()
    t.begin_fill()
    star_recursive(100, 8, 8, 3)  # should draw a red octagram (8-pointed star)
    t.end_fill()
    t.penup()
    turtle.done()
