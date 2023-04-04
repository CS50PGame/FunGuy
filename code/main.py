import pygame
from characters import Player
from settings import *
from enemy import Enemy

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
        
        allsprites = CameraGroup()
        player = Player([allsprites])
        enemy = Enemy([allsprites])
        enemy2 = Enemy([allsprites])
        enemy2.rect = enemy2.image.get_rect(center = (100,400))
        enemy3 = Enemy([allsprites])
        enemy3.rect = enemy3.image.get_rect(center = (100,100))
        enemy4 = Enemy([allsprites])
        enemy4.rect = enemy4.image.get_rect(center = (700,100))

        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Move player and redraw the screen
            allsprites.custom_draw(player)
            allsprites.update()
            allsprites.enemy_update(player)
            pygame.display.update()
            self.clock.tick(60)

        # Quit Pygame
        pygame.quit()

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../assets/background.png').convert()
        self.rect = self.image.get_rect(center=(0, 0))
        
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2
        self.offset = pygame.math.Vector2()
        
        self.surf = pygame.image.load('../assets/background.png').convert()
        self.rect = self.surf.get_rect(topleft=(0,0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.rect.topleft - self.offset
        self.display_surface.blit(self.surf, floor_offset_pos)

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
        
    def enemy_update(self, player):
        enemy_sprites = [
            sprite
            for sprite in self.sprites()
            if hasattr(sprite, "sprite_type") and sprite.sprite_type == "enemy"
        ]
        for enemy in enemy_sprites:
            enemy.enemy_update(player)

if __name__=="__main__":
    game = Game()
    game.run()
    