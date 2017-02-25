import pygame as pg
from GameConstants import *

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.wall
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(COLOR_BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
class Water(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.water
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(COLOR_BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
  
class Mountain(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mountain
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(COLOR_BABY_BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
class Player(pg.sprite.Sprite):
   def __init__(self, game, x, y):
       self.groups = game.all_sprites
       pg.sprite.Sprite.__init__(self, self.groups)
       self.game = game
       self.image = pg.Surface((TILESIZE, TILESIZE))
       self.image.fill(COLOR_PURPLE)
       self.rect = self.image.get_rect()
       self.x = x
       self.y = y
 
   def move(self, dx=0, dy=0):
       if not self.collide_detection(dx, dy):
           self.x += dx
           self.y += dy
 
   def collide_detection(self, dx=0, dy=0):
       for m in self.game.wall:
           if m.x == self.x + dx and m.y == self.y + dy:
               return True       
       for m in self.game.water:
           if m.x == self.x + dx and m.y == self.y + dy:
               return True
       return False
 
   def update(self):
       self.rect.x = self.x * TILESIZE
       self.rect.y = self.y * TILESIZE       

