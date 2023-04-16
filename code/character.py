import pygame
from support import import_folder

class Character(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.movement_speed = 5
        self.hp = 100
        self.hp_regen = 0
        self.lifesteal = 0
        self.melee_dmg = 5
        self.ranged_dmg = 5
        self.elemental_dmg = 0
        self.atk_speed = 1
        self.crit_chance = 1
        self.armor = 0
        self.dodge = 0
        self.luck = 0

class Player(Character):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../assets/player/FunGuyMainChar.png').convert_alpha()

        self.rect = self.image.get_rect(center = (pos)) 
        self.hitbox = self.rect.inflate(0,-26)
        self.direction = pygame.math.Vector2()
        self.inventory = []

        # graphics setup
        self.import_player_assets()
        self.status = 'right'
        self.frame_index = 0
        self.animation_speed = 0.15


    def import_player_assets(self):
        character_path = '../assets/player/'
        self.animations = {'right': [], 'left': [], 'right_idle': [], 'left_idle': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if 'idle' not in self.status:
                self.status += '_idle'

    def add_item(self, item):
        self.inventory.append(item)
        self.hp += item.hp_bonus
        self.hp_regen += item.hp_regen_bonus
        self.lifesteal += item.lifesteal_bonus
        self.melee_dmg += item.melee_dmg_bonus
        self.ranged_dmg += item.ranged_dmg_bonus
        self.elemental_dmg += item.elemental_dmg_bonus
        self.atk_speed += item.atk_speed_bonus
        self.crit_chance += item.crit_chance_bonus
        self.armor += item.armor_bonus
        self.dodge += item.dodge_bonus
        self.luck += item.luck_bonus

    def draw_inventory(self, screen):
        x, y = 50, 50
        for item in self.inventory:
            if item.image is not None:
                screen.blit(item.image, (x, y))
            x += item.image.get_width() + 10

    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = self.status.replace('_idle', '')
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = self.status.replace('_idle', '')
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        else:
            self.direction.x = 0
        
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.hitbox.center += self.direction * speed

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.input()
        self.get_status()
        self.animate()
        self.move(self.movement_speed)