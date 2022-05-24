# from turtle import Turtle, Screen
# import random
#
# tim = Turtle()
# # new object of turtle class
#
# tim.shape('turtle')
# tim.color('red')


# for i in range(4):
#     tim.forward(100)
#     tim.left(90)
# the above lines of code makes a square of 100*100

# the below code makes a dashed line
# for _ in range(10):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

# making different shapes with different colors

# colours = ['aquamarine', 'navy', 'light blue', 'lawn green']
#
#
# def shape(side):
#     angle = 360/side
#     tim.color(random.choice(colours))
#     for _ in range(side):
#         tim.forward(50)
#         tim.rt(angle)
#
# for i in range(3,11):
#     shape(i)



# random walk challenge
# pen_size = tim.pensize(5)
# # sets the size of the pen.
# tim.speed(0)
# # animation speed of turtle
# angle = [0, 90, 180, 270, 360]
# color_list = ['#00ffff', '#845fff', '#2714ff', '#871423', '#ffff00', '#ff0000']
#
#
# def random_path(pen, angle, color_list):
#     tim.hideturtle()  # hides the turtle
#     i = 0
#     while i<100 :
#
#         tim.color(random.choice(color_list))
#         tim.fd(15)
#         tim.setheading(random.choice(angle))
#         # sethheading chooses the direction randomly
#         i += 1


# random_path(pen_size, angle, color_list)



# importing turtle as t and using the colormode function to change the colormode of the pen everytime.
# turtle.colormode() is as to be used instead of turtle object(like tim).
# now we can generate random colors.
# import turtle as t
# import random
#
# tim = t.Turtle()
# tim.ht()
# t.colormode(255)
# direction =[0, 90, 180, 270, 360]
# tim.pensize(5)
# tim.speed(0)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# for _ in range(200):
#
#     tim.color(random_color())
#     tim.forward(10)
#     tim.setheading(random.choice(direction))


# makiung a spiro graph

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed(0)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def spiro():
    for _ in range(120):
        tim.color(random_color())
        tim.circle(100)
        tim.lt(3)


spiro()


















screen = t.Screen()
screen.exitonclick()





