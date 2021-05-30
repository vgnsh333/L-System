# backend.py

import turtle

def canvas_builder(title, canvas_width, canvas_height, square_length):
    CANVAS_COLOR = "red"
    PEN_COLOR = "black"
    scr = turtle.Screen()
    scr.screensize(canvas_width, canvas_height)
    scr.title(title)
    scr.bgcolor(CANVAS_COLOR)
    turtle.setworldcoordinates(0, 0, canvas_width, canvas_height)
    t = turtle.Turtle()
    t.color(PEN_COLOR)
    t.begin_fill()
    for i in range(4):
        t.forward(square_length)
        t.left(90)
    t.end_fill()
    turtle.done()