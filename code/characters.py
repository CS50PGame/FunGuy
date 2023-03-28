import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
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
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../assets/FunGuy1.png').convert_alpha()
        self.rect = self.image.get_rect(center = (400,300)) 
        self.direction = pygame.math.Vector2()
        self.inventory = []


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
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.center += self.direction * speed

    def update(self):
        self.input()
        self.move(self.movement_speed)