import pygame

class Player(object):

    def __init__(self, game):
        self.game = game
        self.rect = pygame.Rect(30, 30, 10, 10)
        self.room = self.in_room()

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx*10, 0)
        if dy != 0:
            self.move_single_axis(0, dy*10)
 
    def move_single_axis(self, dx, dy):
        allow_move = False
        is_door = False
        room  = self.in_room()
        on_door = None
        for door in room.doors:
            if door.rect.contains(self.rect):
                on_door = door
                break
            else:
                pass
        self.move_character(dx, dy, door)

    def move_character(self, dx, dy, on_door):
        old_location = {'x': self.rect.x, 'y': self.rect.y}
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
        
        if self.in_room() != self.room and (not on_door or on_door.closed):
            self.rect.x = old_location['x']
            self.rect.y = old_location['y']
        self.room = self.in_room()

    def in_room(self):
        rtn_room = None
        for room in self.game.maps.rooms:
            room.color = (255, 255, 255)
            if room.rect.contains(self.rect):
                room.color = (90, 90, 90)
                rtn_room = room
        return rtn_room

    def open_door(self):
        for door in self.room.doors:
            if door.rect.contains(self.rect):
                door.action()

       
