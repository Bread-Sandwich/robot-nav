import turtle, random, sys, math

fuel = 10000
size = random.randint(15,30)
size2 = random.randint(15,20)
leftboundary = 15-size*15
topboundary = 15-size2*15
wide = size*30-30
length = size2*30-30
l = 0

room = turtle.Turtle()
room.color('white')
room.speed(20)
room.goto(leftboundary-15,-topboundary+15)
room.width(10)
room.color('black')
for i in range(2):
    room.forward(wide+15)
    room.right(90)
    room.forward(length+15)
    room.right(90)


def fuelcolor(fuel):
    output = (1-(fuel/10000),fuel/10000,0)
    return output

def avoidBlockade(spiralstorage,l,fuel,r):
    robot.right(90)
    robot.forward(blockwidth*2)
    fuel -= blockwidth*2
    if fuel < 2*robot.distance(leftboundary, startingplace):
        r = robot.pos()
        spiralstorage,l,fuel,r = chargingAvoid(spiralstorage,l,fuel,r)
    robot.left(90)
    robot.forward(blockwidth+33)
    fuel -= blockwidth+33
    if fuel < 2*robot.distance(leftboundary, startingplace):
        r = robot.pos()
        spiralstorage,l,fuel,r = chargingAvoid(spiralstorage,l,fuel,r)
    robot.left(90)
    robot.forward(blockwidth*4)
    fuel -= blockwidth*4
    if fuel < 2*robot.distance(leftboundary, startingplace):
        r = robot.pos()
        spiralstorage,l,fuel,r = chargingAvoid(spiralstorage,l,fuel,r)
    robot.left(90)
    robot.forward(blockwidth+33)
    fuel -= blockwidth+33
    if fuel < 2*robot.distance(leftboundary, startingplace):
        r = robot.pos()
        spiralstorage,l,fuel,r = chargingAvoid(spiralstorage,l,fuel,r)
    robot.left(90)
    robot.forward(blockwidth*4)
    fuel -= blockwidth*4
    if fuel < 2*robot.distance(leftboundary, startingplace):
        r = robot.pos()
        spiralstorage,l,fuel,r = chargingAvoid(spiralstorage,l,fuel,r)
    robot.left(90)
    robot.forward(blockwidth+33)
    fuel -= blockwidth+33
    if fuel < 2*robot.distance(leftboundary, startingplace):
        r = robot.pos()
        spiralstorage,l,fuel,r = chargingAvoid(spiralstorage,l,fuel,r)
    robot.left(90)
    robot.forward(blockwidth*2)
    fuel -= blockwidth*2
    if fuel < 2*robot.distance(leftboundary, startingplace):
        r = robot.pos()
        spiralstorage,l,fuel,r = chargingAvoid(spiralstorage,l,fuel,r)
    robot.right(90)
    return int((blockwidth+33)/2)

def spiraling(spiralstorage,l,fuel,r):
    for i in range(spiralstorage, 999):
        if robot.heading() == 0 or robot.heading() == 180:
            if wide-15*i*2 <= 0 and length-15*i*2 <= 0:
                end(spiralstorage,l,fuel,r)
            j = int((wide-15*i*2)/2)
            objdone = 0
            while j > 0:
                robot.forward(2)
                l += 2
                fuel -= 2
                j -= 1
                if math.fabs(robot.xcor()-blockade.xcor()) < (blockwidth/2)+18 and math.fabs(robot.ycor()-blockade.ycor()) < (blockwidth/2)+18 and objdone == 0:
                    j -= avoidBlockade(spiralstorage,l,fuel,r)
                    objdone = 1
            robot.right(90)
            robot.color(fuelcolor(fuel))
            if fuel < 2*robot.distance(leftboundary, startingplace):
                r = robot.pos()
                spiralstorage = i
                spiralstorage,l,fuel,r = charging(spiralstorage,l,fuel,r)
        if robot.heading() == 90 or robot.heading() == 270:
            if wide-15*i*2 <= 0 and length-15*i*2 <= 0:
                end(spiralstorage,l,fuel,r)
            j = int((length-15*i*2)/2)
            while j > 0:
                robot.forward(2)
                l += 2
                fuel -= 2
                j -= 1
                if math.fabs(robot.xcor()-blockade.xcor()) < (blockwidth/2)+18 and math.fabs(robot.ycor()-blockade.ycor()) < (blockwidth/2)+18 and objdone == 0:
                    j -= avoidBlockade(spiralstorage,l,fuel,r)
                    objdone = 1
            robot.right(90)
            robot.color(fuelcolor(fuel))
            if fuel < 2*robot.distance(leftboundary, startingplace):
                r = robot.pos()
                spiralstorage = i
                spiralstorage,l,fuel,r = charging(spiralstorage,l,fuel,r)
            
