import tkinter as tk

# Constants
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 10  # Increase the player speed

# Create the main window
window = tk.Tk()
window.title("Super Mario Game")

# Set the size of the game window
window.geometry(f"{CANVAS_WIDTH}x{CANVAS_HEIGHT}")

# Create the canvas
canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black")
canvas.pack()

# Load the background image
background_image = tk.PhotoImage(file=r"C:\Users\Roeurn.KAKI\Desktop\Platformer Game A7\Assets\Images\Background\background.png")

# Create a background image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Load the player character image
player_image = tk.PhotoImage(file=r"C:\Users\Roeurn.KAKI\Desktop\Platformer Game A7\Assets\Images\Character\player.png")

# Create the player character
player_x = CANVAS_WIDTH // 2 - PLAYER_WIDTH // 2
player_y = CANVAS_HEIGHT - PLAYER_HEIGHT
player = canvas.create_image(player_x, player_y, image=player_image)

# Variables to track player movement
move_left = move_right = move_up = move_down = False

# Function to handle key press events
def handle_key_press(event):
    global move_left, move_right, move_up, move_down
    if event.keysym == "Left":
        move_left = True
    elif event.keysym == "Right":
        move_right = True
    elif event.keysym == "Up":
        move_up = True
    elif event.keysym == "Down":
        move_down = True

# Function to handle key release events
def handle_key_release(event):
    global move_left, move_right, move_up, move_down
    if event.keysym == "Left":
        move_left = False
    elif event.keysym == "Right":
        move_right = False
    elif event.keysym == "Up":
        move_up = False
    elif event.keysym == "Down":
        move_down = False

# Bind key press and release events to functions
window.bind("<KeyPress>", handle_key_press)
window.bind("<KeyRelease>", handle_key_release)

# Function to create obstacles
def create_obstacles():
    # Create five obstacles
    for _ in range(5):
        # Generate random coordinates for the obstacles
        x = canvas.winfo_width() * 0.1  # Adjust the percentage as needed
        y = canvas.winfo_height() * 0.1  # Adjust the percentage as needed
        
        # Draw the obstacle on the canvas
        canvas.create_rectangle(x, y, x+50, y+50, fill="red")  # Adjust the size and color as needed

# Call the create_obstacles function to create the obstacles
create_obstacles()

# Function to update the game state
def update_game():
    # Move the player character
    player_coords = canvas.coords(player)
    player_x = player_coords[0]
    player_y = player_coords[1]

    if move_left and player_x > 0:
        canvas.move(player, -PLAYER_SPEED, 0)
    elif move_right and player_x + PLAYER_WIDTH < CANVAS_WIDTH:
        canvas.move(player, PLAYER_SPEED, 0)

    if move_up and player_y > 0:
        canvas.move(player, 0, -PLAYER_SPEED)
    elif move_down and player_y + PLAYER_HEIGHT < CANVAS_HEIGHT:
        canvas.move(player, 0, PLAYER_SPEED)

    # Schedule the next update
    window.after(10, update_game)

# Start the game loop
update_game()

# Start the Tkinter event loop
window.mainloop()