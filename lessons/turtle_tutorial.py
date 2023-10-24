from turtle import Turtle, colormode, done
colormode(255)
leo = Turtle()


leo.goto(45, 60)
leo.color(99, 204, 250)

i: int = 0
leo.begin_fill()
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()


bob = Turtle()
bob.color("black")
bob.goto(45, 60)
bob.speed = 10
while (i < 3):
    bob.forward(300)
    bob.left(120)
    i = i + 1


done()