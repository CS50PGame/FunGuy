import pygame
from characters import Player
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('FunGuy')
        self.clock = pygame.time.Clock()

    def draw_title_screen(self):
        self.screen.fill(('black'))
        font = pygame.font.Font(None, 64)
        title_text = font.render("FunGuy", True, (255, 0, 0))
        font = pygame.font.Font(None, 16)
        subtitle_text = font.render("Press any key to start", True, (0, 0, 255))
        title_rect = title_text.get_rect()
        title_rect.center = self.screen.get_rect().center
        subtitle_rect = subtitle_text.get_rect()
        subtitle_rect.center = (title_rect.center[0], title_rect.center[1] + 100)
        self.screen.blit(title_text, title_rect)
        self.screen.blit(subtitle_text, subtitle_rect)
        pygame.display.flip()

    def run(self):
        self.draw_title_screen()

        # Wait for input to start the game loop
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                    waiting = False

        pygame.display.update()
        player = pygame.sprite.GroupSingle()
        player.add(Player())
        player.draw(self.screen)

        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Move player and redraw the screen
            player.update()
            self.screen.fill((255, 255, 255))
            player.draw(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)

        # Quit Pygame
        pygame.quit()

if __name__=="__main__":
    game = Game()
    game.run()