import pygame
from pygame.locals import *

class Player(object):

    def __init__(self, game):
	self.game = game
        self.rect = pygame.Rect(30, 30, 10, 10)

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx*10, 0)
        if dy != 0:
            self.move_single_axis(0, dy*10)
 
    def move_single_axis(self, dx, dy):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy
        # If you collide with a wall, move out based on velocity
        for wall in self.game.maps.walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

