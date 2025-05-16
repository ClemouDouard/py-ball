import pygame
import numpy as np
from config import BALL_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT, CIRCLE_RADIUS

class Ball:
    def __init__(self, x, y, color):
        self.ball_position = np.array([x, y], dtype=float)
        self.ball_velocity = np.array([0.0, 0.0])
        self.color = color

    def update(self):
        self.ball_velocity[1] += 0.3

        direction = self.ball_position - np.array([SCREEN_WIDTH//2, SCREEN_HEIGHT//2])
        distance = np.linalg.norm(direction)

        if distance + BALL_RADIUS >= CIRCLE_RADIUS:
            if distance != 0:
                normal = direction / distance
                self.ball_velocity = self.ball_velocity - 2*np.dot(self.ball_velocity, normal) * normal

        self.ball_position += self.ball_velocity


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.ball_position[0]), int(self.ball_position[1])), BALL_RADIUS)

