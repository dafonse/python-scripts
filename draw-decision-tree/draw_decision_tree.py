'''
https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''

import turtle
from time import sleep
from math import ceil

hr = turtle.Turtle()
hr.left(90)
hr.speed(150)
slp = 0.2


def tree(i):
    if i < 10:
        return
    else:
        hr.forward(i)
        sleep(slp)
        hr.left(30)
        sleep(slp)
        print(f'left: {ceil(3*i/4)}')
        tree(3 * i / 4)
        hr.right(60)
        sleep(slp)
        print(f'right: {ceil(3*i/4)}')
        tree(3 * i / 4)
        hr.left(30)
        sleep(slp)
        hr.backward(i)


tree(90)
turtle.done()
