import turtle, random
fuel = 10000
n = 570
p = 15
l = 0
startingplace = random.randint(-285,285)
screen = turtle.Screen()
screen.bgcolor('white')
screen.setup(width=600, height=600)

robot = turtle.Turtle()
robot.speed(15)
robot.shape('circle')
robot.color('orange')

robot.width(30)
robot.color('white')
robot.goto(-285,startingplace)
robot.color('blue')
robot.goto(-285,285)
fuel -= robot.distance(-285,startingplace)
l += robot.distance(-285,startingplace)
robot.color('orange')

for i in range (1, 40):
    robot.forward (n-15*i)
    l += (n-15*i)
    fuel -= n-15*i
    robot.right(90)
    if fuel < 900:
        r = robot.pos()
        spiralstorage = i
        break
print(robot.pos())


robot.color('red')
robot.goto(-285, startingplace)
l+= robot.distance(r)

print(l)
robot.goto(r)
robot.color('purple')
robot.width(30)

for i in range (spiralstorage, 40):
    robot.forward (n- 15*i)
    l += (n-15*i)
    robot.right(90)
print(robot.pos())
r = robot.pos()

robot.color('black')
robot.goto(-285, startingplace)
