# Tanner Mahofski     tzm5490
#Cole Schutzman       cms7721
import math

def getInput():
    numOfLines = int(input())
    a = []
    b = []
    for i in range(0,numOfLines):
        ins = raw_input().split(" ")
        a.append(ins[0])
        b.append(ins[1])

    return a, b

def getPoints(a, b):
    points = []
    for i in range(0, len(a)):
        p = Point(float(a[i]), -float(b[i]))
        points.append(p)
    return points

def calculateSmallestY(P):
    minY = None
    counter = 0
    for i in range(0, len(P)):
        if(i == 0):
            minY = P[i].getY()
            counter = i
        else:
            if(minY > P[i].getY()):
                minY = P[i].getY()
                counter = i
            elif(minY == P[i].getY()):
                if(P[counter].getX() > P[i].getX()):
                    minY = P[i].getY()
                    counter = i

    return(P[counter])

def calcSlope(p1, p2):
    deltaX = p2.getX() - p1.getX()
    deltaY = p2.getY() - p1.getY()
    return deltaX, deltaY

def getAngles(P, origin):
    angles = []
    for i in range(0, len(P)):
        if(((P[i].getX() != origin.getX()) and (P[i].getY() != origin.getY()))):
            x, y = calcSlope(origin, P[i])
            angle = math.atan2(y, x)
            angles.append(angle)
    return angles

def sortPoints(P, origin, angles):
    sortedPoints = []
    for i in range(0, len(angles)):
        for j in range(0, len(P)):
            x, y = calcSlope(origin, P[j])
            angle = math.atan2(y, x)
            if(angle == angles[i]):
                sortedPoints.append(P[j])
                break

    return sortedPoints

def popAdd(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(b)
    stack.append(a)
    return a, b

def getVector(pa, pb, pk):
    v1X = pa.getX()-pb.getX()
    v1Y = pa.getY()-pb.getY()
    v2X = pk.getX()-pa.getX()
    v2Y = pk.getY()-pa.getY()
    calc = (v1X * v2Y) - (v2X * v1Y)
    if(calc > 0):
        return 1
    elif(calc < 0 ):
        return 2
    else:
        return 0

def grahamScanCore(sortedPoints):
    stack = []
    stack.append(sortedPoints[0])
    stack.append(sortedPoints[1])
    stack.append(sortedPoints[2])
    for k in range(3, len(sortedPoints)):
        while(stack != None):
            pa, pb = popAdd(stack)
            vectorCalculation = getVector(pa, pb, sortedPoints[k])
            if(vectorCalculation == 2):
                stack.pop()
            elif(vectorCalculation == 1):
                break
        stack.append(sortedPoints[k])
    return stack

def calculateSmallestX(stack):
    minX = None
    counter = 0
    for i in range(0, len(stack)):
        if(i == 0):
            minX = stack[i].getX()
            counter = i
        else:
            if(minX > stack[i].getX()):
                minX = stack[i].getX()
                counter = i
            elif(minX == stack[i].getX()):
                if(stack[counter].getY() > stack[i].getY()):
                    minX = stack[i].getX()
                    counter = i

    return(stack[counter], counter)

def calculateBiggestX(stack):
    maxX = None
    counter = 0
    for i in range(0, len(stack)):
        if(i == 0):
            maxX = stack[i].getX()
            counter = i
        else:
            if(maxX < stack[i].getX()):
                maxX = stack[i].getX()
                counter = i
            elif(maxX == stack[i].getX()):
                if(stack[counter].getY() > stack[i].getY()):
                    maxX = stack[i].getX()
                    counter = i
    return(stack[counter], counter)

def getEnvelopes(stack, smallestXIndex, biggestXIndex):
    upper = 0
    lower = 0

    if(smallestXIndex > biggestXIndex):
        temp = biggestXIndex
        biggestXIndex = smallestXIndex
        smallestXIndex = temp

    for i in range(smallestXIndex, biggestXIndex + 1):
        lower += 1
    upper = len(stack) - lower + 2

    return upper, lower

def merge(a, b):
    res = []
    ca = 0
    cb = 0

    while ca < len(a) and cb < len(b):
        if a[ca] < b[cb]:
            res.append(a[ca])
            ca += 1
        else:
            res.append(b[cb])
            cb += 1

    if ca == len(a):
        while cb < len(b):
            res.append(b[cb])
            cb += 1
    else:
        while ca < len(a):
            res.append(a[ca])
            ca += 1

    return res

def msort(a, n):
    if n <= 1:
        return a

    midpoint = n//2

    if n & 1:
        l1 = msort(a[:midpoint], n//2)
        l2 = msort(a[midpoint:], n//2+1)
    else:
        l1 = msort(a[:midpoint], n//2)
        l2 = msort(a[midpoint:], n//2)
    return merge(l1, l2)

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


a = []
b = []
points = []
angles = []
sortedAngles = []
sortedPoints = []

a, b = getInput()
points = getPoints(a, b)
origin = calculateSmallestY(points)
angles = getAngles(points, origin)
angles.append(0)
sortedAngles = msort(angles, len(angles))
sortedPoints = sortPoints(points, origin, sortedAngles)
stack = grahamScanCore(sortedPoints)
smallestXPoint, smallestXIndex = calculateSmallestX(stack)
biggestXPoint, largestXIndex = calculateBiggestX(stack)
print(smallestXIndex, largestXIndex)
upper, lower = getEnvelopes(stack, smallestXIndex, largestXIndex)
print upper, lower
for i in range(0, len(sortedAngles)):
    print(sortedAngles[i])
for i in range(0, len(sortedPoints)):
    print(sortedPoints[i].getX())
    print(sortedPoints[i].getY())
