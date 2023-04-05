import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.sprite_type = "enemy"
        
        self.direction = pygame.math.Vector2()
        self.image = pygame.image.load('../assets/enemy/EnemyBoy.png').convert_alpha()

        self.rect = self.image.get_rect(center = (600,400))
        self.speed = 1
        
    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.center += self.direction * self.speed
        
    def get_player_distance(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        
        return (player_vec - enemy_vec).magnitude()
    
    def get_player_direction(self, player, distance):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        
        if distance > 0:
            return (player_vec - enemy_vec).normalize()
        
        return pygame.math.Vector2(0, 0)
    
    def follow(self, player):
        distance = self.get_player_distance(player)
        self.direction = self.get_player_direction(player, distance)
        
    def update(self):
        self.move()
        
    def enemy_update(self, player):
        self.follow(player)