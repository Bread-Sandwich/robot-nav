import objectDetection as obj
import turtle
import math
from PIL import Image

PixelsPerSquare = 4
IMAGENAME = "imageScaled2.png"

#wall = obj.drawPolygon([(-300, 130), (-300, 289), (299, 289), (299, -289), (-300, -289), (-300, 130), (-235, 129), (-235, -58), (-176, -149), (-86, -149), (-86, -82), (-65, -82), (-65, -150), (-10, -150), (-10, -256), (235, -256), (235, -98), (62, -98), (62, -36), (18, -36), (17, 35), (37, 34), (37, -16), (243, -16), (243, 100), (16, 100), (16, 135), (141, 135), (147, 142), (152, 156), (155, 170), (156, 193), (155, 214), (151, 234), (147, 243), (141, 251), (20, 251), (20, 221), (-65, 221), (-65, -1), (-86, -1), (-86, 222), (-160, 222), (-160, 130), (-235, 130), (-235, 117)])
#circle = obj.drawPolygon([(154, -146), (167, -148), (174, -153), (180, -160), (184, -168), (185, -177), (183, -188), (178, -197), (172, -203), (154, -208), (138, -204), (130, -197), (125, -188), (123, -177), (126, -164), (134, -153)])

def inRoom(point):
    checks = []
    for x in range(8):
        for y in range(8):
            checks.append(len(getCollisionsToPoint((x-4,y-4),point))%2 == 0)
    if sum(checks) >= len(checks)*0.85:
        return True
    else:
        return False

def getCollisionsToPoint(point1,point2):
        line = (point1, point2)
        wallCollisions = wall.inObject(line)
        circleCollisions = circle.inObject(line)
        return wallCollisions + circleCollisions

def indexToCoord(grid,row,col):
    totalCols = len(grid[0])
    totalRows = len(grid)
    return ((col-int(totalCols/2))*PixelsPerSquare + PixelsPerSquare/2,(row-int(totalRows/2))*-1*PixelsPerSquare - PixelsPerSquare/2)
def coordToIndex(grid,x,y):
    totalCols = len(grid[0])
    totalRows = len(grid)
    row = y//(-1*PixelsPerSquare) + int(totalRows/2)
    col = x//PixelsPerSquare + int(totalCols/2)
    return (row,col)
def createGrid():
    grid = []
    shapes = {True: " ", False: "#"}
    for row in range(56):
        grid.append([])
    for row in range(56):
        for col in range(59):
            grid[row].append(shapes[inRoom(indexToCoord(row,col))])
    return grid
    
def printGrid(grid):
    printstr = ""
    
    for Row in range(len(grid)):
        if Row >= 10:
            printstr+= f"{Row} "
        else:
            printstr+= f"{Row}  "
        for Col in range(len(Grid[Row])):
            printstr+= grid[Row][Col]
        
            
    """
    printstr = ""
    for row in range(56):
        if row >= 10:
            printstr+= f"{row} "
        else:
            printstr+= f"{row}  "
        for col in range(59):
            printstr += grid[row][col]*2
        printstr+="\n"
    print(printstr)
    """

def LoadImage():
    FileIn = Image.open(IMAGENAME)
    Width, Height = FileIn.size
    ImageData = list(FileIn.getdata())
    Grid = []
    for Row in range(Height):
        Grid.append([])
        for Col in range(Width):
            Grid[-1].append(" ")
    NextChar = 0
    for Row in range(Height):
        for Column in range(Width):
            Grid[Row][Column] = (" " if ImageData[NextChar] > 0.5 else("█"))
            NextChar += 1
    return Grid, Width, Height

#print("\n".join("".join(grid[ThisRow][ThisColumn] for ThisColumn in range(600))for ThisRow in range(579)))

def getSquare(grid,col,row,length=5):
    square = []
    math.ceil(len(grid)/length)
    missingRows = -1*(len(grid)-1 - (row*length+length))
    if missingRows > 0:
        noRows = length-missingRows
    else:
        noRows = length
    missingCols = -1*(len(grid[0])-1 - (col*length+length))
    if missingCols > 0:
        noCols = length-missingCols
    else:
        noCols = length
    for gridRow in grid[row*length:row*length+noRows]:
        square.append(gridRow[col*length:col*length+noCols])
    return square

