import pygame
from random import randint
from pygame.locals import *

class Maps(object):

    def __init__(self, game):
        self.game = game
        self.width = 800
        self.height = 400
        self.walls = []
        self.level = []
	self.rooms = []
        self.room_count = randint(8,20)
	self.min_room_area = 1000
        #for i in range(self.height): self.level.append(' ' * self.width)
	self.generate(game)
        
        # Parse the level string above. W = wall, E = exit
#	x = y = 0
#	for row in self.level:
#	    for col in row:
#		if col == "W":
#		    Wall((x, y), game=self)
#		if col == "E":
#		    self.end_rect = pygame.Rect(x, y, 10, 10)
#		x += 10
#	    y += 10
#	    x = 0
    def generate(self, game):
        first = Rooms(game, 0, 0, self.width, self.height)
        self.rooms.append(first)
        while len(self.rooms) < self.room_count:
            i = randint(0, len(self.rooms)-1)
            room = self.rooms[i]
            if room.area() > self.min_room_area:
               split_direction = randint(1,2)
               #split_direction = 1
               if split_direction == 1: # Split along X
                   if room.height <= 50:
                       pass
                   else:
                       old_width = room.width
                       new_width = randint(old_width/3, old_width/3*2)
                       if (room.height * new_width) < self.min_room_area or (room.height * (old_width - new_width)) > self.min_room_area:
                           pass
                       room.width = new_width
                       new_room = Rooms(game, (room.x + new_width), room.y, (old_width - new_width), room.height)
                       self.rooms.append(new_room)
               elif split_direction == 2: # Split along Y
                   if room.height <= 50:
                       pass
                   else:
                       old_height = room.height
                       new_height = randint(old_height/3, old_height/3*2)
                       if (room.width * new_height) < self.min_room_area or (room.width * (old_height - new_height)) > self.min_room_area:
                           pass
                       room.height = new_height
                       new_room = Rooms(game, room.y, (room.y + new_height), room.width, (old_height - new_height))
                       self.rooms.append(new_room)
	for room in self.rooms:
            room.rect = pygame.Rect(room.x, room.y, room.width, room.height)
        print self.level
            

class Wall(object):
    def __init__(self, pos, game):
        game.walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)

    def create_room(self, player=None):
        size = {'x': (randint(5,10)*10), 'y': (randint(5,10)*10)}
        location = {'x': 0, 'y':0}
        wallRect = pygame.Rect(location['x'], location['y'], 100, 100)

class Rooms(object):
    def __init__(self, game, x, y, width, height):
	self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height
	self.rect = ''

    def area(self):
        return self.width * self.height

    def render(self, rooms, x, y):
        for i in xrange(0, y+1):
            self.maps.layout.append([' '] * self.width)
        for room in rooms:
            for x in xrange(0, self.width):
                self.layout[room.y][room.x + x] = '#'
                self.layout[room.y + self.height][room.x + x] = '#'
            for y in xrange(0, self.height):
                self.layout[room.y + y][room.x] = '#'
                self.layout[room.y + y][room.x + self.width] = '#'

