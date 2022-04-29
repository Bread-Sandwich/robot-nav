#Explanation of code:
#Starts a run with given parameters when you type run(parameters),
#using defaults if nothing is entered. The program then creates a
#list of 10 simple models for the robot, or loads the from a file.
# The program iterates through the list running each model 10 times
#and giving it a score, which is based on the number of times it
#crosses over itself. The 5 lowest scoring models are removed from
#the list.
# The remaining 5 models each get 2 new models which are slightly
#varied copies of themselves, with their attributes (variables)
#changed by a random amount.
# These new models are then run and the same process is applied however
#many times were specified when you did run(parameters), or 20 times.
#
import turtle
import random
import math as maths
import pickle
import os
import objectDetection as obj
#from PIL import Image
wn = turtle.Screen()
wn.setup(784,788,starty=5)
turtle.delay(5)
#list of possible turtle shapes:
shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
#list of possible turtle colours:
colours = ["alice blue", "aquamarine", "azure", "beige", "bisque", "black", "blanched almond", "blue", "blue violet", "brown", "burlywood", "cadet blue", "chartreuse", "chocolate", "coral", "cornflower blue", "cornsilk", "cyan", "dark blue", "dark cyan", "dark goldenrod", "dark gray", "dark green", "dark grey", "dark khaki", "dark magenta", "dark olive green", "dark orange", "dark orchid", "dark red", "dark salmon", "dark sea green", "dark slate blue", "dark slate grey", "dark turquoise", "dark violet", "deep pink", "deep sky blue", "dim grey", "dodger blue", "firebrick", "forest green", "gainsboro", "gold", "goldenrod", "green", "green yellow", "grey", "honeydew", "hot pink", "indian red", "khaki", "lavender", "lavender blush", "lawn green", "lemon chiffon", "light blue", "light coral", "light cyan", "light goldenrod", "light goldenrod yellow", "light gray", "light green", "light grey", "light pink", "light salmon", "light sea green", "light sky blue", "light slate blue", "light slate grey", "light steel blue", "light yellow", "lime green", "magenta", "maroon", "medium aquamarine", "medium blue", "medium orchid", "medium purple", "medium sea green", "medium slate blue", "medium spring green", "medium turquoise", "medium violet red", "midnight blue", "mint cream", "misty rose", "moccasin", "navy", "navy blue", "old lace", "olive drab", "orange", "orange red", "orchid", "pale goldenrod", "pale green", "pale turquoise", "pale violet red", "papaya whip", "peach puff", "peru", "pink", "plum", "powder blue", "purple", "red", "rosy brown", "royal blue", "saddle brown", "salmon", "sandy brown", "sea green", "seashell", "sienna", "sky blue", "slate blue", "slate grey", "spring green", "steel blue", "tan", "thistle", "tomato", "turquoise", "violet", "violet red", "wheat", "yellow", "yellow green"]
#colours = [(0,1,0)] #This line makes the turtle always green
MUTATIONRATE = 1
#creating the room (square) and the obstacle in it (circle)
square = obj.drawPolygon([(-300, 130), (-300, 289), (299, 289), (299, -289), (-300, -289), (-300, 130), (-235, 129), (-235, -58), (-176, -149), (-86, -149), (-86, -82), (-65, -82), (-65, -150), (-10, -150), (-10, -256), (235, -256), (235, -98), (62, -98), (62, -36), (18, -36), (17, 35), (37, 34), (37, -16), (243, -16), (243, 100), (16, 100), (16, 135), (141, 135), (147, 142), (152, 156), (155, 170), (156, 193), (155, 214), (151, 234), (147, 243), (141, 251), (20, 251), (20, 221), (-65, 221), (-65, -1), (-86, -1), (-86, 222), (-160, 222), (-160, 130), (-235, 130), (-235, 117)])
circle = obj.drawPolygon([(154, -146), (167, -148), (174, -153), (180, -160), (184, -168), (185, -177), (183, -188), (178, -197), (172, -203), (154, -208), (138, -204), (130, -197), (125, -188), (123, -177), (126, -164), (134, -153)])

