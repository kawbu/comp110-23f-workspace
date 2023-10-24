"""EX03: Turtle Art: Logo for popular game 'osu!'."""

__author__ = "730658017"


from turtle import Turtle, colormode, bgcolor, done

pen = Turtle()
pen.pensize(2)
pen.speed(11)
colormode(255)
bgcolor(128, 128, 128)


def main() -> None:
    """Main function."""
    x, y = 0, 0
    
    draw_circle(330, x, y - 300, [255, 255, 255], "white")
    draw_circle(300, x, y - 270, [240, 100, 164], "white")
    oval(30, 90, x - 140, y - 30)
    draw_letter_s(30, 40, x - 30, y - 45)
    draw_letter_u(30, 30, x + 60, y + 105)
    draw_exclamation_mark(30, x + 225, y + 135)
    pen.hideturtle()
    done()
    
    
def draw_circle(radius: int, x: int, y: int, color: list[int], pen_color: str) -> None:
    """Draws a circle of given radius, with a given fill and outline color at a given (x,y) coordinate."""
    pen.color(pen_color)
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.begin_fill()
    pen.circle(radius)
    pen.fillcolor(color[0], color[1], color[2])
    pen.end_fill()
    
    
def oval(width: int, radius: int, x: int, y: int) -> None:
    """Draws an oval of given width and given radius starting at a given (x,y) coordinate."""
    pen.up()
    pen.width(width)
    pen.goto(x, y)
    pen.down()
    pen.left(45)
    for i in range(0, 2):
        pen.circle(radius, 90)
        pen.circle(radius / 2, 90)
    pen.setheading(0)


def draw_letter_s(width: int, radius: int, x: int, y: int) -> None:
    """Draws the letter s with a given pen width and radius starting at a given (x, y) coordinate."""
    pen.pensize(width)
    pen.up()
    pen.goto(x, y)
    pen.down()
    
    pen.circle(radius, -60)
    pen.setheading(0)
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.circle(radius, 180)
    pen.setheading(0)
    pen.circle(radius, -230)
    pen.setheading(0)
    

def draw_letter_u(width: int, radius: int, x: int, y: int) -> None:
    """Draws the letter u with a given pen width and radius starting at a given (x, y) coordinate."""
    pen.pensize(width)
    pen.up()
    pen.goto(x, y)
    pen.down()
    
    pen.right(90)
    pen.backward(5)
    pen.forward(105)
    pen.circle(50, 180)
    pen.forward(105)
    pen.setheading(0)
    

def draw_exclamation_mark(width: int, x: int, y: int) -> None:
    """Draws an exclamation mark with a given pen width starting at a given (x, y) coordinate."""
    pen.pensize(width)
    pen.right(270)
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.backward(120)
    pen.up()
    pen.backward(60)
    pen.down()
    pen.backward(5)
    pen.setheading(0)


if __name__ == "__main__":
    main()