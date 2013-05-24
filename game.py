# Filename: game.py
import pygame
import sys
from player import Player
from maps import Maps

class QuitGame(Exception):
    pass

class Main():
    def __init__(self):
        pygame.init()
        self.maps = Maps(game=self)
        self.player = Player(game=self)
        self.screen = pygame.display.set_mode((self.maps.width, self.maps.height))
        self.play()

    def play(self):
        playing = True
        while playing:
            try:
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT or
                        (event.type == pygame.KEYDOWN and event.key == pygame.K_q)):
                        raise QuitGame()
                    elif event.type == pygame.KEYDOWN:
                        self.key_action(event.key)
                    else:
                        pass
                    self.draw_map()
            except (QuitGame, KeyboardInterrupt, SystemExit):
                playing = False
                print "\nQuitter! You will never see how this finishes!"
            finally:
                pass
        pygame.quit()
        sys.exit()

    def draw_map(self):
        self.screen.fill((0, 0, 0))
        for room in self.maps.rooms:
            if room == self.player.in_room():
                pygame.draw.rect(self.screen, room.color, room.rect, 0)
            else:
                pygame.draw.rect(self.screen, room.color, room.rect, 1)
        for door in self.maps.doors:
            pygame.draw.rect(self.screen, door.color, door.rect)
        pygame.draw.rect(self.screen, (255, 200, 0), self.player.rect)
        pygame.display.flip()

    def key_action(self, key):
        if key == pygame.K_LEFT:
            self.player.move(-1, 0)
        elif key == pygame.K_a:
            self.player.move(-0.5, 0)
        elif key == pygame.K_RIGHT:
            self.player.move(1, 0)
        elif key == pygame.K_d:
            self.player.move(0.5, 0)
        elif key == pygame.K_UP:
            self.player.move(0, -1)
        elif key == pygame.K_w:
            self.player.move(0, -0.5)
        elif key == pygame.K_DOWN:
            self.player.move(0, 1)
        elif key == pygame.K_s:
            self.player.move(0, 0.5)
        elif key == pygame.K_l:
            print "List Doors"
            for door in self.maps.doors :
                print "door: %i: %s -- %s" % (door.door_id, list(door.room_ids), list(door.rect))
        elif key == pygame.K_r:
            print "\n\n\n\n"
            self.player = Player(game=self)
            self.maps = Maps(game=self)
        elif key == pygame.K_h:
            self.help_screen()

    def help_screen(self):
        print ""
        print "-" * 20
        print "Show the help screen"


if __name__ == "__main__":
    Main()
