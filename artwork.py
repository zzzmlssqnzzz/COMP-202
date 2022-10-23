# Melissa Qian
# 261120131
# Assignment 1: Question 1

import turtle

def flower_pattern(flower_length, flower_angle):
    """(int, int) --> NoneType
    Displays a flower pattern
    """
    flower_length = int(flower_length)
    flower_angle = int(flower_angle)
    
    flower = turtle.Turtle()
    flower.penup()
    flower.goto(50,-50)
    flower.pendown()
    flower.pensize(2)
    flower.speed("fastest")
    flower.color("mediumaquamarine")
    
    radius = flower_length
    for i in range(10):
        for x in range(5):
            flower.circle(radius)
            flower.right(flower_angle)
        radius = radius + 2
        
    flower.hideturtle()

def ice_cream():
    """ () -> NoneType
    Displays an ice cream cone
    """
    icecream = turtle.Turtle()
    icecream.speed(0)
    icecream.pensize(10)

    icecream.penup()
    icecream.goto(-200, 150)
    icecream.pendown()
    icecream.color("plum", "saddlebrown")
    icecream.begin_fill()
    icecream.circle(78)
    icecream.end_fill()

    icecream.penup()
    icecream.goto(-250, 100)
    icecream.pendown()
    icecream.fillcolor("pink")
    icecream.begin_fill()
    icecream.circle(65)
    icecream.end_fill()

    icecream.penup()
    icecream.goto(-150, 100)
    icecream.pendown()
    icecream.fillcolor("seashell")  
    icecream.begin_fill()
    icecream.circle(65)
    icecream.end_fill()

    icecream.penup()
    icecream.goto(-100, 125)
    icecream.pendown()
    icecream.fillcolor("peru")
    icecream.begin_fill()
    for i in range(3):
        icecream.right(120)
        icecream.forward(200)
    icecream.end_fill()
    
    icecream.hideturtle()

def exo_logo():
    """ () -> NoneType
    Displays the logo of K-Pop group Exo
    """
    exo = turtle.Turtle()
    exo.speed(0)
    exo.pensize(10)
        
    exo.penup()
    exo.goto(200, 100)
    exo.pendown()
    exo.color("lightgreen","deeppink")
    exo.begin_fill()
    for i in range(6):
        exo.forward(100)
        exo.left(60)   
    exo.end_fill()

    exo.penup()
    exo.goto(300, 100)
    exo.pendown()
    exo.left(120)
    exo.forward(195)
    exo.right(120)
    exo.forward(100)
    exo.right(120)
    exo.forward(195)
        
    exo.penup()
    exo.goto(200,185)
    exo.pendown()
    exo.right(60)
    exo.forward(50)
    
    exo.hideturtle()

def signature():
    """ () -> NoneType
    Displays a letter M
    """
    letter = turtle.Turtle()
    letter.speed(0)
    letter.pensize(10)
    letter.color("lightskyblue")
    letter.penup()
    letter.goto(-250,-200)
    letter.pendown()

    for i in range(2):
        letter.left(90)
        letter.forward(50)
        letter.right(120)
        letter.forward(50)
        
    letter.hideturtle()

def my_artwork():
    """ () -> NoneType
    Displays artwork
    """
    flower_pattern(50, 80)
    ice_cream()
    exo_logo()
    signature()

    
        
    
    
        
        
       
    
   


    
    
    
    
    









    
    
    
    
    
        
        
    
