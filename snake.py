from turtle import Turtle
MOVE_DIS=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]

class Snake():
    def __init__(self):
        self.snake=[]
        self.create_snake()
        self.head=self.snake[0]
        

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segement(i)
           

    def add_segement(self,position):
        saap = Turtle("square")
        saap.up()
        saap.goto(position)
        saap.color("white")
        self.snake.append(saap)

    def extend(self):
         self.add_segement(self.snake[-1].position())

    def reset(self):
        for i in self.snake:
            i.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head=self.snake[0]

    def move(self):
        for s in range(len(self.snake)-1,0,-1):
            self.snake[s].goto(self.snake[s-1].pos())
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    