def smallGrid(grid,size,width,height):
    squares = []
    for row in range(math.ceil(height/size)):
        currentRow = []
        for col in range(math.ceil(width/size)):
            currentSquare = getSquare(grid,col,row,size)
            for i,v in enumerate(currentSquare):
                currentSquare[i] = ("█" if v.count("█") else(" "))
            currentSquare = ("█" if currentSquare.count("█") else(" "))
            currentRow.append(currentSquare)
        squares.append(currentRow)
    return squares

def printGrid(grid):
    rows = len(grid)
    cols = len(grid[0])
    printstr = ""
    for row in range(rows):
        for col in range(cols):
            printstr+=grid[row][col]*2
        printstr+="\n"
    print(printstr)





def findMove(grid,row,col,here=False):
    maxrow = len(grid)-1
    maxcol = len(grid[0])-1
    first = False
    if row > 0 and grid[row-1][col] in " @":
        if here:
            grid[row-1][col] = "@"
        first = first or "N"
    if col + 1 <= maxcol and grid[row][col+1] in " @":
        if here:
            grid[row][col+1] = "@"
        first = first or "E"
    if col > 0 and grid[row][col-1] in " @":
        if here:
            grid[row][col-1] = "@"
        first = first or "W"
    if row + 1 <= maxrow and grid[row+1][col] in " @":
        if here:
            grid[row+1][col] = "@"
        first = first or "S"
    return first

def isEmpty(grid,row,col):
    maxrow = len(grid)-1
    maxcol = len(grid[0])-1
    if row >= 0 and row <= maxrow and col >= 0 and col <= maxcol and grid[row][col] in " @":
        return True
    return False

def isSeen(grid,row,col):
    maxrow = len(grid)-1
    maxcol = len(grid[0])-1
    if row >= 0 and row <= maxrow and col >= 0 and col <= maxcol and grid[row][col] == "@":
        return True
    return False

def findNearestEmpty(grid,row,col):
    nearestIndex = None
    for searchradius in range(max(len(grid),len(grid[0]))):
        for xdist in range(searchradius):
            ydist = searchradius - xdist
            currentpos = (row,col)
            if isSeen(grid, row+ydist,col+xdist):
                nearestIndex = (row+ydist,col+xdist)
                if not pathToPoint(grid,passedPoints,currentpos,(row+ydist,col+xdist)):
                    nearestIndex = None
            if nearestIndex == None and isSeen(grid, row-ydist,col+xdist):
                nearestIndex = (row-ydist,col+xdist)
                if not pathToPoint(grid,passedPoints,currentpos,(row-ydist,col+xdist)):
                    nearestIndex = None
            if nearestIndex == None and isSeen(grid, row+ydist,col-xdist):
                nearestIndex = (row+ydist,col-xdist)
                if not pathToPoint(grid,passedPoints,currentpos,(row+ydist,col-xdist)):
                    nearestIndex = None
            if nearestIndex == None and isSeen(grid, row-ydist,col-xdist):
                nearestIndex = (row-ydist,col-xdist)
                if not pathToPoint(grid,passedPoints,currentpos,(row-ydist,col-xdist)):
                    nearestIndex = None
            if nearestIndex:
                break
        if nearestIndex:
            break
    return nearestIndex
"""
def findNearestEmptyOld(grid,row,col,passedPoints = []):
    nearestIndex = None
    for searchradius in range(max(len(grid),len(grid[0]))):
        for xdist in range(searchradius):
            ydist = searchradius - xdist
            currentpos = indexToCoord(grid,row,col)
            if isEmpty(grid, row+ydist,col+xdist):
                nearestIndex = (row+ydist,col+xdist)
            if not pathToPoint(passedPoints,currentpos,indexToCoord(grid,row+ydist,col+xdist)):
                nearestIndex = None
            if nearestIndex == None and isEmpty(grid, row-ydist,col+xdist):
                nearestIndex = (row-ydist,col+xdist)
            if not pathToPoint(passedPoints,currentpos,indexToCoord(grid,row-ydist,col+xdist)):
                nearestIndex = None
            if nearestIndex == None and isEmpty(grid, row+ydist,col-xdist):
                nearestIndex = (row+ydist,col-xdist)
            if not pathToPoint(passedPoints,currentpos,indexToCoord(grid,row+ydist,col-xdist)):
                nearestIndex = None
            if nearestIndex == None and isEmpty(grid, row-ydist,col-xdist):
                nearestIndex = (row-ydist,col-xdist)
            if not pathToPoint(passedPoints,currentpos,indexToCoord(grid,row-ydist,col-xdist)):
                nearestIndex = None
            if nearestIndex:
                break
        if nearestIndex:
            break
    return nearestIndex
"""
            


