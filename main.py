from turtle import Screen
import time
from snake import Snake
from food import Food 
from scoreboard import Scoreboard


screen= Screen()
screen.setup(600,600)
screen.bgcolor("pink4")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

gameOn=True
while gameOn:
    screen.update()
    time.sleep(.1)
    snake.move()


    #collision with food
    if snake.head.distance(food) < 25:
        food.random_pos()
        snake.extend()
        score.inc_score()

    #collision with the wall 
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300:
        score.reset()
        snake.reset()
    #collision with it's own body
    for seg in snake.snake[1:]:
        if snake.head.distance(seg)<10:
            score.reset()
            snake.reset()

    





screen.exitonclick()