#=======================================================================================
#   This function is used to check if 2 paths the robot has made cross each other.
def intersect(a,b,c,d):
    #variable name meanings:
    #a - first point of first line
    #b - second point of first line
    #c - first point of second line
    #d - second point of second line
    #dxab/dxcd - change in x of ab / cd
    #mab/mcd - gradient of ab / cd
    #yab/ycd - y intercept of ab / cd
    #gdf = gradient difference (to check if the lines are parallel)
    #xcross, ycross - co-ordinates of lines' intersection
    #b1,l1 - bigger x of line 1, littler x of line 1(ab)
    #b2,l2 - above, but line 2 (cd)
    if a==c or b==c:
        return False
    dxab = b[0]-a[0]
    dxcd = d[0]-c[0]
    if dxab != 0 and dxcd != 0:
        mab = (b[1]-a[1])/dxab
        mcd = (d[1]-c[1])/dxcd
        yab = b[1]-b[0]*mab
        ycd = d[1]-d[0]*mcd
        #ex+f = gx+h, find x
        #ex-gx = h-f
        #x = (h-f)/(e-g), where f,h are intercepts and e,g are gradients
        gdf = mab-mcd
        if gdf != 0:
            xcross = (ycd-yab)/(gdf)
        else:
            return False
        n = xcross
        b1 = max(a[0],b[0])
        b2 = max(c[0],d[0])
        l1 = min(a[0],b[0])
        l2 = min(c[0],d[0])
        if l1 <= n <= b1 and l2 <= n <= b2:
            ycross = mab * xcross + yab
            return (xcross,ycross)
        else:
            return False
    elif dxab == 0:#ab is vertical
        n = a[0]
        b2 = max(c[0],d[0])#bigger of c and d x
        l2 = min(c[0],d[0])#lower of c and d x
        if l2 <= n <= b2:
            dxcd = d[0]-c[0]
            if dxcd == 0:
                return True
            else:
                mcd = (d[1]-c[1])/dxcd
                ycd = d[1] - d[0]*mcd
                xcross = a[0]
                ycross = mcd * xcross + ycd
                return (xcross, ycross)
        else:
            return False
    else:#in this case, cd is vertical and ab is not
        n = c[0]
        b2 = max(a[0],b[0])
        l2 = min(a[0],b[0])
        if l2 <= n <= b2:
            mab = (b[1]-a[1])/dxab
            yab = b[1]-b[0]*mab
            xcross = c[0]
            ycross = mab*xcross+yab
            return (xcross, ycross)
        else:
            return False
#=======================================================================================

def inScreen(x,y):
    #check if position is in screen
    if abs(x) > 390 or abs(y) > 390:
        return False
    else:
        return True

class fastTurtle:
    # Creates a turtle which works the same as python's
    #turtle, but runs faster as it doesn't draw the lines
    #note: attributes have V at the end so they're not confused with functions
    def __init__(self):
        self.posV =(0,0)
        self.headingV = 0
    def right(self,angle):
        #turn right (angle) degrees
        self.headingV = (self.headingV-angle)%360
    def fd(self, distance):
        #move forward (distance)
        x, y = self.posV
        rads = self.headingV * maths.pi/180
        self.posV = (round(x + distance * maths.cos(rads),2),round(y + distance * maths.sin(rads),2))
    def pos(self):
        return self.posV
    def xcor(self):
        return self.posV[0]
    def ycor(self):
        return self.posV[1]
    def distance(self, point):
        #return the distance from the turtle to (point)
        x, y = self.posV
        x2, y2 = point
        return ((x2-x)**2 + (y2-y)**2)**0.5
    def heading(self):
        #return the current angle of the turtle
        return self.headingV
    def clear(self):
        return True

