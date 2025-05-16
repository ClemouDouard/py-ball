import pygame

if __name__ == "__main__":
    pygame.init()
    running = True

    screen = pygame.display.set_mode((1080,1920))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0,0,0))
    
    pygame.quit()