# assignment: programming assignment 1
# author: Will Sobolewski
# date: July 20th, 2023
# file: game.py is a program that is the __main__ for the fifteen puzzle game
# input: mouse clicks
# output: fifteen puzzle


from tkinter import *
import tkinter.font as font
from random import shuffle
from fifteen import Fifteen
import numpy as np
from tkinter import messagebox


class SlidingPuzzleGUI:
    def __init__(self, size=4):
        self.size = size
        self.fifteen = Fifteen(size)
        self.buttons = []

    def create_buttons(self, frame):
        for row in range(self.size):
            button_row = []
            for col in range(self.size):
                if row == self.size - 1 and col == self.size - 1:
                    text = ""
                else:
                    text = str(self.fifteen.layout[row][col])
                f = font.Font(family="Helvetica", size=24, weight="bold")
                button = Button(frame, text=text, font=f, width=4,
                                height=2, bg="bisque", fg="black")
                button.grid(row=row, column=col, padx=2, pady=2)
                button.bind("<Button-1>", lambda event, r=row,
                            c=col: self.move_tile(r, c))
                button_row.append(button)
            self.buttons.append(button_row)

    def update_buttons(self):
        layout = self.fifteen.layout
        empty_row, empty_col = self.fifteen.get_empty_space_position()
        for row in range(self.size):
            for col in range(self.size):
                if row == empty_row and col == empty_col:
                    text = ""
                else:
                    text = str(layout[row][col])
                self.buttons[row][col].configure(text=text)

    def move_tile(self, row, col):
        self.fifteen.move_tile(row, col)
        self.update_buttons()
        if self.fifteen.is_solved():
            messagebox.showinfo("Congratulations!", "You solved the puzzle!")

    def shuffle_puzzle(self):
        self.fifteen.shuffle()
        self.update_buttons()

    def create_gui(self):
        gui = Tk()
        gui.title("Sliding Puzzle")

        frame = Frame(gui)
        frame.pack(padx=10, pady=10)

        self.create_buttons(frame)

        shuffle_button = Button(gui, text="Shuffle", font=font.Font(
            family="Helvetica", size=12, weight="bold"), command=self.shuffle_puzzle)
        shuffle_button.pack(pady=10)

        gui.mainloop()


# Usage example
game = SlidingPuzzleGUI(size=4)
game.create_gui()
