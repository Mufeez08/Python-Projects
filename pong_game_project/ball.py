from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.setpos(0,0)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.movespeed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)


    def wallbounce(self):
        self.y_move *= -1

    def paddlebounce(self):
        self.x_move *= -1
        self.movespeed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.movespeed = 0.1
        self.paddlebounce()

