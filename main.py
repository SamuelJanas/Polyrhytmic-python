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
LINE_OFFSET_BOTTOM = 0.8 * HEIGHT

clock = pygame.time.Clock()

number_of_notes = 5
circle_width = 6
half_length= (WIDTH - 2 * LINE_OFFSET_SIDES) / 2
circle_interval = (half_length)/(number_of_notes+1)

# circle arc pairs: (circle, arc)
center_x = LINE_OFFSET_SIDES + half_length
center_y = HEIGHT - LINE_OFFSET_BOTTOM

circles = []
arcs = []

for i in range(number_of_notes):
    circles.append(NoteCircle.NoteCircle(screen, Color.RED, LINE_OFFSET_SIDES + circle_interval * (i+1), center_y, center_x, circle_width, angular_speed=0.05 + 0.002 * i))
    arc_radius = circles[i].get_flight_arc_radius(center_x)
    arcs.append(FlightArc.FlightArc(screen, Color.WHITE, center_x, center_y, arc_radius, np.pi, 0))

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
    clock.tick(60)

pygame.quit()