import pygame
from config import *
from ball import Ball
from circle import Circle

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rebond Musical")
clock = pygame.time.Clock()

ball = Ball(SCREEN_WIDTH//2 + 50, SCREEN_HEIGHT//2, COLORS["ball_red"])
circle = Circle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, CIRCLE_SPEED)

running = True
while running:
    screen.fill(COLORS["background"])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.update()
    circle.update()

    ball.draw(screen)
    circle.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
