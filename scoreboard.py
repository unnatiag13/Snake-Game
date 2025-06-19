from turtle import Turtle
ALIGNMENT="center"
FONT=("courier",15,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("Day-20 & 21(Snake_game)\data.txt") as f:
            self.highscore=int(f.read())
        self.penup()
        self.goto(0,265)
        self.pencolor("white")
        self.ht()
        self.update_score()
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over.",move=False,align=ALIGNMENT,font=FONT)


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score:{self.highscore}",move=False,align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score>self.highscore:
            with open("Day-20 & 21(Snake_game)\data.txt","w") as f:
                f.write(str(self.score))
            self.highscore=self.score
        self.score=0
        self.update_score()

    def inc_score(self):
        self.score+=1
        self.update_score()
        
        


    
     
