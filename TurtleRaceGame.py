import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which color will win?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
race_on = True
winner = ""

x = -230
y = -70

def t_creator(amount, colors, x, y):
    t_dic = {}
    for i in range(amount):
        t = Turtle(shape="turtle")
        t.color(colors[i])
        t.penup()
        t.goto(x, y)
        y += 30
        t_dic[f"t{i}"] = t
    return t_dic

t_dic = t_creator(6,colors, x, y)

while race_on:

    for t in t_dic.values():
        rand_distance = random.randint(0,10)
        t.forward(rand_distance)
        if t.xcor() > 230:
            race_on = False
            winner = t.color()[0]
            if winner == user_input:
                screen.textinput("Result", f"You won! The {winner} turtle is the winner! 🏆")
            else:
                screen.textinput("Result", f"You lost! The {winner} turtle won the race! 💨")
            break

screen.exitonclick()