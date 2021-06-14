# importing area
import turtle
from turtle import Screen
import pandas
from state_display import StateMove

# object assigning
screen = Screen()
error = StateMove()
state_display = StateMove()

# making picture of india a shape and backgroung
bg_image = "india_map.gif"
screen.addshape(bg_image)
turtle.shape(bg_image)

# tile of the file
screen.title("Guess the States in India")

# reading the csv data and handling
state_file = pandas.read_csv("states_cor.csv")
state_list = state_file["states"].to_list()

states_got = []
missing_states = []
while len(states_got) < 36:
    # diplay a dialog box for entering the state name
    user_choice = screen.textinput(title="Guess the State", prompt="Enter the state").title()

    # check if the user want to stop the program and also making a csv data for mmissing data
    if user_choice == "Exit":
        missing_states = [state for state in state_list if state not in states_got]
        missing_data = pandas.DataFrame(missing_states)
        missing_data.to_csv("states_names_missed.csv")
        break

    # checking if the user data with previous data
    elif user_choice in states_got:
        error.error_message("Already guessed try again")

    # checking the data entered by the user is in state_list and printing the state name in specific location
    elif user_choice in state_list:
        state_cord = state_file[state_file.states == user_choice]
        state_display.move_to_position(int(state_cord.x), int(state_cord.y), user_choice)
        states_got.append(user_choice)

    # checking the user input in invalid or not
    else:
        error.error_message("invalid entry")

# To screen stay on
turtle.getscreen()._root.mainloop()
