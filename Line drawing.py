#Line Drawing Project
#Initialize
import turtle
Amaya = turtle.Turtle()
gabriel = turtle.Turtle()

#Functions
def orange():   #This is creating the smiley orange
    gabriel.dot(500,"#ff6600") #This is the base of the orange
    gabriel.left(180)
    gabriel.penup()
    gabriel.forward(20)
    gabriel.right(90)
    gabriel.forward(100)
    gabriel.dot(20,"#000000")
    gabriel.right(90)
    gabriel.forward(40)
    gabriel.dot(20,"#000000") #These two other dots are the eyes
    gabriel.goto(170,100)
    gabriel.pendown()
    gabriel.circle(40,-90)
    gabriel.circle(40,45)
    gabriel.right(80)
    gabriel.circle(-200,100)
    gabriel.penup()

def stem():    #This will be drawing the stem
    gabriel.goto(-5,230)
    gabriel.pendown()
    gabriel.right(90)
    gabriel.color("#009933") #Adds color
    gabriel.begin_fill()
    gabriel.circle(60,100)
    gabriel.left(50)
    gabriel.forward(30)
    gabriel.left(120)
    gabriel.circle(-60,100)
    gabriel.left(155)
    gabriel.forward(50)
    gabriel.end_fill()

def leaf():  #This draws the leaf right next to the stem
    gabriel.left(50)
    gabriel.begin_fill()
    gabriel.circle(-100,60)
    gabriel.left(10)
    gabriel.circle(60,60)
    gabriel.right(160)
    gabriel.circle(-100,120)
    gabriel.end_fill()

def slice():  #This is drawing the big slice
    Amaya.left(120)
    Amaya.color("orange") #Base color
    Amaya.begin_fill()
    Amaya.circle(120,180)
    Amaya.left(90)
    Amaya.forward(240)
    Amaya.end_fill()
    Amaya.color("#ffeace") #Color of the details
    Amaya.left(180)
    Amaya.forward(90)
    Amaya.right(90)
    Amaya.circle(30, 180)
    Amaya.left(180)
    Amaya.left(90)
    Amaya.forward(60)
    Amaya.right(90)
    Amaya.circle(-90,180)
    Amaya.penup()
    Amaya.goto(100, -240)
    Amaya.left(120)
    Amaya.pendown()
    Amaya.forward(63)
    Amaya.penup() 
    Amaya.goto(80, -245)
    Amaya.left(70)
    Amaya.pendown()
    Amaya.forward(63)
    Amaya.penup()
    Amaya.goto(10, -265)
    Amaya.right(140)
    Amaya.pendown()
    Amaya.forward(65)
    
def image(): #This is the function all put together, it will draw the full image
    orange()
    stem()
    leaf()
    Amaya.goto(200, -210)
    slice()
    Amaya.penup()
    Amaya.goto(170,-250)
    Amaya.pendown()
    Amaya.color("orange")
    Amaya.begin_fill()
    for i in range(3): #This is for the triangular orange peel next to the slice
        Amaya.forward(100)
        Amaya.left(120)
    Amaya.end_fill()

image()
 

