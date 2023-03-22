import pygame
from characters import Player

# Initialize Pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simple')

clock = pygame.time.Clock()

# Title Screen
font = pygame.font.Font(None, 64)
title_text = font.render("FunGuy", True, (255, 0, 0))
font = pygame.font.Font(None, 16)
subtitle_text = font.render("Press any key to start", True, (0, 0, 255))
title_rect = title_text.get_rect()
title_rect.center = screen.get_rect().center
subtitle_rect = subtitle_text.get_rect()
subtitle_rect.center = (title_rect.center[0], title_rect.center[1] + 100)
screen.blit(title_text, title_rect)
screen.blit(subtitle_text, subtitle_rect)
pygame.display.flip()

# Wait for input to start the game loop
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
            waiting = False

# Initialize game screen and player
screen.fill((255, 255, 255))
pygame.display.update()
player = pygame.sprite.GroupSingle()
player.add(Player())
player.draw(screen)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player and redraw the screen
    player.update()
    screen.fill((255, 255, 255))
    player.draw(screen)
    pygame.display.update()
    clock.tick(60)

# Quit Pygame
pygame.quit()
