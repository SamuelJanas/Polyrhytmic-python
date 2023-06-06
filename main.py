import pygame
import Color
import NoteCircle
import FlightArc
import numpy as np


pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Polyrhythm")

LINE_OFFSET_SIDES = 50
LINE_OFFSET_BOTTOM = 0.2 * HEIGHT

clock = pygame.time.Clock()

number_of_notes = 12
circle_width = 4
half_length= (WIDTH - 2 * LINE_OFFSET_SIDES) / 2
circle_interval = (half_length)/(number_of_notes+1)

# circle arc pairs: (circle, arc)
center_x = LINE_OFFSET_SIDES + half_length
center_y = HEIGHT - LINE_OFFSET_BOTTOM

circles = []
arcs = []

for i in range(number_of_notes):
    arc_radius = (i+1) * circle_interval
    track = f"assets/{i+1}.wav"
    circles.append(NoteCircle.NoteCircle(screen, Color.RED, center_x, center_y, circle_width, arc_radius, angular_speed=0.005 - 0.0001 * i, track_name=track))
    arcs.append(FlightArc.FlightArc(screen, Color.WHITE, center_x, center_y, arc_radius, 0, np.pi))

circle_arcs = arcs + circles

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   # Clear the screen
    screen.fill(Color.BLACK)
    pygame.draw.line(screen, Color.WHITE, (LINE_OFFSET_SIDES, HEIGHT - LINE_OFFSET_BOTTOM), (WIDTH - LINE_OFFSET_SIDES, HEIGHT - LINE_OFFSET_BOTTOM), 2)

    for shape in circle_arcs:
        shape.draw()


    pygame.display.update()
    clock.tick(144)

pygame.quit()