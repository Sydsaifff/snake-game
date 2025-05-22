from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


my_screen = Screen()
my_screen.setup(600,600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

snake = Snake()
food = Food()
points = ScoreBoard()

my_screen.listen()

my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")




game_is_on = True

while game_is_on:
        my_screen.update()
        time.sleep(0.05)
        snake.move()
        

        #food collision and refreshing it's location
        if snake.segments[0].distance(food) < 15:
                snake.extend()
                food.refresh()
                points.increase()

        #collision with the walls
        if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
                points.game_over()
                game_is_on = False

        # collision with it's own body
        for segment in snake.segments[1:]:
                if snake.segments[0].distance(segment) < 10:
                        game_is_on = False
                        points.game_over()




                
                

        
        
                


  

        
                
        











my_screen.exitonclick()

