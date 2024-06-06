import turtle
import random

bob = turtle.Turtle()

points = 0
lives = 3

def Italy():
    bob.pu()
    bob.goto(-200, 50)
    bob.pd()
    bob.fillcolor("green")

    bob.pencolor("green")
    bob.begin_fill()
    bob.fd(200)
    bob.rt(90)
    bob.fd(400)
    bob.rt(90)
    bob.fd(200)
    bob.rt(90)
    bob.fd(400)
    bob.end_fill()

    bob.rt(90)
    bob.fd(200)

    bob.fillcolor("white")

    bob.pencolor("white")
    bob.begin_fill()
    bob.fd(200)
    bob.rt(90)
    bob.fd(400)
    bob.rt(90)
    bob.fd(200)
    bob.rt(90)
    bob.fd(400)
    bob.end_fill()

    bob.rt(90)
    bob.fd(200)

    bob.fillcolor("red")

    bob.pencolor("red")
    bob.begin_fill()
    bob.fd(200)
    bob.rt(90)
    bob.fd(400)
    bob.rt(90)
    bob.fd(200)
    bob.rt(90)
    bob.fd(400)
    bob.end_fill()

    bob.pu()
    bob.fd(10000)

def France():
    bob.pu()
    bob.goto(-200, 50)
    bob.pd()
    bob.fillcolor("blue")

    bob.pencolor("blue")
    bob.begin_fill()
    bob.fd(200)
    bob.rt(90)
    bob.fd(400)
    bob.rt(90)
    bob.fd(200)
    bob.rt(90)
    bob.fd(400)
    bob.end_fill()

    bob.rt(90)
    bob.fd(200)

    bob.fillcolor("white")

    bob.pencolor("white")
    bob.begin_fill()
    bob.fd(200)
    bob.rt(90)
    bob.fd(400)
    bob.rt(90)
    bob.fd(200)
    bob.rt(90)
    bob.fd(400)
    bob.end_fill()

    bob.rt(90)
    bob.fd(200)

    bob.fillcolor("red")

    bob.pencolor("red")
    bob.begin_fill()
    bob.fd(200)
    bob.rt(90)
    bob.fd(400)
    bob.rt(90)
    bob.fd(200)
    bob.rt(90)
    bob.fd(400)
    bob.end_fill()

    bob.pu()
    bob.fd(10000)

def Germany():
    bob.fillcolor("black")

    bob.begin_fill()

    for i in range(2):
        bob.fd(300)
        bob.rt(90)
        bob.fd(100)
        bob.rt(90)
    bob.end_fill()

    bob.rt(90)
    bob.fd(100)
    bob.begin_fill()
    bob.fillcolor("red")

    for i in range(2):
        bob.fd(100)
        bob.lt(90)
        bob.fd(300)
        bob.lt(90)
    bob.end_fill()

    bob.fd(200)
    bob.lt(90)
    bob.begin_fill()
    bob.fillcolor("yellow")

    for i in range(2):
        bob.fd(300)
        bob.lt(90)
        bob.fd(100)
        bob.lt(90)
    bob.end_fill()

def Finland():
    bob.pencolor("black")
    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
        bob.fd(300)
        bob.rt(90)
        bob.fd(160)
        bob.rt(90)
    bob.end_fill()
    bob.fillcolor("blue")
    bob.fd(100)
    bob.begin_fill()
    for i in range(2):
        bob.rt(90)
        bob.fd(160)
        bob.rt(90)
        bob.fd(30)
    bob.end_fill()
    bob.fd(200)
    bob.rt(90)
    bob.fd(70)
    bob.rt(90)
    bob.begin_fill()
    for i in range(2):
        bob.fd(300)
        bob.lt(90)
        bob.fd(30)
        bob.lt(90)
    bob.end_fill()

def Poland():
    bob.fillcolor("white")

    bob.begin_fill()

    for i in range(2):
        bob.fd(300)
        bob.rt(90)
        bob.fd(100)
        bob.rt(90)
    bob.end_fill()

    bob.rt(90)
    bob.fd(100)
    bob.begin_fill()
    bob.fillcolor("red")

    for i in range(2):
        bob.fd(100)
        bob.lt(90)
        bob.fd(300)
        bob.lt(90)
    bob.end_fill()

def Greece():
    bob.fillcolor("blue")
    bob.fd(100)
    bob.begin_fill()
    for i in range(2):
        bob.rt(90)
        bob.fd(70)
        bob.rt(90)
        bob.fd(30)
    bob.end_fill()
    bob.fd(200)
    bob.rt(90)
    bob.fd(70)
    bob.rt(90)
    bob.begin_fill()
    for i in range(2):
        bob.fd(300)
        bob.lt(90)
        bob.fd(30)
        bob.lt(90)
    bob.end_fill()


#lista me flags
flags = [Italy, France, Germany, Finland, Poland]

while lives>0 and len(flags) >0:
     bob.reset()
     bob.speed(200)
     flag = random.choice(flags)
     flag()
     answer = input("Guess the flag")

     if answer  == flag.__name__:
         print("Medium Rare")
         points = points +1
         print("Points:", points)
         print("Lives:", lives)
         flags.remove(flag)

     else:
         print("Medium Well")
         if points>0:
             points -= 1
         else:
             points =0
         lives -= 1
         print("Points: ",points)
         print("Lives: ",lives)
#Italy()
#France()
#Germany()
#Finland()
#Poland()
#Greece()


