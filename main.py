from turtle import Turtle, Screen
import random
sc = Screen()
sc.setup(width=500, height=500)
user_bet = sc.textinput(title="Make your Bet", prompt="which turtle will win the game? Enter a color")
color = ["red", "green", "blue", "pink", "yellow", "brown"]
y_direction = [-100, -70, -40, -10, 20, 50]
all_turtles = []
is_race_on = False
if user_bet:
    is_race_on = True

for x in range(6):
    tim = Turtle(shape="turtle")
    tim.color(color[x])
    tim.penup()
    tim.goto(x=-230, y=y_direction[x])
    all_turtles.append(tim)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_turtle = turtle.pencolor()
            if win_turtle == user_bet:
                print(f"Congratulations Your turtle {user_bet}, win the Game")
            else:
                print(f"Ohh No Your turtle {user_bet}, Lost the Game ")
        run = random.randint(1, 10)
        turtle.forward(run)

sc.exitonclick()