class turtleAlg:
    def __init__(self,moveDist, turnAngle, bounceAngle, distVaried, angleVaried, stepDist, bounceLoss):
        self.moveDist = moveDist
        self.turnAngle = turnAngle
        self.distVaried = distVaried
        self.angleVaried = angleVaried
        self.bounceAngle = bounceAngle
        self.stepDist = stepDist
        self.bounceLoss = bounceLoss
    def __lt__(self, other):
        #allows turtles to be sorted by intersections
        return self.intersections < other.intersections
    def run(self, dummy = True):
        #makes the turtle do a single run until it goes for too long or runs out of charge
        #setting up variables:
        segments = []
        moveDist = self.moveDist
        distVaried = self.distVaried
        turnAngle = self.turnAngle
        angleVaried = self.angleVaried
        bounceAngle = self.bounceAngle
        stepDist = self.stepDist
        bounceLoss = self.bounceLoss
        fuel = 10000
        random.shuffle(colours)
        random.shuffle(shapes)
        if not dummy:
            #creating a real turtle if this is a visible run
            self.tr = turtle.Turtle()
            tr = self.tr
            tr.degrees()
            tr.speed(0)
            tr.pencolor(colours[0])
            tr.shape(shapes[0])
            tr.width(8)
        else:
            #creating a fake turtle if this is a dummy run
            self.tr = fastTurtle()
            tr = self.tr
        self.name = colours[0]
        self.shape = shapes[0]
        steps = 0
        bonusDist = 0
        while fuel > 1 and steps < 2000:
            #deciding distance to travel, then turning
            fdDistance = bonusDist + moveDist + random.uniform(-distVaried,distVaried)
            fdDistance = max(min(fuel,fdDistance),0)
            clockwiseAngle = random.uniform(turnAngle-angleVaried,turnAngle+angleVaried)
            tr.right(clockwiseAngle)
            angle = tr.heading()
            rads = angle * maths.pi / 180
            #finding where the turtle would be after it moves
            newpos = (tr.xcor() + fdDistance * maths.cos(rads),tr.ycor() + fdDistance * maths.sin(rads))
            currentpos = tr.pos()
            if inScreen(newpos[0],newpos[1]) and not square.inObject((currentpos,newpos)) and not circle.inObject((currentpos,newpos)):
                #moving if the path doesn't collide with anything
                fuel -= tr.distance(newpos)
                tr.fd(fdDistance)
                newpos = tr.pos()
                segments.append((currentpos[0], currentpos[1], newpos[0], newpos[1]))
                bonusDist += stepDist
            else:
                squareInt = square.inObject((currentpos,newpos))
                circleInt = circle.inObject((currentpos,newpos))
                if squareInt and not circleInt:
                    #if the turtle hits a wall, find the point at the wall instead
                    if len(squareInt)>1:
                        squareInt.sort(key = lambda x: ((x[0]-currentpos[0])**2 + (x[1]-currentpos[1])**2)**0.5)
                    squareInt = squareInt[0]
                    x = squareInt
                    dist = ((x[0]-currentpos[0])**2 + (x[1]-currentpos[1])**2)**0.5
                    newX = (squareInt[0] * 2 + currentpos[0] * 1)/3
                    newY = (squareInt[1] * 2 + currentpos[1] * 1)/3
                    newpos = (newX, newY)
                elif circleInt:
                    #if the turtle hits the circle, find the point at the circle instead
                    if len(squareInt)>1:
                        circleInt.sort(key = lambda x: ((x[0]-currentpos[0])**2 + (x[1]-currentpos[1])**2)**0.5)
                    circleInt = circleInt[0]
                    x = circleInt
                    dist = ((x[0]-currentpos[0])**2 + (x[1]-currentpos[1])**2)**0.5
                    newX = (circleInt[0] * 2 + currentpos[0] * 1)/3
                    newY = (circleInt[1] * 2 + currentpos[1] * 1)/3
                    newpos = (newX, newY)
                if (squareInt or circleInt) and dist >= 1:
                    #moving to the place the turtle hits
                    fuel -= tr.distance(newpos)
                    tr.fd(tr.distance(newpos))
                    newpos = tr.pos()
                    segments.append((currentpos[0], currentpos[1],newpos[0],newpos[1]))
                tr.right(bounceAngle)
                bonusDist -= bounceLoss
                bonusDist = max(0,bonusDist)
            steps +=1
        self.segments = segments
        self.fuel = fuel

    def ints(self, returnSegs = False):
        #returns the number of times the turtle crossed over its own path
        intersections = 0
        intsegs = []
        segments = self.segments
        l = len(segments)
        for k in range(l):
            s1 = segments[k]
            for j in range(k+1,l):
                s2 = segments[j]
                a = s1[0:2]
                b = s1[2:4]
                c = s2[0:2]
                d = s2[2:4]
                if intersect(a,b,c,d):
                    intersections += 1
                    intsegs.append([a,b,c,d])
        
        intersections += self.fuel
        if returnSegs:
            return intsegs
        else:
            return intersections
    def clear(self):
        #clear everything the turtle drew
        try:
            self.tr.clear()
            return True
        except:
            return False
        
def avginter(array):
    #return the average of numbers in the array
    count = 0
    total = 0
    for i in array:
        ints = i.intersections
        if ints < 5000:
            count += 1
            total += ints
    return total/count

def saveTurtle(turtle):
    #save (turtle) to a file
    with open(f'{turtle.name}.pkl', 'wb') as outp:
        pickle.dump(turtle, outp, pickle.HIGHEST_PROTOCOL)

