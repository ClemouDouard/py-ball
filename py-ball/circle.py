import pygame
import math
from config import COLORS, CIRCLE_RADIUS

class Circle:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = speed

    def update(self):
        self.angle += self.speed
        if self.angle >= 360:
            self.angle -= 360

    def draw(self, screen):
        pygame.draw.circle(screen, COLORS["circle"], (self.x, self.y), CIRCLE_RADIUS, 5)

        for i in range(3):
            angle_deg = self.angle + i * 120
            angle_rad = math.radians(angle_deg)
            hole_x = self.x + CIRCLE_RADIUS * math.cos(angle_rad)
            hole_y = self.y + CIRCLE_RADIUS * math.sin(angle_rad)
            pygame.draw.circle(screen, COLORS["background"], (int(hole_x), int(hole_y)), 40)
