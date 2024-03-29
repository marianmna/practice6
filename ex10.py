from turtle import *
import turtle

import math

t = turtle.Turtle()
w = turtle.Screen()

x1_1 = float(input('первая координата x первого прямоугольника: '))
y1_1 = float(input('первая координата y первого прямоугольника: '))
x1_2 = float(input('вторая координата x первого прямоугольника: '))
y1_2 = float(input('вторая координата у первого прямоугольника: '))
x2_1 = float(input('первая координата x второго прямоугольника: '))
y2_1 = float(input('первая координата y второго прямоугольника: '))
x2_2 = float(input('вторая координата x второго прямоугольника: '))
y2_2 = float(input('вторая координата y второго прямоугольника: '))


def rectangle(a, b):
    t.penup()
    t.goto(a, b)
    t.pendown()
    for i in range(2):
        t.forward(a)
        t.left(90)
        t.forward(b)
        t.left(90)


a1 = y1_1 - y1_2
b1 = x1_1 - x1_2
a2 = y2_1 - y2_2
b2 = x2_1 - x2_2

rectangle(a1, b1)
rectangle(a2, b2)


def rectangle_relation(rect1, rect2):
    if (rect1[0][0] > rect2[1][0] or rect1[1][0] < rect2[0][0] or
        rect1[0][1] > rect2[1][1] or rect1[1][1] < rect2[0][1]):
        return "Прямоугольники лежат вне друг друга, не касаясь"
    elif (rect1[0][0] == rect2[1][0] or rect1[1][0] == rect2[0][0] or
          rect1[0][1] == rect2[1][1] or rect1[1][1] == rect2[0][1]):
        return "Прямоугольники имеют касание"
    elif (rect1[0][0] < rect2[1][0] and rect1[1][0] > rect2[0][0] and
          rect1[0][1] < rect2[1][1] and rect1[1][1] > rect2[0][1]):
        return "Прямоугольники имеют пересечение"
    elif (rect1[0][0] > rect2[0][0] and rect1[1][0] < rect2[1][0] and
          rect1[0][1] > rect2[0][1] and rect1[1][1] < rect2[1][1]):
        return "Один прямоугольник лежит внутри другого, не касаясь"
    else:
        return "Прямоугольники пересекаются"


rect1 = [x1_1, y1_1, x1_2, y1_2]
rect2 = [x2_1, y2_1, x2_2, y2_2]

relation = rectangle_relation(rect1, rect2)
print(relation)

w.mainloop()