def importTurtle(filename):
    #loads a turtle from a file
    with open(filename,'rb') as inp:
        saved = pickle.load(inp)
    return saved
#IGNORE THIS FUNCTION
#========================================================================
#def savepng(canvas, fileName):
#    #saves the image as a picture (DOESNT WORK WITHOUT EXTRA STUFF)
#    canvas.postscript(file = 'temp.eps')
#    img = Image.open('temp.eps')
#    img.save('testSave.png')
#========================================================================
turtle.delay(0)
turtles = []
winners = []
generations = 0
def run(turtles = turtles, maxgens = 20, filename=None, mr=1):
    #run (maxgens) generations of turtles, loading turtles from (filename)
    #mutation rate of (mr)
    winners = []
    LI = 1000
    generations = 0
    while LI > 3 and generations < maxgens:
        
        if len(turtles) == 0:
            try:
                #tries to load turtles from file
                with open(filename,'rb') as inp:
                    for i in range(10):
                        turtles.append(pickle.load(inp))
            except:
                #starts with new turtles if it can't load the file
                print('no file found, starting new thing')
                for i in range(10):
                    md = random.uniform(10,50) #move distance
                    ta = random.uniform(5,90) #turn angle
                    dv = random.uniform(5,25) #distance variation
                    av = random.uniform(5,30) #angle variation
                    sd = 0 #move distance increase per step
                    ba = 90 #bounce angle
                    bl = 0 #move distance lost on bounce
                    turtles.append(turtleAlg(md,ta,ba,dv,av,sd,bl))
        for i in turtles:
            #runs each turtle 10 times, saving their intersections
            i.clear()
            totalInts = 0
            for _ in range(10):
                i.run()
                currentInts = round(i.ints())
                totalInts += currentInts
                if currentInts > 3000:
                    currentInts += 10000
                    break
            avgInts = totalInts / 10
            avgInts = round(avgInts)
            i.intersections = avgInts
            print(avgInts)
        turtles.sort()
        LI = turtles[0].intersections
        winners.append(turtles[0])
        #running the best turtle and showing some stats for the generation:
        winners[-1].run(False)
        print(f'best score: {turtles[0].name}')
        print(f'the average score this generation was: {avginter(turtles)}')
        winners[-1].tr.clear()
        winners[-1].tr.hideturtle()
        #removing 5 worst turtles
        while len(turtles) > 5:
            del turtles[5]
        #creating new turtles mutated from remaining turtles
        turtles2 = []
        for i in turtles:
            for _ in range(2):
                md = i.moveDist
                ta = i.turnAngle
                dv = i.distVaried
                av = i.angleVaried
                sd = i.stepDist
                ba = i.bounceAngle
                bl = i.bounceLoss
                md = max(10, md + random.uniform(-5*mr,5*mr))
                ta += random.uniform(-5*mr,5*mr)
                dv += random.uniform(-5*mr,5*mr)
                av += random.uniform(-5*mr,5*mr)
                sd += random.uniform(-0.5*mr,0.5*mr)
                ba += random.uniform(-5*mr,5*mr)
                bl = max(0, bl + random.uniform(-3*mr,3*mr))
                turtles2.append(turtleAlg(md,ta,ba,dv,av,sd, bl))
        #deleting remaning old turtles:
        while len(turtles) > 0:
            del turtles[0]
        #moving new turtles to main list:
        for i in turtles2:
            turtles.append(i)
        #deleting temporary turtle list:
        for i in turtles:
            try:
                turtles2.remove(i)
                #print('removed a turtle from turtles2')
            except:
                print('turtle could not be removed')
        generations +=1
    #after the runs have been complete:
    #saving the turtles to a file:
    try:
        with open(filename,'wb') as outp:
            for i in range(10):
                pickle.dump(turtles[i], outp, pickle.HIGHEST_PROTOCOL)
    except:
        print("couldn't save")
        
        backupno = 1
        
        while os.path.exists('backup' + str(backupno) + '.pkl'):
            backupno +=1
        with open('backup' + str(backupno) + '.pkl','wb') as outp:
            for i in range(10):
                pickle.dump(turtles[i], outp, pickle.HIGHEST_PROTOCOL)
        return 'saved backup as: ' + 'backup' + str(backupno) + '.pkl'
    #deleting turtles so a new run can be started without reloading
    while len(turtles) > 0:
        del turtles[0]
