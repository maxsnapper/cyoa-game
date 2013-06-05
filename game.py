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
        self.extras = []
        self.maps = Maps(game=self)
        self.screen = pygame.display.set_mode((self.maps.width, self.maps.height))
        self.player = Player(game=self)
        pygame.display.set_caption('Game')
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
        update_rects = [self.player.rect]
        for room in self.player.open_rooms:
            self.screen.fill((60, 60, 60), room.rect)
            pygame.draw.rect(self.screen, room.color, room.rect, 1)
            update_rects.append(room.rect)
            for door in room.doors:
                pygame.draw.rect(self.screen, door.color, door.rect)
                update_rects.append(room.rect)
        pygame.draw.rect(self.screen, (255, 200, 0), self.player.rect)
        pygame.display.update(update_rects)
#        self.player.imageRect = pygame
        self.screen.blit(self.player.image, (40, 40))
        pygame.display.flip()

    def key_action(self, key):
        if key == pygame.K_LEFT:
            self.player.move(-1, 0)
        elif key == pygame.K_RIGHT:
            self.player.move(1, 0)
        elif key == pygame.K_UP:
            self.player.move(0, -1)
        elif key == pygame.K_DOWN:
            self.player.move(0, 1)
        elif key == pygame.K_o or key == pygame.K_SPACE:
            self.player.open_door()
        elif key == pygame.K_r:
            print "Reloading Map"
            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            self.player = self.maps = None
            self.maps = Maps(game=self)
            self.player = Player(game=self)
        elif key == pygame.K_h:
            self.help_screen()
        elif key == pygame.K_l:
            print "List Open Rooms"
            for room in self.player.open_rooms :
                print "room: %r" % (room)

    def help_screen(self):
        print ""
        print "-" * 20
        print "Show the help screen"
        print "Use the arrow keys to navigate around the character around the map"
        print ""

if __name__ == "__main__":
    Main()
