import pygame
import numpy as np


class NoteCircle:
    def __init__(self, screen, color, center_x, center_y, radius, arc_radius, distance=np.pi, angular_speed=0.02, track_name=""):
        self.screen = screen
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.color = color
        self.distance = distance
        self.angular_speed = angular_speed
        self.arc_radius = arc_radius
        self.x = center_x + int(self.arc_radius * np.cos(self.distance))
        self.y = center_y + int(self.arc_radius * np.sin(self.distance))
        if track_name != "":
            self.track = pygame.mixer.Sound(track_name)
            self.track.set_volume(0.5)

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
        self.distance += self.angular_speed
        self.x = self.center_x + int(self.arc_radius * np.cos(self.distance))
        self.y = self.center_y + int(self.arc_radius * np.sin(self.distance))
        
        if self.distance >= 2 * np.pi:
            self.angular_speed *= -1
            self.distance = 2 * np.pi
            self.track.play()
            self.track.fadeout(1000)

        if self.distance <= np.pi:
            self.angular_speed *= -1
            self.distance = np.pi
            self.track.play()
            self.track.fadeout(1000)