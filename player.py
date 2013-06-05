""" Player object """
import pygame

class Player(object):
    """ Player object """
    def __init__(self, game):
        """ initialize the players character """
        self.game = game
        self.rect = pygame.Rect(30, 30, 10, 10)
        self.open_rooms = []
        self.room = self.in_room()
        self.open_rooms = [self.room]
        self.image = pygame.image.load('character.png')
        #self.game.screen.blit(self.image, (40, 40))

    def move(self, move_x, move_y, on_door=None):
        """ move the character around the map, 
        checking not going out of bounds 
        or walking through closed doors or walls """
        # increase the step size to compensate for block sizes
        move_x = move_x*10 
        move_y = move_y*10
        old_location = {'x': self.rect.x, 'y': self.rect.y}
        if not (move_x + self.rect.x < 0 or \
            move_x + self.rect.x >= self.game.maps.width):
            self.rect.x += move_x
        if not (move_y + self.rect.y < 0 or \
            move_y + self.rect.y >= self.game.maps.height):
            self.rect.y += move_y
        for door in self.in_room().doors:
            if door.rect.contains(self.rect):
                on_door = door
                break
        if self.in_room() != self.room and \
            (not on_door or on_door.closed):
            if on_door and on_door.closed:
                print "You can't go through here the door is closed!"
                print "You may want to try opening it"
            self.rect.x = old_location['x']
            self.rect.y = old_location['y']
        self.room = self.in_room()
        if (self.room not in self.open_rooms):
            self.open_rooms.append(self.room)

    def in_room(self):
        """ Check if the player is in a room

        return the room object that they are in """
        rtn_room = None
        for room in self.game.maps.rooms:
            room.color = (255, 255, 255)
            if room.rect.contains(self.rect):
                rtn_room = room
        return rtn_room

    def open_door(self):
        """ Check if the player is close enough to a door
        Open the door to the next room """
        for door in self.room.doors:
            if door.rect.contains(self.rect):
                door.action()
       
