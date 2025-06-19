from turtle import Turtle,Screen
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("midnightblue")
        self.shape("circle")
        self.penup()
        # self.shapesize(0.8)
        self.speed("fastest")
        self.random_pos()

    def random_pos(self):
        self.goto(random.randint(-280,280),random.randint(-280,280))

