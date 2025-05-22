from turtle import Turtle
from food import Food

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.teleport(0,270)
        self.color("white")
        self.score = 0
        self.write(f"ScoreBoard:{self.score}",False,"center",('courier', 16, 'normal'))       
    
    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"ScoreBoard:{self.score}",False,"center",('courier', 16, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",False,"center",('courier', 16, 'normal'))