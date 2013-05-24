import pygame
#from pygame.locals import *

class Player(object):

    def __init__(self, game):
        self.game = game
        self.rect = pygame.Rect(30, 30, 10, 10)
        self.in_room = None

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx*10, 0)
        if dy != 0:
            self.move_single_axis(0, dy*10)
 
    def move_single_axis(self, dx, dy):
        # If you collide with a wall, move out based on velocity
        if dx + self.rect.x <= 0: 
            self.rect.x = 0
        elif dx + self.rect.x >= self.game.maps.width:
            self.rect.x = self.game.maps.width-10
        else: 
            self.rect.x += dx

        if dy + self.rect.y <= 0: 
            self.rect.y = 0
        elif dy + self.rect.y >= self.game.maps.height:
            self.rect.y = self.game.maps.height-10
        else:
            self.rect.y += dy
        for room in self.game.maps.rooms:
            if room.rect.contains(self.rect):
                if room.room_id != self.in_room:
                    print "ROOM id: %s, %s" % (room.room_id, room.rect)
                self.in_room = room.room_id
        for door in self.game.maps.doors:
            if door.rect.contains(self.rect):
                print "DOOR: id: %s, %s, %s" % (door.door_id, door.rect, list(door.room_ids))
        
