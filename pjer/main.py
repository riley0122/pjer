import turtle
import tkinter
turtle.title('pjer')
class sprite():
    def __init__(self, model, speed):
      turtle.pencolor('#000000')
      self.model = model
      turtle.speed(speed)

    def create(self, x, y):
        self.id = {
          "x":x,
          "y":y
        }

    def move(self,ox,oy,xc,yc,diffrence):
      self.undraw(ox,oy,diffrence)
      self.draw(ox+(xc*diffrence),oy+(yc*diffrence),diffrence)
  
    def draw(self,x,y, diffrence):
      turtle.pencolor('#000000')
      turtle.penup()
      turtle.goto(x,y)
      turtle.pensize(diffrence)
      turtle.ht()
      for i in range(len(self.model)):
        if i==4 or i==8 or i==12:
          turtle.penup()
          turtle.back(4*diffrence)
          turtle.right(90)
          turtle.forward(diffrence)
          turtle.left(90)
        
        if self.model[i]==1:
          turtle.pendown()
          turtle.forward(0)
          turtle.penup()
          turtle.forward(diffrence)
        elif self.model[i]==0:
          turtle.penup()
          turtle.forward(diffrence)
        
        turtle.ht()

    def undraw(self,x,y,diffrence):
      turtle.penup()
      turtle.goto(x,y)
      turtle.pencolor('#ffffff')
      for i in range(len(self.model)):
        if i==4 or i==8 or i==12:
          turtle.penup()
          turtle.back(4*diffrence)
          turtle.right(90)
          turtle.forward(diffrence)
          turtle.left(90)
        
        if self.model[i]==1:
          turtle.pendown()
          turtle.forward(0)
          turtle.penup()
          turtle.forward(diffrence)
        elif self.model[i]==0:
          turtle.penup()
          turtle.forward(diffrence)
        
        turtle.ht()

class prefs():
  def setTitle(title):
    turtle.title(title)

  def setIcon(icoPath):
    root = turtle.Screen()._root
    root.iconbitmap(icoPath)

  def screenSize(height,width):
    turtle.screensize(canvwidth=width, canvheight=height)