import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.movement_speed = 5
        self.hp = 100
        self.atk = 5

class Player(Character):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../assets/FunGuy1.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (400,300)) 

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.movement_speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.movement_speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.movement_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.movement_speed
    
    def update(self):
        self.player_input()