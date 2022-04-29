import turtle, random, sys

fuel = 10000
size = random.randint(15,30)
size2 = random.randint(15,30)
leftboundary = 15-size*15
wide = size*30-30
length = size2*30-30
l = 0

def fuelcolor(fuel):
    output = (1-(fuel/10000),fuel/10000,0)
    return output

def spiraling(spiralstorage,l,fuel,r):
    for i in range (spiralstorage, 999):
        if wide-15*i <= 0:
            end(spiralstorage,l,fuel,r)
        robot.forward(wide-15*i)
        l += wide-15*i
        fuel -= wide-15*i
        robot.color(fuelcolor(fuel))
        robot.right(90)
        if fuel < 2*robot.distance(leftboundary, startingplace):
            r = robot.pos()
            spiralstorage = i
            charging(spiralstorage,l,fuel,r)
            
def charging(spiralstorage,l,fuel,r):
    robot.color(fuelcolor(fuel))
    robot.goto(leftboundary, startingplace)
    l += robot.distance(r)
    fuel = 10000
    robot.color(fuelcolor(fuel))
    robot.goto(r)
    l += robot.distance(leftboundary, startingplace)
    fuel -= robot.distance(leftboundary, startingplace)
    spiraling(spiralstorage,l,fuel,r)

def end(spiralstorage,l,fuel,r):
    robot.color(fuelcolor(fuel))
    robot.goto(leftboundary, startingplace)
    sys.exit()

startingplace = random.randint(leftboundary,-leftboundary)
screen = turtle.Screen()
screen.bgcolor('white')
screen.setup(width=size*30, height=size*30)

robot = turtle.Turtle()
robot.speed(10)
robot.shape('circle')
robot.color(fuelcolor(fuel))

robot.width(30)
robot.color('white')
robot.goto(leftboundary,startingplace)
robot.color(fuelcolor(fuel))
robot.goto(leftboundary,-leftboundary)
fuel -= robot.distance(leftboundary,startingplace)
l += robot.distance(leftboundary,startingplace)
robot.color(fuelcolor(fuel))
spiralstorage = 1
r = 0
 
def spiralingstart(spiralstorage,l,fuel,r):
    for i in range (1, 4):
        robot.forward(wide-15)
        l += wide-15
        fuel -= wide-15
        robot.right(90)

spiralingstart(spiralstorage,l,fuel,r)
spiraling(spiralstorage,l,fuel,r)