def charging(spiralstorage,l,fuel,r):
    robot.color(fuelcolor(fuel))
    robot.goto(leftboundary, startingplace)
    l += robot.distance(r)
    fuel = 10000
    robot.color(fuelcolor(fuel))
    robot.goto(r)
    l += robot.distance(leftboundary, startingplace)
    fuel -= robot.distance(leftboundary, startingplace)
    return spiraling(spiralstorage,l,fuel,r)

def chargingAvoid(spiralstorage,l,fuel,r):
    robot.color(fuelcolor(fuel))
    robot.goto(leftboundary, startingplace)
    l += robot.distance(r)
    fuel = 10000
    robot.color(fuelcolor(fuel))
    robot.goto(r)
    l += robot.distance(leftboundary, startingplace)
    fuel -= robot.distance(leftboundary, startingplace)
    return spiralstorage,l,fuel,r

def end(spiralstorage,l,fuel,r):
    robot.color(fuelcolor(fuel))
    robot.goto(leftboundary, startingplace)
    sys.exit()

startingplace = random.randint(topboundary,-topboundary)
screen = turtle.Screen()
screen.bgcolor('white')
screen.setup(width=size*30+10, height=size2*30+10)

robot = turtle.Turtle()
robot.speed(9999)
robot.shape('circle')
robot.color(fuelcolor(fuel))

robot.width(30)
robot.color('white')
robot.goto(leftboundary,startingplace)
robot.color(fuelcolor(fuel))
robot.goto(leftboundary,-topboundary)
fuel -= robot.distance(leftboundary,startingplace)
l += robot.distance(leftboundary,startingplace)
robot.color(fuelcolor(fuel))
spiralstorage = 1
r = 0


listofblock = []
for i in range(1):
    blockade = turtle.Turtle()
    blockade.shape('circle')
    blockade.penup()
    blockade.color('black')
    blockwidth = random.randint(20,50)
    blockade.width(blockwidth)
    blockX = random.randint(leftboundary+100,-leftboundary-100)
    blockY = random.randint(topboundary+100,-100-topboundary)
    blockade.goto(blockX,blockY)
    blockade.pendown()
    listofblock.append(blockade.pos())


line=turtle.Turtle()
line.penup()
line.width(2)
line.goto(blockX-int(blockwidth/2),blockY-int(blockwidth/2))
line.pendown()
line.goto(blockX-int(blockwidth/2),blockY+int(blockwidth/2))
line.goto(blockX+int(blockwidth/2),blockY+int(blockwidth/2))
line.goto(blockX+int(blockwidth/2),blockY-int(blockwidth/2))
line.goto(blockX-int(blockwidth/2),blockY-int(blockwidth/2))


def spiralingstart(spiralstorage,l,fuel,r):
    robot.color(fuelcolor(fuel))
    robot.goto(leftboundary,-topboundary)
    fuel -= robot.distance(leftboundary,startingplace)
    l += robot.distance(leftboundary,startingplace)
    robot.color(fuelcolor(fuel))
    for i in range (1, 3):
        robot.color(fuelcolor(fuel))
        robot.forward(wide-15)
        l += wide-15
        fuel -= wide-15
        robot.right(90)
        robot.color(fuelcolor(fuel))
        robot.forward(length-15)
        l += length-15
        fuel -= length-15
        robot.right(90)

robot.heading()
spiralingstart(spiralstorage,l,fuel,r)
spiraling(spiralstorage,l,fuel,r)
