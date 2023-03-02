# Day 25 - US States Game

import turtle
import pandas as pd


def add_to_map():
    state = state_df[state_df['state'] == answer_state]
    # Create turtle, go to state location and write state name
    label = turtle.Turtle()
    label.hideturtle()
    label.penup()
    label.goto(
        x=int(state['x']),
        y=int(state['y'])
    )
    label.write(
        answer_state,
        font=('Arial', 8, 'normal')
    )


screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'Day21-30/US_States_Game/blank_states_img.gif'
screen.addshape(image)
screen.tracer(0)
turtle.shape(image)

state_df = pd.read_csv('Day21-30/US_States_Game/50_states.csv')
correct = []
states_to_learn = []

while len(correct) < 50:
    screen.update()
    answer_state = screen.textinput(
        title=f'{len(correct)}/50 States Correct',
        prompt="What's another state's name?"
    ).title()

    if answer_state == 'Exit':
        break
    if answer_state.title() in state_df['state'].values:
        add_to_map()
        if answer_state not in correct:
            correct.append(answer_state)

for state in state_df['state'].values:
    if state not in correct:
        states_to_learn.append(state)

learn_list = pd.DataFrame(states_to_learn)
learn_list.to_csv('Day21-30/US_States_Game/states_to_learn.csv')
