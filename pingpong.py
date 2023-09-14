# assignment: programming assignment 1
# author: Will Sobolewski
# date: July 23rd, 2023
# file: pingpong.py is a program that is my attempt at recreating Pong
# input: left and right arrow keys
# output: Ping-Pong Game against AI opponent

from tkinter import *


class Racket:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.racket_id = self.canvas.create_rectangle(
            x, y, x + 100, y + 10, fill=color)

    def move(self, x):
        self.canvas.move(self.racket_id, x, 0)

    def get_coords(self):
        return self.canvas.coords(self.racket_id)


class Ball:
    def __init__(self, canvas, x, y, width, height):  # Add width and height as parameters
        self.canvas = canvas
        self.ball_id = self.canvas.create_oval(
            x, y, x + 10, y + 10, fill="red")
        self.dx, self.dy = 1, 1
        self.width = width  # Store the width and height
        self.height = height

    def move(self):
        x1, y1, x2, y2 = self.canvas.coords(self.ball_id)
        if x2 > self.width or x1 < 0:
            self.dx = -self.dx
        if y2 > self.height or y1 < 0:
            self.dy = -self.dy
        self.canvas.move(self.ball_id, self.dx, self.dy)

    def get_coords(self):
        return self.canvas.coords(self.ball_id)


class PingPong:
    def __init__(self, gui):
        self.gui = gui
        self.canvas = Canvas(gui)
        self.canvas.pack()
        self.width = int(self.canvas.cget('width'))
        self.height = int(self.canvas.cget('height'))

        self.player_racket = Racket(
            self.canvas, self.width // 2 - 50, self.height - 30, "black")
        self.ai_racket = Racket(self.canvas, self.width // 2 - 50, 20, "blue")
        self.ball = Ball(self.canvas, self.width // 2 - 12,
                         self.height // 2 - 12, self.width, self.height)

        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)

        # Initialize scores for both players
        self.player_score = 0
        self.ai_score = 0

        # Create score text for both players with the new format

        self.score_text = self.canvas.create_text(
            self.width // 2, self.height // 2, text=self.get_score_text(), font=('Times', 20))
        self.animation()

    def get_score_text(self):
        return f"{self.player_score}:{self.ai_score}"

    def move_left(self, event):
        self.player_racket.move(-10)

    def move_right(self, event):
        self.player_racket.move(10)

    def check_collision(self):
        ball_coords = self.ball.get_coords()
        player_racket_coords = self.player_racket.get_coords()
        ai_racket_coords = self.ai_racket.get_coords()

        if ball_coords[3] >= player_racket_coords[1] and ball_coords[0] >= player_racket_coords[0] and ball_coords[2] <= player_racket_coords[2]:
            self.ball.dy = -self.ball.dy

        if ball_coords[1] <= ai_racket_coords[3] and ball_coords[0] >= ai_racket_coords[0] and ball_coords[2] <= ai_racket_coords[2]:
            self.ball.dy = -self.ball.dy

        # If the ball goes beyond the goals
        if ball_coords[3] >= self.height:
            self.ai_score += 1
            self.reset_ball()

        if ball_coords[1] <= 0:
            self.player_score += 1
            self.reset_ball()

        # Update the score text with the new format
        self.canvas.itemconfig(self.score_text, text=self.get_score_text())

    def reset_ball(self):
        # Reset the ball position and direction
        self.ball.canvas.move(self.ball.ball_id, self.width // 2 - self.ball.get_coords()[
                              2], self.height // 2 - self.ball.get_coords()[3])
        self.ball.dx, self.ball.dy = 1, 1

    def ai_move(self):
        ball_coords = self.ball.get_coords()
        ai_racket_coords = self.ai_racket.get_coords()
        ai_move_speed = 2

        if ball_coords[0] > ai_racket_coords[2] or ball_coords[2] < ai_racket_coords[0]:
            if ball_coords[0] - ai_racket_coords[0] < 0:
                self.ai_racket.move(-ai_move_speed)
            else:
                self.ai_racket.move(ai_move_speed)

    def animation(self):
        self.ball.move()
        self.ai_move()
        self.check_collision()
        self.gui.after(10, self.animation)


# main program
gui = Tk()
ping_pong = PingPong(gui)
gui.mainloop()
