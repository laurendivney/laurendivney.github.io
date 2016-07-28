"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)

WHITE = (255, 255, 255)
PURPLE = (178, 102, 255)
MINT = (51, 255, 153)
ROSE = (204, 0, 102)
BLUE2 = (0, 0, 204)
YELLOW = (255, 255, 0)
COLORS= [WHITE, PURPLE, MINT, ROSE, BLUE2, YELLOW]


pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()




# WRITE YOUR CODE HERE


circle_y = 250
circle_x = 350
r = random.randint (20,80)
min_x = r
min_y = r
max_x = SCREEN_WIDTH - r
max_y = SCREEN_HEIGHT - r
move_x = 1
new_x = 350
new_y = 250
move_y = 1
SPEED = random.randint(-10,10)

while True:
    SPEED = random.randint(-10,10)
    if SPEED == 0:
        SPEED = random.randint(-10,10)
    else:
        break





# -------- MAIN PROGRAM LOOP -----------
while not done:
    # --- MAIN EVENT LOOP --------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    # --- GAME LOGIC should go here


    # SCREEN CODE: 

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(PURPLE)


    # DRAWING CODE: 
    # --- should go here
    pygame.draw.circle(screen, random.choice(COLORS), (circle_x, circle_y), r, 0)
    while True:
        new_x = circle_x + move_x * SPEED
        new_y = circle_y + move_y * SPEED
        if (new_x >= min_x and new_x <= max_x) and (new_y >= min_y and new_y <= max_y):
            circle_x = new_x
            circle_y = new_y
            break
        if new_x < min_x or new_x > max_x:
            move_x *= -1
        if new_y < min_y or new_y > max_y:
            move_y *= -1
        
        






    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
