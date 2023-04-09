import pygame
from settings import *
from support import *
from tile import Tile
from character import Player
from enemy import Enemy

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = CameraGroup()
        self.upper_sprites = CameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        tileset = pygame.image.load('../assets/map/tiles.png')
        layout = {
            'boundary': import_csv_layout('../map/FunMap_boundary.csv'),
            'objects' : import_csv_layout('../map/FunMap_objects.csv'),
            'upper' : import_csv_layout('../map/FunMap_upper.csv')
        }
        
        for style, layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary' or style == 'objects':
                            Tile((x,y), [self.obstacle_sprites], 'invisible')

                        # Parts that need to be over the player
                        if style == 'upper':
                            if col == '540':
                                Tile((x,y),[self.visible_sprites], 'upper', tileset.subsurface(pygame.Rect(1836, 612, TILESIZE, TILESIZE)))
                            elif col == '593':
                                Tile((x,y),[self.visible_sprites], 'upper', tileset.subsurface(pygame.Rect(1564, 680, TILESIZE, TILESIZE)))
                            elif col == '586':
                                Tile((x,y),[self.visible_sprites], 'upper', tileset.subsurface(pygame.Rect(1088, 680, TILESIZE, TILESIZE)))
                            elif col == '583':
                                Tile((x,y),[self.visible_sprites], 'upper', tileset.subsurface(pygame.Rect(884, 680, TILESIZE, TILESIZE)))

        # Spawn Player and Enemies
        self.player = Player((800,800),[self.visible_sprites])
        enemy = Enemy([self.visible_sprites])
        enemy2 = Enemy([self.visible_sprites])
        enemy2.rect = enemy2.image.get_rect(center = (700,700))
        enemy3 = Enemy([self.visible_sprites])
        enemy3.rect = enemy3.image.get_rect(center = (1000,1000))
        enemy4 = Enemy([self.visible_sprites])
        enemy4.rect = enemy4.image.get_rect(center = (700,1000))

    def run(self):
        # Move player and redraw the screen
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2
        self.offset = pygame.math.Vector2()
        
        self.surf = pygame.image.load('../assets/map/FunMap.png').convert()
        self.rect = self.surf.get_rect(topleft=(0,0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.rect.topleft - self.offset
        self.display_surface.blit(self.surf, floor_offset_pos)

        # Draw everything
        for sprite in self.sprites():
                offset_pos = sprite.rect.topleft - self.offset  
                self.display_surface.blit(sprite.image, offset_pos)

        # Draw the always visible
        for sprite in self.sprites():
            if hasattr(sprite, "sprite_type") and sprite.sprite_type == "upper":
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
