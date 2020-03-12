class TikTakToe:
    field = {
        "1 3": "_", "2 3": "_", "3 3": "_",
        "1 2": "_", "2 2": "_", "3 2": "_",
        "1 1": "_", "2 1": "_", "3 1": "_"
    }

    def __init__(self):
        self.coordinates = " "
        self.field_row = []
        self.field_colum = []
        self.field_diag = []
        self.x_win = False
        self.o_win = False
        self.state = "1 turn"

    def set_field(self):
        self.field_row = [[self.field["1 3"], self.field["2 3"], self.field["3 3"]],
                          [self.field["1 2"], self.field["2 2"], self.field["3 2"]],
                          [self.field["1 1"], self.field["2 1"], self.field["3 1"]]]
        self.field_colum = [[self.field["1 3"], self.field["1 2"], self.field["1 1"]],
                            [self.field["2 3"], self.field["2 2"], self.field["2 1"]],
                            [self.field["3 3"], self.field["3 2"], self.field["3 1"]]]
        self.field_diag = [[self.field["1 3"], self.field["2 2"], self.field["3 1"]],
                           [self.field["3 3"], self.field["2 2"], self.field["1 1"]]]
        self.x_win = any([any(row == ["X", "X", "X"] for row in self.field_row),
                         any(col == ["X", "X", "X"] for col in self.field_colum),
                         any(dia == ["X", "X", "X"] for dia in self.field_diag)])
        self.o_win = any([any(row == ["O", "O", "O"] for row in self.field_row),
                         any(col == ["O", "O", "O"] for col in self.field_colum),
                         any(dia == ["O", "O", "O"] for dia in self.field_diag)])
        frame = ("---------", "|")
        print("{}".format(frame[0]))
        print("{} {} {} {} {}".format(frame[1], self.field["1 3"], self.field["2 3"], self.field["3 3"], frame[1]))
        print("{} {} {} {} {}".format(frame[1], self.field["1 2"], self.field["2 2"], self.field["3 2"], frame[1]))
        print("{} {} {} {} {}".format(frame[1], self.field["1 1"], self.field["2 1"], self.field["3 1"], frame[1]))
        print("{}".format(frame[0]))
        if self.state != "1 turn":
            self.check_field()
        else:
            self.state = "X turn"
            self.get_move()

    def check_field(self):
        if self.x_win:
            print("X wins")
            self.state = "end"
        elif self.o_win:
            print("O wins")
            self.state = "end"
        elif any(val == "_" for val in self.field.values()):
            pass
        else:
            print("Draw")
            self.state = "end"

    def get_move(self):
        self.coordinates = input("Enter the coordinates: ")
        if self.field.get(self.coordinates, False) and self.field.get(self.coordinates, False) == "_":
            self.make_move_xo()
        else:
            self.error(self.coordinates.split())

    def make_move_xo(self):
        print(new_game.state)
        if self.state == "X turn":
            self.field[self.coordinates] = "X"
            self.state = "O turn"
        elif self.state == "O turn":
            self.field[self.coordinates] = "O"
            self.state = "X turn"
        self.set_field()

    # error processing: OOR or text
    def error(self, daten):
        numbers = ("4", "5", "6", "7", "8", "9", "0")
        if daten[0] in numbers or daten[1] in numbers:
            print("Coordinates should be from 1 to 3!")
            self.get_move()
        elif self.field.get(self.coordinates, False) and self.field.get(self.coordinates) != "_":
            print("This cell is occupied! Choose another one!")
            self.get_move()
        else:
            print("You should enter numbers!")
            self.get_move()


new_game = TikTakToe()
new_game.set_field()
while new_game.state != "end":
    new_game.get_move()
