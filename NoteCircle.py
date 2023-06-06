import pygame
import numpy as np

# ...

class NoteCircle(pygame.sprite.Sprite):
    def __init__(self, screen, color, x, y, radius):
        super().__init__()
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.angular_velocity = 0.02  # Adjust the angular velocity as needed
        self.angle = 0

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_flight_arc_radius(self, center_x):
        return abs(self.x - center_x)

    def move(self, start_angle, end_angle):
        self.angle += self.angular_velocity

        if self.angle >= end_angle or self.angle <= start_angle:
            self.angular_velocity *= -1  # Reverse the angular velocity if the circle reaches the end of the arc

        arc_center_x = self.screen.get_width() // 2
        arc_center_y = self.screen.get_height() // 2
        self.x = int(self.radius * np.cos(self.angle) + arc_center_x)
        self.y = int(self.radius * np.sin(self.angle) + arc_center_y)
