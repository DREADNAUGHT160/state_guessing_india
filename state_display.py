from turtle import Turtle


class StateMove(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def move_to_position(self, x, y, name):  # function for moving the turtle and print the name
        self.goto(x, y)
        self.write(name)

    def error_message(self, message):  # function for displaying error message
        self.clear()
        self.goto(100, 200)
        self.write(message)
