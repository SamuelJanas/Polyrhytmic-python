import pygame
import colors
import NoteCircle

pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))
screen.fill(colors.BLACK)
pygame.draw.line(screen, colors.WHITE, (50, 500), (750, 500), 1)
pygame.draw.circle(screen, colors.WHITE, (50, 500), 2)
pygame.draw.circle(screen, colors.WHITE, (750, 500), 2)
# Title and Icon
pygame.display.set_caption("Polyrhythm")
# icon = pygame.image.load('assets/icon.png')

# Circles 
circle1 = NoteCircle.NoteCircle(screen, colors.RED, 70, 500, 10)
circle2 = NoteCircle.NoteCircle(screen, colors.GREEN, 120, 500, 10)
# Game Loop
running = True
while running:
    # RGB = Red, Green, Blue


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    circle1.draw()
    circle2.draw()


    pygame.display.update()