def getCollisionsToPoint(point1, point2):
        line = (point1, point2)
        wallCollisions = wall.inObject(line)
        circleCollisions = circle.inObject(line)
        return wallCollisions + circleCollisions

def lineCollides(grid,start,end):
    startCoord = indexToCoord(grid,start[0],start[1])
    endCoord = indexToCoord(grid,end[0],end[1])
    x1, y1 = startCoord
    x2, y2 = endCoord
    for step in range(100):
        pointx = x1 + (x2-x1)*step/99
        pointy = y1 + (y2-y1)*step/99
        gridSquare = coordToIndex(grid,pointx,pointy)
        gridSquare = (round(gridSquare[0]), round(gridSquare[1]))
        if grid[gridSquare[0]][gridSquare[1]] in "█ ":
            return True
    return False

def pathToPoint(grid,passedPoints,start,end):
    robotPos = start
    path = [end]
    while lineCollides(grid,start,path[0]):
        for point in passedPoints[::-1]:
            if not lineCollides(grid,point,path[0]):
                nextpoint = point
                break
        try:
            nextpoint
        except:
            return None
        if nextpoint == path[-1]:
            return None
        path = [nextpoint] + path
    path.append(end)
    return path

def getColour(fuel,limit=9000):
    if fuel >limit/2:
        g=1
        r = (1 - fuel/limit)*2
        b=0
        return (r,g,b)
    else:
        g = fuel*2/limit
        r=1
        b=0
        return (r,g,b)

grid,width,height = LoadImage()
grid = smallGrid(grid,PixelsPerSquare,width,height)
start = (0,0)
found = False
for irow, row in enumerate(grid):
    for icol, col in enumerate(row):
        if col == " ":
            start = (irow,icol)
            found = True
            break
    if found:
        break
current=start
grid[current[0]][current[1]] = "▒"
move = "N"
moveturtle = turtle.Turtle()
turtle.delay(0)
turtle.bgpic(IMAGENAME)
moveturtle.speed(0)
moveturtle.penup()
moveturtle.goto(indexToCoord(grid,current[0],current[1]))
moveturtle.pendown()
moveturtle.width(15)
moveturtle.color('grey')
fuel=9000
buffer=1000


#FIX BUFFER



passedPoints = []
while (move or findNearestEmpty(grid,current[0],current[1])) and buffer > 0:
    moveturtle.color(getColour(fuel))
    passedPoints.append(current)
    grid[current[0]][current[1]] = "▒"
    fuel -= moveturtle.distance(indexToCoord(grid,current[0],current[1]))
    moveturtle.goto(indexToCoord(grid,current[0],current[1]))
    if fuel < 0:
        buffer += fuel
        fuel = 0
        chargerpos = start
        for point in pathToPoint(grid,passedPoints, passedPoints[-1], chargerpos):
            passedPoints.append(point)
            fuel -= moveturtle.distance(indexToCoord(grid,point[0],point[1]))
            moveturtle.goto(indexToCoord(grid,point[0],point[1]))
        fuel = 9000
        buffer = 1000
        moveturtle.color(getColour(fuel))
        for point in pathToPoint(grid,passedPoints, passedPoints[-1], current):
            passedPoints.append(point)
            fuel -= moveturtle.distance(indexToCoord(grid,point[0],point[1]))
            moveturtle.goto(indexToCoord(grid,point[0],point[1]))
    move = findMove(grid,current[0],current[1],True)
    if not move:
        row,col = findNearestEmpty(grid,current[0],current[1])
        grid[row][col] = "▒"
        moveturtle.color(getColour(fuel))
        for point in pathToPoint(grid,passedPoints, passedPoints[-1], (row,col)):
            passedPoints.append(point)
            fuel -= moveturtle.distance(indexToCoord(grid,point[0],point[1]))
            moveturtle.goto(indexToCoord(grid,point[0],point[1]))
        current = (row,col)
        moveturtle.color(getColour(fuel))
    move = findMove(grid,current[0],current[1],True)
    if move == "N":
        current = (current[0]-1, current[1])
    elif move == "E":
        current = (current[0], current[1]+1)
    elif move == "S":
        current = (current[0]+1, current[1])
    elif move == "W":
        current = (current[0], current[1]-1)
    
printGrid(grid)
