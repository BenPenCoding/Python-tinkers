from turtle import *

colours = ["black","red","green","hot pink","blue","yellow"]

def drawAxis():
    t = Turtle()
    maxSize = 1000
    t.speed(0)
    t.pensize(3)
    for i in range(2):
        for i in range(10):
            t.forward(50)
            t.right(90)
            t.forward(3)
            t.up()
            t.backward(5)
            t.write(i+1, False, font=("Verdana",15, "normal"))
            t.forward(5)
            t.down()
            t.right(180)
            t.forward(6)
            t.right(180)
            t.forward(3)
            t.left(90)
        
        t.up()
        t.setpos(0,0)
        t.down()
        t.right(90)
        
        
    for i in range(2):
        for i in range(10):
            t.forward(50)
            t.right(90)
            t.forward(3)
            t.up()
            t.forward(5)
            t.write(i+1, False, font=("Verdana",15, "normal"))
            t.backward(5)
            t.down()
            t.right(180)
            t.forward(6)
            t.right(180)
            t.forward(3)
            t.left(90)
        t.up()
        t.setpos(0,0)
        t.down()
        t.right(90)
    t.ht()
    
def getPolynomialType():
    while True:
        
        try:
            highestOrder = int(input("Please enter the highest order of your polynomial: "))
            break
        
        except:
            print("\nThat was not a valid integer.\n")
    
    return highestOrder

def getPolynomialCoefficient(order):
    
    while True:
        
        try:
            coefficient = float(input(f"Please enter the coefficient of x^{order}: "))
            print(coefficient)
            break
        
        except:
            print("\nThat was not a valid integer.\n")
    
    return coefficient

def getPolynomial():
    
    highestOrder = getPolynomialType()
    polynomial = []
    
    for i in range(highestOrder,-1,-1):
        
        polynomial.append(getPolynomialCoefficient(i))
    

    
    return polynomial

def drawPolynomial(colour):
    polynomial = getPolynomial()
    t = Turtle()
    t.color(colour)
    t.speed(0)
    t.pensize(3)
    t.up()
    t.down()
    x = -500

    y = 0
    for i in range(len(polynomial)-1,0,-1):
        
        y += (50*(polynomial[(len(polynomial)-1)-i] * (x/50)) ** i)
    y += polynomial[-1]*50
    t.up() 
    
    t.setpos(x,y)
    t.down()
    x+=1

    for i in range(500):
        
        
        y = 0
        for i in range(len(polynomial)-1,0,-1):
            
            y += (50*(polynomial[(len(polynomial)-1)-i] * (x/50)) ** i)
        
        y += polynomial[-1]*50
        
        t.setpos(x,y)
        
        x+=2
        
#MAIN 
drawAxis()
for i in range(5):
    drawPolynomial(colours[i])
    if i < 4:
        userInput = str(input("Type 'more' to add another graph: ")).upper()
    else:
        break
    if userInput != "MORE":
        break
    
    
