import pygame


class NoteCircle(pygame.sprite.Sprite):
    def __init__(self, screen, color, x, y, radius):
        super().__init__()
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_flight_arc_radius(self, center_x):
        return abs(self.x - center_x)
    
    

        