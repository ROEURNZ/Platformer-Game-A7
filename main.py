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

game_level= tk.PhotoImage(file="images/bg_level.png")
game_start = tk.PhotoImage(file="images/bg_show1.png")
game_play = tk.PhotoImage(file="images/start_game.png")

btn_start_game = tk.PhotoImage(file="images/btn_start3.png")
btn_exit_game = tk.PhotoImage(file="images/btn_exit1.png")
btn_help_game = tk.PhotoImage(file="images/btn_help1.png")
btn_back = tk.PhotoImage(file="images/btn_back1.png")

help_image = tk.PhotoImage(file="images/help_game5.png")
title_game = tk.PhotoImage(file="images/text_main.png")


def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_start)
    canvas.create_image(270,530, image=btn_start_game, tags="startgame")
    canvas.create_image(670,530,image=btn_exit_game, tags="exit")
    canvas.create_image(1070,530,image=btn_help_game, tags="help")
    canvas.create_image(680,200,image=title_game, tags="text")


# -----level1-----
def levelEasy(event):
    canvas.delete("all")
    canvas.create_image(680, 352,  image=game_play)
    canvas.create_image(200, 220, image=btn_back, tags="startgame")

    # winsound.PlaySound("sounds/music_game1.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

# -------level2------
def levelMedium(event):
    canvas.delete("all")
    canvas.create_image(680, 352,  image=game_play)

# --------level3--------
def levelHard(event):
    canvas.delete("all")
    canvas.create_image(680, 352,  image=game_play)


def showLevel(event):
    canvas.delete("all")
    canvas.create_image(685, 372,  image=game_level)

    canvas.create_text(320, 225, text="Level1",tags="level1", fill='red', font=('Halloween Slime (PERSONAL USE)', 50 ,'bold'))

    canvas.create_text(670, 345, text="Level2",tags="level2", fill='red', font=('Halloween Slime (PERSONAL USE)', 50 ,'bold'))

    canvas.create_text(1020, 445, text="Level3",tags="level3", fill='red', font=('Halloween Slime (PERSONAL USE)', 50 ,'bold'))

    winsound.PlaySound("sounds/music_game1.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

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

canvas.tag_bind("startgame","<Button-1>", showLevel)
canvas.tag_bind("back","<Button-1>", gameShow)
canvas.tag_bind("exit","<Button-1>", gameExit)
canvas.tag_bind("help","<Button-1>", gameHelp)

canvas.tag_bind("level1","<Button-1>", levelEasy)
canvas.tag_bind("level1","<Button-1>", levelMedium)
canvas.tag_bind("level1","<Button-1>", levelHard)


canvas.pack(expand=True, fill='both')
root.mainloop()