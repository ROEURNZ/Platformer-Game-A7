import tkinter as tk
from tkinter import *
import winsound
from tkinter.ttk import *

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
window = tk.Tk()
window.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
window.title('Mr. Indicredible Destiny')
canvas = tk.Canvas(window,bg="black")

# creates a Tk() object
keyPressed = []
SPEED = 15
TIME = 10
GRAVITY_FORCE = 9
distance = 0
collected_coins = 0
scroll_offset = 0
obstacles = []
all_coins = []
WIN_WIDTH = 1920
canvas_width = 1920
game_over = False
score = 0
is_jumping = False 
width=1920
height=1080
x = 20
y = 20
player_x = width // 2
player_y = height // 2




# -------image----------------
game_level= tk.PhotoImage(file="images/bg_level.png")
game_start = tk.PhotoImage(file="images/bg_show1.png")
game_play = tk.PhotoImage(file="images/forest_img.png")

btn_start_game = tk.PhotoImage(file="images/btn_start3.png")
btn_exit_game = tk.PhotoImage(file="images/btn_exit1.png")
btn_help_game = tk.PhotoImage(file="images/btn_help1.png")
btn_back = tk.PhotoImage(file="images/btn_back1.png")

help_image = tk.PhotoImage(file="images/help_game5.png")
title_game = tk.PhotoImage(file="images/text_main.png")

img_player = tk.PhotoImage(file="images/man.png")
player = canvas.create_image(100, 100, image=img_player)
imge7 = tk.PhotoImage(file="images/land.png")
# ---------------show_game_back---------------


def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_start)
    canvas.create_image(270,530, image=btn_start_game, tags="startgame")
    canvas.create_image(670,530,image=btn_exit_game, tags="exit")
    canvas.create_image(1070,530,image=btn_help_game, tags="help")
    canvas.create_image(680,200,image=title_game, tags="text")


# -----level1-----


# -------level2------
def levelMedium(event):
    canvas.delete("all")
    opennewWindow()

# --------level3--------
def levelHard(event):
    canvas.delete("all")
    opennewWindow()
    



