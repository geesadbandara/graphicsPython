import graphics

win = graphics.GraphWin("My UI", 1000,1000)
win.setBackground("#ADD8E6")

def drawLine(x1,x2,y1,y2):
    linePoint1 = graphics.Point(x1,y1)
    linePoint2 = graphics.Point(x2,y2)
    lineA = graphics.Line(linePoint1,linePoint2)
    lineA.draw(win)
    mid =lineA.getCenter()
    #return mid


drawLine(3.5,1000,8,8)
def drawCircle(x,y,r,color):
    circPoint = graphics.Point(x,y)
    circ = graphics.Circle(circPoint,r)
    circ.setFill(color)
    circ.draw(win)

drawCircle(500,8,500,"White")
drawCircle(500,8,400,"#ADD8E6")

def drawRectangle(x1,y1,x2,y2):
    point1 = graphics.Point(x1,y1)
    point2 = graphics.Point(x2,y2)
    rec1 = graphics.Rectangle(point1,point2)
    rec1.setFill("White")
    rec1.draw(win)
drawRectangle(300,200,700,50)

def createText(x,y):
    point = graphics.Point(x,y)
    text = graphics.Text(point, "Geex World")
    text.setSize(20)
    text.setFill("Blue")
    text.draw(win)

createText(500,150)
