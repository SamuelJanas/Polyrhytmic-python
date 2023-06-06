import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Animation")

# Define the colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the clock
clock = pygame.time.Clock()


class Circle:
    def __init__(self, center_x, center_y, radius, color, move_radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.color = color
        self.angle = 0
        self.angular_speed = 0.02
        self.move_radius = move_radius
        self.x = center_x + int(move_radius * math.cos(self.angle))
        self.y = center_y + int(move_radius * math.sin(self.angle))

    def update(self):
        self.angle -= self.angular_speed
        self.x = self.center_x + int(self.move_radius * math.cos(self.angle))
        self.y = self.center_y + int(self.move_radius * math.sin(self.angle))
        # check if on the other side of the arc
        if self.angle > math.pi or self.angle < 0:
            self.angular_speed *= -1
        # reset the angle
        

    def draw(self, screen):
        self.update()
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Arc:
    def __init__(self, center_x, center_y, radius, start_angle, stop_angle, color, thickness=2):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.start_angle = start_angle
        self.stop_angle = stop_angle
        self.color = color
        self.thickness = thickness

    def draw(self, screen):
        pygame.draw.arc(screen, self.color,
                        (self.center_x - self.radius, self.center_y - self.radius, 2 * self.radius, 2 * self.radius),
                        self.start_angle, self.stop_angle, self.thickness)


# Create instances of Circle and Arc

circle = Circle(WIDTH // 2, HEIGHT // 2, 10, RED, 200)
arc = Arc(WIDTH // 2, HEIGHT // 2, 200, math.pi, 2 * math.pi, RED, 2)

# Create a list to store shapes for drawing
shapes = [circle, arc]

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw shapes
    for shape in shapes:
        shape.draw(screen)

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()