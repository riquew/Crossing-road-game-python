import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car_list = []

screen.listen()
screen.onkey(key='w', fun=player.go_up)
screen.onkey(key='s', fun=player.go_down)
game_is_on = True
while game_is_on:
    time.sleep(player.flash)
    screen.update()
    qtt = 25 #Quantity of cars.
    while len(car_list) < qtt:
        car = CarManager()
        car_list.append(car)
    for car in range(len(car_list)):
        car_list[car].moving()
        # Check collision with car:
        if car_list[car].distance(player) < 21:
            score.reset()
            for car in car_list:
                car.hideturtle()
            car_list.clear()
            player.goto(0, -280)
            while len(car_list) < qtt:
                car = CarManager()
                car_list.append(car)
        # Check if the turtle has crossed the road:
        elif player.ycor() > 310:
            score.level += 1
            player.reset()
            score.update_score()
            for element in range(len(car_list)):
                car_list[element].speeding_up()










screen.exitonclick()

























