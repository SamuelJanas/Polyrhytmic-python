import pygame
import numpy as np

# ...

class NoteCircle:
    def __init__(self, screen, color, x, y, center_x, radius, angle=0, angular_speed=0.02):
        self.screen = screen
        self.center_x = center_x
        self.center_y = y
        self.x = x
        self.y = y
        self.starting_x = x
        self.starting_y = y
        self.radius = radius
        self.color = color
        self.angle = angle
        self.angular_speed = angular_speed
        self.move_radius = self.get_flight_arc_radius(center_x)

    def draw(self):
        self.update()
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_flight_arc_radius(self, center_x):
        return abs(self.x - center_x)

    def update(self):
        self.angle += self.angular_speed
        self.x = self.center_x + int(self.move_radius * np.cos(self.angle))
        self.y = self.center_y + int(self.move_radius * np.sin(self.angle))
        # check if on the other side of the arc
        if self.angle > np.pi or self.angle < 0:
            self.angular_speed *= -1
