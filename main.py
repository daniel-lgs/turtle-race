from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=1000, height=500)
my_screen.bgcolor("gray10")
message = "Enter the color of the turtle you think will be the winner: "
user_color_choice = my_screen.textinput(title="Choose your guess", prompt=message)
my_turtles = []
my_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
my_x = -480
my_y = 125

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(my_colors[i])
    new_turtle.goto(x=my_x, y=my_y)
    my_y -= 41.66
    my_turtles.append(new_turtle)

winner_color = ""
race_is_on = True

while race_is_on:
    for turtle in my_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.pos()[0] > 480:
            race_is_on = False
            winner_color = turtle.color()[0]
            break

if winner_color == user_color_choice:
    print("You win!")
else:
    print(f"You lose! The {winner_color} turtle was the winner!")

my_screen.exitonclick()
