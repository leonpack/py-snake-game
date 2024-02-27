from turtle import Turtle
import random as r

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.next_random_location()

    def next_random_location(self):
        self.goto(r.randint(-220, 220), r.randint(-220, 220))