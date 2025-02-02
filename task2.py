import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        return

    for _ in range(4):
        t.forward(length)
        t.right(90)

    t.forward(length)
    t.left(45)

    new_length = length * math.sqrt(2) / 2

    draw_pythagoras_tree(t, new_length, level - 1)

    t.right(90)
    draw_pythagoras_tree(t, new_length, level - 1)

    t.left(45)
    t.backward(length)

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-50, -200)
t.pendown()
t.left(90)

level = int(input("Введіть рівень рекурсії: "))

initial_length = 100
draw_pythagoras_tree(t, initial_length, level)

screen.mainloop()
