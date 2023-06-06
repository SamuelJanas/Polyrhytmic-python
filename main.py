import pygame
import Color
import NoteCircle
import FlightArc
import numpy as np
import math


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

speed = 0.012
speed_offset = 0.001

for i in range(number_of_notes):
    arc_radius = (i+1) * circle_interval
    track = f"assets/{i+1}.wav"
    circles.append(NoteCircle.NoteCircle(screen, Color.CIRCLE, center_x, center_y, circle_width, arc_radius, angular_speed=speed - speed_offset * i, track_name=track))
    arcs.append(FlightArc.FlightArc(screen, Color.gradient[i], center_x, center_y, arc_radius, 0, np.pi))

circle_arcs = arcs + circles

circle_arcs_copy = circle_arcs.copy()

# Game loop
running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_m:
                # change volume to 0 or 1
                for circle in circles:
                    if circle.track.get_volume() == 0:
                        circle.track.set_volume(0.5)
                    else:
                        circle.track.set_volume(0)
            # lower volume on down arrow raise on up arrow
            elif event.key == pygame.K_DOWN:
                for circle in circles:
                    circle.track.set_volume(circle.track.get_volume() - 0.1)
            elif event.key == pygame.K_UP:
                for circle in circles:
                    circle.track.set_volume(circle.track.get_volume() + 0.1)
            elif event.key == pygame.K_r:
                circle_arcs = circle_arcs_copy.copy()
                for circle in circles:
                    circle.track.stop()
                    circle.distance = np.pi
                    circle.angular_speed = speed - speed_offset * (circles.index(circle))
                    circle.x = center_x + int(circle.arc_radius * np.cos(circle.distance))
                    circle.y = center_y + int(circle.arc_radius * np.sin(circle.distance))
                    circle.track.play()
                    circle.track.fadeout(1000)

    if not paused:
        # Clear the screen
        screen.fill(Color.BLACK)
        pygame.draw.line(screen, Color.WHITE, (LINE_OFFSET_SIDES, HEIGHT - LINE_OFFSET_BOTTOM), (WIDTH - LINE_OFFSET_SIDES, HEIGHT - LINE_OFFSET_BOTTOM), 2)

        for shape in circle_arcs:
            shape.draw()

        pygame.display.update()
        clock.tick(288)

pygame.quit()
