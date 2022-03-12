from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
race_on = False

# My initial method
# We create six different new turtles and give each one its color and position on the screen
tim = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
tam = Turtle(shape="turtle")
tem = Turtle(shape="turtle")
tum = Turtle(shape="turtle")
tym = Turtle(shape="turtle")
turtles = [tim, tom, tam, tem, tum, tym]
for i in range(6):
    turtles[i].penup()
    turtles[i].speed(0)
    new_y = -65 + (30 * i)
    turtles[i].goto(x=-240, y=new_y)
    turtles[i].color(colors[i])

# # A much simpler method
# for i in range(6):
#     tim = Turtle(shape="turtle")
#     tim.penup()
#     new_y = -65 + (30 * i)
#     tim.goto(x=-240, y=new_y)
#     tim.color(colors[i])

# Now the race
if user_bet:
    race_on = True

while race_on:
    for i in range(6):
        if turtles[i].xcor() > 210:
            race_on = False
            if user_bet == turtles[i].pencolor():
                print(f"You win! The {turtles[i].pencolor()} turtle won the race.")
            else:
                print(f"You lose! The {turtles[i].pencolor()} turtle won the race.")
        turtles[i].forward(random.randint(0, 10))


screen.exitonclick()
