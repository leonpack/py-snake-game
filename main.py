from turtle import Screen
import time
from snake import Snake
from tkinter import messagebox
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The PySnake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        messagebox.showinfo("Game Over", f"Your final scores: {scoreboard.score}")

    if snake.head.distance(food) < 15:
        food.next_random_location()
        snake.extend()
        scoreboard.increase_score()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            messagebox.showinfo("Game Over", f"Your final scores: {scoreboard.score}")


screen.exitonclick()
