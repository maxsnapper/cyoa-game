import pygame
from random import randint

class Maps(object):

    def __init__(self, game):
        self.game = game
        self.width = 400
        self.height = 300
        self.walls = []
        self.level = []
        self.rooms = []
        self.doors = []
        self.room_count = randint(20, 25)
        self.min_room_area = 2500
        self.min_room_size = 50
        self.multiplier = 10
        self.game.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Choose your own Adventure game!')
        self.generate(game)
    
    def generate(self, game):
        new_room = Rooms(game, 0, 0, self.width, self.height, 0)
        self.rooms.append(new_room)
        skipped_rooms = []
        counter = 0
        #while len(self.rooms) < self.room_count:
        while (len(self.rooms) >= len(skipped_rooms) and
            len(self.rooms) <= self.room_count):
            i = randint(0, len(self.rooms)-1)
            room = self.rooms[i]
            if room not in skipped_rooms:
                is_skipped = self.split_rooms(game, room)
                if is_skipped:
                    skipped_rooms.append(room)
                    if (len(skipped_rooms) >= len(self.rooms) or
                        counter >= self.room_count*2):
                        break
            counter += 1
        x = y = 0
        for room in self.rooms:
            room.rect = pygame.Rect(room.x, room.y, room.width, room.height)
        self.generate_doors()
        for door in self.doors:
            door.rect = pygame.Rect(door.x, door.y, door.width, door.height)

    def split_rooms(self, game, room):
        if (room.area() > self.min_room_area and
            (room.width*2 > self.min_room_size) and
            (room.height*2 > self.min_room_size)):
            split_direction = randint(1, 2)
            if split_direction == 1: # Split along X
                if (room.width-self.min_room_size > self.min_room_size and
                    room.area() >= self.min_room_area):
                    old_width = room.width
                    new_width = randint(self.min_room_size, (old_width-self.min_room_size))
                    new_width = int(round(new_width/10)*10)
                    if ((room.height * new_width) >= self.min_room_area and 
                        (room.height * (old_width - new_width)) > self.min_room_area):
                        room.resize(new_width, room.height)
                        new_room = Rooms(game, (room.x + new_width), room.y, (old_width - new_width), room.height, len(self.rooms))
                        self.rooms.append(new_room)
            else: 
                split_direction = 2
                if split_direction == 2: # Split along Y
                    if ((room.height-self.min_room_size > self.min_room_size and
                        room.area() >= self.min_room_area)):
                        old_height = room.height
                        new_height = randint(self.min_room_size, (old_height - self.min_room_size))
                        new_height = int(round(new_height/10)*10)
                        if ((room.width * new_height) > self.min_room_area and
                            (room.width * (old_height - new_height)) > self.min_room_area):
                            room.resize(room.width, new_height)

                            new_room = Rooms(game, room.x, (room.y + new_height), room.width, (old_height - new_height), len(self.rooms))
                            self.rooms.append(new_room)
                    else:
                        return True
            return False
        else:
            return True

    def generate_doors(self):
        #room1 = self.rooms[4];
        for room1 in self.rooms:
            for room2 in self.rooms:
                x = None
                y = None
                if ((room1.y2 == room2.y) or 
                    (room1.y == room2.y2)):
                    if room1.y2 == room2.y:
                        y = room1.y2
                    else:
                        y = room1.y
                    if (room1.x <= room2.x and 
                        room1.x2 >= room2.x2): 
                        # bigger than original box
                        if (room2.x2 - room2.x) >= 50 :
                            x = (room2.x + room2.x2)/2
                    elif (room1.x >= room2.x and 
                        room1.x2 <= room2.x2): 
                        # smaller than original box
                        if (room1.x2 - room1.x) >= 50:
                            x = (room1.x + room1.x2)/2
                    elif (room1.x >= room2.x and 
                        room1.x < room2.x2 and 
                        room1.x2 >= room2.x2):
                        # overlaps and to the left of original room
                        if room2.x2 - room1.x >= 50:
                            x = (room1.x + room2.x2)/2
                    elif (room1.x <= room2.x and 
                        room1.x2 > room2.x and 
                        room1.x2 <= room2.x2): 
                        # overlaps and to the right of the original room
                        if (room1.x2 - room2.x) >= 50:
                            x = (room2.x + room1.x2)/2
                    if x :
                        room1.attached.append(room2)
                        room2.attached.append(room1)
                        new_door = Doors(self.game, x, y, (room1, room2), len(self.doors), (255, 0, 0))
                        if not (new_door.is_duplicate(self.doors)):
                            self.doors.append(new_door)
                        else:
                            new_door = None
        print "room: %s, <x=%s; x2=%s; y=%s; y2=%s> <w=%s; h:%s>" % (room1.room_id, room1.x, room1.x2, room1.y, room1.y2, room1.width, room1.height)
        print "doors: %s to rooms: %s" % (len(self.doors), len(self.rooms))
        print "number of doors created: %s" % len(self.doors)

class Rooms(object):
    def __init__(self, game, x, y, width, height, room_id=0):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = ''
        self.x2 = x + width
        self.y2 = y + height
        self.room_id = room_id
        self.attached = []

    def resize(self, width, height):
        self.width = width
        self.height = height
        self.x2 = self.x + self.width
        self.y2 = self.y + self.height

    def area(self):
        return self.width * self.height

class Doors(object):
    def __init__(self, game, x, y, rooms, door_id=0, color=(0, 0, 255)):
        self.game = game
        self.x = x - 10
        self.y = y - 10
        self.width = 20
        self.height = 20
        self.rect = ''
        self.x2 = self.x + self.width
        self.y2 = self.y + self.height
        self.door_id = door_id
        self.rooms = rooms
        self.room_ids = []
        self.color = color
        for room in self.rooms:
            self.room_ids.append(room.room_id)
            
    def is_duplicate(self, doors):
        is_duplicate = False
        for door in doors:
            if sorted(self.room_ids) == sorted(door.room_ids):
                print "door %s matches %s (%s)<%s>" % (self.door_id, door.door_id, self.room_ids, door.room_ids)
        #print self
                is_duplicate = True
        return is_duplicate

