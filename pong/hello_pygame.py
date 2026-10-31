import pygame

pygame.init() #initialise all modules

screen = pygame.display.set_mode((800,600)) 
"""
#pygame.display.set_mode((width, height)) -This function creates a display window with the specified dimensions.
The function returns a Surface object representing the display. We store that object in the variable screen.
Why? - Because we will use screen to draw things on our game window.
"""

pygame.display.set_caption("Hello player trinity")
#title displayed in the window's title bar

clock = pygame.time.Clock()
#When running a game, Python executes instructions as quickly as your computer allows.
#Without controlling the execution speed, your game might run extremely fast on one computer and slower on another.
#Pygame provides the Clock() object to control the frame rate.

#clock.tick(60) - This limits the game loop to approximately 60 iterations per second.

running = True
while running:
    for event in pygame.event.get(): #event is something that happens while your game is running
        #pygame.event.get()
        #This retrieves the events that have occurred since the previous time you checked the event queue.
        if event.type == pygame.QUIT:
            running = False

    screen.fill((50,255,60)) #r,g,b
    pygame.display.flip()
    """when you draw something on the screen Surface, the changes are not necessarily displayed immediately.
Pygame uses a display-update mechanism. pygame.display.flip() updates the entire display with the contents of the screen Surface."""

    clock.tick(60) #60 represents the maximum number of frames per second (FPS) -> upper limit

pygame.quit() #It shuts down the Pygame modules that were initialized earlier.