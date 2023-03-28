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
        allsprites = pygame.sprite.Group()
        allsprites.add(Background())
        player = Player()
        allsprites.add(player)
        allsprites.draw(self.screen)
        camera = Camera(screen_width, screen_height)

        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Move player and redraw the screen
            allsprites.update()
            camera.update(player)
            for sprite in allsprites:
                self.screen.blit(sprite.image, camera.apply(sprite))
            pygame.display.update()
            self.clock.tick(60)

        # Quit Pygame
        pygame.quit()


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../assets/background.png').convert()
        self.rect = self.image.get_rect(center=(0, 0))

class Camera:
    def __init__(self, width, height):
        self.rect = pygame.Rect(0, 0, width, height)

    def update(self, target):
        x = -target.rect.centerx + WIDTH // 2
        y = -target.rect.centery + HEIGHT // 2
        self.rect = pygame.Rect(x, y, self.rect.width, self.rect.height)

    def apply(self, sprite):
        return sprite.rect.move(self.rect.topleft)


if __name__=="__main__":
    game = Game()
    game.run()