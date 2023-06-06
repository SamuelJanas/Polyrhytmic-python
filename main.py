import pygame
import Color
import NoteCircle
import FlightArc
import numpy as np

pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

center_x, center_y = (50+750)/2, 500

# Title and Icon
pygame.display.set_caption("Polyrhythm")
# icon = pygame.image.load('assets/icon.png')

number_of_notes = 11
circle_width = 6
half_length = (750-50)/2
circle_interval = (half_length)/(number_of_notes+1)


# circle arc pairs: (circle, arc)

circles = []
arcs = []

for i in range(number_of_notes):
    circles.append(NoteCircle.NoteCircle(screen, Color.RED, 50 + circle_interval * (i+1), center_y, circle_width))
    arc_radius = circles[i].get_flight_arc_radius(center_x)
    arcs.append(FlightArc.FlightArc(screen, Color.WHITE, center_x, center_y, arc_radius, 0, np.pi))

circle_arcs = zip(circles, arcs)

for circle, arc in circle_arcs:
    arc.draw()
    circle.draw()

clock = pygame.time.Clock()
running = True
while running:
    # RGB = Red, Green, Blue
    clock.tick(12)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Color.BLACK)
    pygame.draw.line(screen, Color.WHITE, (50, 500), (750, 500), 1)
    pygame.draw.circle(screen, Color.WHITE, (50, 500), 2)
    pygame.draw.circle(screen, Color.WHITE, (750, 500), 2)
    pygame.draw.circle(screen, Color.WHITE, (center_x, center_y), 2)   

    for circle, arc in circle_arcs:
        circle.move(arc.start_angle, arc.end_angle)
        arc.draw()
        circle.draw()

    pygame.display.update()

pygame.quit()