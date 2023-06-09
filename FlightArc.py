import pygame
import Color

class FlightArc:
    def __init__(self, screen, color, x, y, radius, start_angle, end_angle):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.start_angle = start_angle
        self.end_angle = end_angle

    def draw(self):
        pygame.draw.arc(self.screen, self.color, (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2), self.start_angle, self.end_angle, width=1)