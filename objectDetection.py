import turtle

def intersects(line1,line2):
    ax1, ay1 = line1[0] #a1 is the first point of line1
    bx1, by1 = line1[1] #b1 is the second point of line1
    ax2, ay2 = line2[0] #a2 is the first point of line2
    bx2, by2 = line2[1] #b2 is the second point of line2
    xdist1 = bx1-ax1 #change in x line1
    ydist1 = by1-ay1 #change in y line1
    xdist2 = bx2-ax2 #change in x line2
    ydist2 = by2-ay2 #change in y line2
    xMin1 = min(ax1,bx1) #sorting the points by their x co-ordinates
    xMax1 = max(ax1,bx1)
    xMin2 = min(ax2,bx2)
    xMax2 = max(ax2,bx2)
    if xdist1 == 0 and xdist2 == 0:
        return False
    elif xdist1 == 0: #if the first line is a vertical line
        xcross = ax1
        grad2 = ydist2/xdist2 #gradient of line2
        int2 = ay2-grad2*ax2 #y intercept of line2
        yMin1 = min(ay1,by1)
        yMax1 = max(ay1,by1)
        ycross = ax1*grad2+int2 #the y position of the crossing point
        if yMin1 <= ycross <= yMax1 and xMin2 <= xcross <= xMax2: #if the lines cross somewhere in the segment
            return (xcross, ycross)
        else:
            return False
        
    elif xdist2 == 0: #if the second line is a vertical line
        xcross = ax2
        grad1 = ydist1/xdist1
        int1 = ay1 - grad1*ax1
        yMin2 = min(ay2,by2)
        yMax2 = max(ay2,by2)
        ycross = ax2*grad1+int1
        if yMin2 <= ycross <= yMax2 and xMin1 <= xcross <= xMax1: #if the lines cross somewhere in the segment
            return (xcross, ycross)
        else:
            return False
    else: #if neither are vertical
        grad1 = ydist1/xdist1 #gradient of line1
        grad2 = ydist2/xdist2 #gradient of line2
        int1 = ay1-grad1*ax1 #y intercept of line1
        int2 = ay2-grad2*ax2 #y intercept of line2
        #ax+b=cx+d       a = grad1 b=int1,        c=grad2,     d=int2
        #(a-c)x=d-b
        #x=(d-b)/(a-c)
        if grad2 != grad1: #if lines intersect at some point
            xcross = (int2-int1)/(grad1-grad2) #the x co-ordinate where the lines cross
            xMin1 = min(ax1,bx1)
            xMax1 = max(ax1,bx1)
            xMin2 = min(ax2,bx2)
            xMax2 = max(ax2,bx2)
            if xMin1 <= xcross <= xMax1 and xMin2 <= xcross <= xMax2: #if the lines cross somewhere in the segment
                ycross = grad1*xcross + int1
                return (xcross, ycross)
            else:
                return False
        elif int1 != int2: # if lines are parallel
            return False
        else: #if lines are the same line
            if min(ax2,bx2) <= min(ax1,bx1) <= max(ax2,bx2) or min(ax2,bx2) <= max(ax1,bx1) <= max(ax2,bx2):
                return True
            return False

class obstacle:
    def __init__(self, vertices):
        self.lines = [[vertices[i], vertices[i+1]] for i in range(len(vertices)-1)]
        self.lines.append([vertices[-1],vertices[0]])
        self.vertices = vertices
        print(self.lines)
        
    def inObject(self, line):#((a,b),(c,d))
        intersections = []
        for edge in self.lines:
            if intersects(edge,line):
                intersections.append(intersects(edge,line))
        return intersections

    def draw(self):
        self.tr = turtle.Turtle()
        tr = self.tr
        tr.penup()
        tr.speed(0)
        vertices = self.vertices
        tr.goto(vertices[-1])
        tr.pendown()
        tr.begin_fill()
        for v in vertices:
            tr.goto(v)
        tr.end_fill()
        tr.hideturtle()
        del tr

    def clear(self):
        self.tr.clear()
        self.tr.hideturtle()
        del self.tr
    

def drawSquare(topLeft, sideLength):
    x = topLeft[0]
    y = topLeft[1]
    v1 = (x,y)
    v2 = (x+sideLength,y)
    v3 = (x+sideLength,y-sideLength)
    v4 = (x,y-sideLength)
    square = obstacle([v1,v2,v3,v4])
    square.draw()
    return square

def drawPolygon(vertices):
    polygon = obstacle(vertices)
    polygon.draw()
    return polygon
