import pygame

class Item:
    def __init__(self, name, image_path=None, hp_bonus=0, hp_regen_bonus=0, lifesteal_bonus=0, melee_dmg_bonus=0,
                 ranged_dmg_bonus=0, elemental_dmg_bonus=0, atk_speed_bonus=0, crit_chance_bonus=0, armor_bonus=0,
                 dodge_bonus=0, luck_bonus=0):
        self.name = name
        self.image_path = image_path
        self.hp_bonus = hp_bonus
        self.hp_regen_bonus = hp_regen_bonus
        self.lifesteal_bonus = lifesteal_bonus
        self.melee_dmg_bonus = melee_dmg_bonus
        self.ranged_dmg_bonus = ranged_dmg_bonus
        self.elemental_dmg_bonus = elemental_dmg_bonus
        self.atk_speed_bonus = atk_speed_bonus
        self.crit_chance_bonus = crit_chance_bonus
        self.armor_bonus = armor_bonus
        self.dodge_bonus = dodge_bonus
        self.luck_bonus = luck_bonus
        if image_path is not None:
            self.image = pygame.image.load(image_path).convert_alpha()