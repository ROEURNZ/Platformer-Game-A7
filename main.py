import tkinter as tk
from tkinter import *
import winsound
from random import randrange

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
root.title('Group 13 - Game Pro')
canvas = tk.Canvas(root,bg="black")

game_play= tk.PhotoImage(file="images/bg_play.png")
game_start = tk.PhotoImage(file="images/bg_show1.png")

btn_start_game = tk.PhotoImage(file="images/btn_start3.png")
btn_exit_game = tk.PhotoImage(file="images/btn_exit1.png")
btn_help_game = tk.PhotoImage(file="images/btn_help1.png")
btn_back = tk.PhotoImage(file="images/btn_back1.png")

help_image = tk.PhotoImage(file="images/game_help2.png")
title_game = tk.PhotoImage(file="images/text_main.png")


def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_start)
    canvas.create_image(270,530, image=btn_start_game, tags="startgame")
    canvas.create_image(670,530,image=btn_exit_game, tags="exit")
    canvas.create_image(1070,530,image=btn_help_game, tags="help")
    canvas.create_image(680,200,image=title_game, tags="text")

def gameStart(event):
    global player, displayKillVirus, displayNumeberBullet, displayTotalCash
    canvas.delete("all")
    canvas.create_image(680, 372,  image=game_play)
    winsound.PlaySound("sounds/play.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

# ----------------Exit-------------------
def gameExit(event):
    root.destroy()

# ------------------help-------------------
def gameHelp(event):
    canvas.delete("all")
    canvas.create_image(685, 352, image=help_image)
    canvas.create_image(200, 220, image=btn_back, tags="back")


canvas.create_image(685, 352, image=game_start)

canvas.create_image(680,200,image=title_game, tags="text")
canvas.create_image(270,530, image=btn_start_game, tags="startgame")
canvas.create_image(670,530,image=btn_exit_game, tags="exit")
canvas.create_image(1070,530,image=btn_help_game, tags="help")

winsound.PlaySound("sounds/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

canvas.tag_bind("startgame","<Button-1>", gameStart)
canvas.tag_bind("back","<Button-1>", gameShow)
canvas.tag_bind("exit","<Button-1>", gameExit)
canvas.tag_bind("help","<Button-1>", gameHelp)


canvas.pack(expand=True, fill='both')
root.mainloop()