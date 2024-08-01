import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game ")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
State_list = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(f"{len(guessed_states)}/50 states correct", "What is your guess? ").title()
    # print(answer)

    if answer == "Exit":
        #list comprehension
        states_to_learn = [states for states in State_list if states not in guessed_states]
        # for states in State_list:
        #     if states not in guessed_states:
        #         states_to_learn.append(states)
        learn = pandas.DataFrame(states_to_learn)
        learn.to_csv("States_to_learn.csv")
        break
    if answer in State_list:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.ht()
        t.penup()
        State = data[data.state == answer]
        t.goto(State.x.item(), State.y.item())
        t.write(answer)

