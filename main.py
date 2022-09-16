# # Extracting colors from image
# import colorgram
#
# colors = colorgram.extract('image.jpg', 55)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

import turtle
from turtle import Turtle, Screen
import random

colors_list = [(223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235),
               (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43),
               (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87),
               (193, 187, 46), (240, 204, 2), (1, 102, 119), (50, 150, 109), (172, 212, 172), (118, 36, 34),
               (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210), (77, 37, 76), (120, 117, 155)]

turtle.colormode(255)
turtle = Turtle()

def row_of_dots():
    for _ in range(10):
        turtle.pendown()
        turtle.dot(20, random.choice(colors_list))
        turtle.penup()
        turtle.forward(50)

y = -250.0
for _ in range(10):
    turtle.penup()
    turtle.goto(-250.0, y)
    row_of_dots()
    y += 50.0

screen = Screen()
screen.exitonclick()
