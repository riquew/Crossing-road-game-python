from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 15, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.level = 1
        with open('highscore.txt') as text:
            self.highscore = int(text.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.penup()
        self.goto(x=-150, y=270)
        self.write(f'Level: {self.level}  Highscore: {self.highscore}', move=False, align=ALIGN, font=FONT)

    def reset(self):
        if self.level > self.highscore:
            self.highscore = self.level
            with open('highscore.txt', mode='w') as text:
                text.write(str(self.highscore))
        self.level = 1
        self.update_score()


    # def game_over(self):
    #     self.penup()
    #     self.home()
    #     self.write(f'GAME OVER', move=False, align=ALIGN, font=FONT)




