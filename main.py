from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time


screen = Screen()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
starting_positions = [(0,0),(-20,0),(-40,0)]

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()

    #Eating food(collision with food )
    if snake.head.distance(food) < 25:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    #Detect Collision with the wall.
    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    #if head collides with any segment in the tail


screen.exitonclick()
