import turtle
import time
import random

# Clase de la comida
class Comida():

    def __init__(self, colorComida, screen,size):
        x=0
        y=0
        if (size/50)%2==0:
            x=-25
            y=-25
        else:
          x=50
          y=50
        """self.comida = turtle.Turtle()
        self.comida.speed(0)
        self.comida.shape('img/Comida.gif')
        self.comida.color(colorComida)
        self.comida.penup()
        self.comida.goto(x-100,y)"""

        self.lado = screen.lado
    def posMin(self,pos):
      #pos=[["1","1","1"],["1","1","1"],["1","0","1"]] 
      sizeMat=len(pos)
      des=0
      if sizeMat%2==0:
        des=25
      #print(sizeMat)
      for i in range(sizeMat):
        for j in range(sizeMat):
          if pos[i][j]=="1":
            x=j*50-50-des
            y=-i*50+50+des
            self.comida = turtle.Turtle()
            self.comida.speed(0)
            self.comida.shape('img/Comida.gif')
            self.comida.penup()
            self.comida.goto(x,y)
            print("x:",x," y:",y)
      return True

          
    # Método de cuando la serpiente colisiona con la comida
    def alColisionar(self, serpiente, pos):
      #return pos[serpiente.cabeza.ycor()][serpiente.cabeza.xcor()]=="1"
      sizeMat=len(pos)
      des=0
      if sizeMat%2==0:
        des=25
      #print(-(serpiente.cabeza.ycor()-50-des)/50,(serpiente.cabeza.xcor()+50+des)/50)
      return pos[int(-(serpiente.cabeza.ycor()-50-des)/50)][int((serpiente.cabeza.xcor()+50+des)/50)]=="1"
         