def showLevel(event):
    canvas.delete("all")
    canvas.create_image(685, 372,  image=game_level)

    canvas.create_text(320, 225, text="Level1",tags="level1", fill='red', font=('Halloween Slime (PERSONAL USE)', 50 ,'bold'))

    canvas.create_text(670, 345, text="Level2",tags="level2", fill='red', font=('Halloween Slime (PERSONAL USE)', 50 ,'bold'))

    canvas.create_text(1020, 445, text="Level3",tags="level3", fill='red', font=('Halloween Slime (PERSONAL USE)', 50 ,'bold'))
    
    winsound.PlaySound("sounds/music_game2.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

# ----------------Exit-------------------
def gameExit(event):
    window.destroy()

# ------------------help-------------------
def gameHelp(event):
    canvas.delete("all")
    canvas.create_image(685, 352, image=help_image)
    canvas.create_image(200, 220, image=btn_back, tags="back")


# -------------show_game interface-----------
canvas.create_image(685, 352, image=game_start)

canvas.create_image(680,200,image=title_game, tags="text")
canvas.create_image(270,530, image=btn_start_game, tags="startgame")
canvas.create_image(670,530,image=btn_exit_game, tags="exit")
canvas.create_image(1070,530,image=btn_help_game, tags="help")

winsound.PlaySound("sounds/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

def opennewWindow(): 
        WIN_WIDTH = 1920
        WIN_HEIGHT = 1080
        window.withdraw()
        newWindow = tk.Toplevel(window)
        # sets the title of the
        # Toplevel widget
        newWindow.title("New Window")
        # sets the geometry of toplevel
        newWindow.geometry(window.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT)))
        frame = tk.Frame(newWindow,height=1920,width=1080)
        frame.pack()
        canvas = tk.Canvas(frame, width=1920, height=1080)
        canvas.pack()
        background  = tk.PhotoImage(file="images/bg_show1.png")
        background_img1 = canvas.create_image(650, 300, image=background)
        background_img2 = canvas.create_image(WIN_WIDTH, 300, image=background)
        
        imgae_player = tk.PhotoImage(file="images/man.png")
        player = canvas.create_image(400, 300, image=imgae_player)
        # land = canvas.create_rectangle(0, 500, 1536, 800, fill="Blue", tags="wall")
        image7 = tk.PhotoImage(file="images/land.png")
        canvas.create_image(768, 650, image=image7, tags="wall")

        def game():
            canvas.pack()
            canvas.bind_all("<KeyPress>", handle_key_press)
            canvas.bind_all("<KeyRelease>", handle_key_release)
            canvas.focus_set()
            create_obstacles()
            create_coins()
            # create_obstacles()

        ground = tk.PhotoImage(file="images/ground.png")
        ground1 = tk.PhotoImage(file="images/barrier.png")
        coin_image = tk.PhotoImage(file="images/coin.png")
        
        
        # --------create obstacles---------------
        def create_obstacles():
        
            walls = [
                canvas.create_image( 880  ,  272 , image=ground  , tags="wall")   ,
                canvas.create_image( 680  ,  372 , image=ground  , tags="wall")   ,
                canvas.create_image( 380  ,  472 , image=ground  , tags="wall")   ,
                canvas.create_image( 980  ,  572 , image=ground  , tags="wall")   ,
                canvas.create_image( 1600 ,  570 , image=ground  , tags="wall")   ,
                canvas.create_image( 1480 ,  470 , image=ground  , tags="wall")   ,
                canvas.create_image( 1980 ,  400 , image=ground  , tags="wall")   ,
                canvas.create_image( 3200 ,  380 , image=ground  , tags="wall")   ,
                canvas.create_image( 2480 ,  570 , image=ground  , tags="wall")   ,
                canvas.create_image( 2480 ,  540 , image=ground1 , tags="wall")
            ] 
            for obstacle in walls:
                obstacles.append(obstacle)
                
    # -----------------create cash------------
        def create_coins():
            coins = [
                canvas.create_image(800, 200, image=coin_image, tags="coin"),
                canvas.create_image(600, 300, image=coin_image, tags="coin"),
                canvas.create_image(300, 400, image=coin_image, tags="coin"),
                canvas.create_image(900, 500, image=coin_image, tags="coin"),
                canvas.create_image(1500, 498, image=coin_image, tags="coin"),
                canvas.create_image(1380, 398, image=coin_image, tags="coin"),
                canvas.create_image(1880, 328, image=coin_image, tags="coin"),
                canvas.create_image(3100, 308, image=coin_image, tags="coin"),
                canvas.create_image(2380, 498, image=coin_image, tags="coin"),
                canvas.create_image(2380, 468, image=coin_image, tags="coin")
            ]
            for coin in coins:
                all_coins.append(coin)
        def get_coin():
            for coin in all_coins:
                coin_coords = canvas.coords(coin)
                cx1 = coin_coords[0] + 0
                cx2 = coin_coords[0] + 50
                cy1 = coin_coords[1] - 50
                cy2 = coin_coords[1] - 50
                # player_coords = canvas.coords(player)
                cash = canvas.find_overlapping(cx1,cy1,cx2,cy2)
                if player in cash:
                    canvas.delete(coin)
                    all_coins.remove(coin)
          


        def handle_key_press(event):
            global is_jumping, jump_count
            if event.keysym == "Left" and "Left" not in keyPressed:
                keyPressed.append("Left")
            elif event.keysym == "Right" and "Right" not in keyPressed:
                keyPressed.append("Right")
            elif event.keysym == "Up" and not is_jumping:
                is_jumping = True
                jump_count = 20

        def handle_key_release(event):
            if event.keysym == "Left" and "Left" in keyPressed:
                keyPressed.remove("Left")
            elif event.keysym == "Right" and "Right" in keyPressed:
                keyPressed.remove("Right")

        def move_player():
            global is_jumping, jump_count
            x, y = 0, 0
            if "Left" in keyPressed:
                x = -20  # Increase the value to speed up movement to the left
                canvas.move(background_img1, +2, 0)
                canvas.move(background_img2, +2, 0)
                get_coin()
            elif "Right" in keyPressed:
                x = 15  # Increase the value to speed up movement to the right
                canvas.move(background_img1, -2, 0)
                canvas.move(background_img2, -2, 0)
                get_coin()
            if is_jumping:
                y = -GRAVITY_FORCE
                jump_count -= 1
                if jump_count == 0:
                    is_jumping = False

            if check_movement(player, x, y):
                canvas.move(player, x, y)
            scroll_screen(x)

            if not is_jumping:
                apply_gravity()

            window.after(20, move_player)


        def check_movement(item, dx=0, dy=0):
            item_coords = canvas.coords(item)
            new_x1 = item_coords[0] + dx + 50
            new_y1 = item_coords[1] + dy + 50
            new_x2 = item_coords[0] + dx - 50
            new_y2 = item_coords[1] + dy - 50

            overlapping_objects = canvas.find_overlapping(new_x1, new_y1, new_x2, new_y2)

            for wall_id in canvas.find_withtag("wall"):
                if wall_id in overlapping_objects:
                    return False

            return True

        def apply_gravity():
            if not check_movement(player, 0, GRAVITY_FORCE):
                return

            canvas.move(player, 0, GRAVITY_FORCE)
            scroll_screen(0)
        def scroll_screen(x_direction):
            global scroll_offset
            player_coords = canvas.coords(player)
            x1, _ = player_coords

            if x_direction > 0 and x1 >= 300 - scroll_offset:
                scroll_offset += 40
                canvas.move(player, -10, 0)
                for obstacle in obstacles:
                    canvas.move(obstacle, -10, 0)
                for coin in all_coins:
                    canvas.move(coin, -10, 0)

            elif x_direction < 0 and x1 <= scroll_offset:
                scroll_offset -= 40
                canvas.move(player, 10, 0)
                for obstacle in obstacles:
                    canvas.move(obstacle, 10, 0)
                for coin in all_coins:
                    canvas.move(coin, 10, 0)
        
        get_coin()
        game()
        get_coin()
        move_player()
        newWindow.mainloop()    



canvas.tag_bind("startgame","<Button-1>", showLevel)
canvas.tag_bind("back","<Button-1>", gameShow)
canvas.tag_bind("exit","<Button-1>", gameExit)
canvas.tag_bind("help","<Button-1>", gameHelp)

canvas.tag_bind("level1","<Button-1>", opennewWindow)
canvas.tag_bind("level1","<Button-1>", levelMedium)
canvas.tag_bind("level1","<Button-1>", levelHard)


canvas.pack(expand=True, fill='both')


window.mainloop()






































