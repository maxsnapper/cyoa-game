# Filename: game.py
import pygame
import sys
from random import randint
from pygame.locals import *
from player import Player
from maps import *

class QuitGame(Exception):
    pass

class Main():
    def __init__(self):
        pygame.init()
        self.player = Player(game=self)
        self.maps = Maps(game=self)
        self.play()

    def play(self):
        playing = True
        while playing:
            try:
                for event in pygame.event.get():
                    #if self.player.rect.colliderect(self.maps.end_rect):
                    #raise SystemExit("You win!")
                    if (event.type == QUIT or
                        (event.type == KEYDOWN and event.key == pygame.K_q)):
                       raise QuitGame()
                    elif event.type == KEYDOWN:
                        #print pygame.key.get_pressed()
                        if pygame.key.get_pressed()[K_LEFT]:
                            self.player.move(-1, 0)
                        elif pygame.key.get_pressed()[K_a]:
                            self.player.move(-0.5, 0)
                        elif pygame.key.get_pressed()[K_RIGHT]:
                            self.player.move(1, 0)
                        elif pygame.key.get_pressed()[K_d]:
                            self.player.move(0.5, 0)
                        elif pygame.key.get_pressed()[K_UP]:
                            self.player.move(0, -1)
                        elif pygame.key.get_pressed()[K_w]:
                            self.player.move(0, -0.5)
                        elif pygame.key.get_pressed()[K_DOWN]:
                            self.player.move(0, 1)
                        elif pygame.key.get_pressed()[K_s]:
                            self.player.move(0, 0.5)
                        elif pygame.key.get_pressed()[K_l]:
                            print "List Doors"
                            for door in self.maps.doors :
                              print "door: %i: %s -- %s" % (door.door_id, list(door.room_ids), list(door.rect))
                        elif pygame.key.get_pressed()[K_r]:
                            print "\n\n\n\n"
                            self.player = Player(game=self)
                            self.maps = Maps(game=self)
                    else:
                        pass
                self.screen.fill((0,0,0))
                #for wall in self.maps.walls:
                #    pygame.draw.rect(self.screen, (255,255,255), wall.rect)
                #pygame.draw.rect(self.screen, (255, 0, 0), self.maps.end_rect)
                for room in self.maps.rooms:
                    pygame.draw.rect(self.screen, (255,255,255), room.rect,1)
                for door in self.maps.doors:
                    pygame.draw.rect(self.screen, door.color, door.rect)
                pygame.draw.rect(self.screen, (255,200,0), self.player.rect)
                pygame.display.flip()
            except (QuitGame, KeyboardInterrupt, SystemExit):
                playing = False
                print "\nQuitter! you will never see how this finishes!"
            finally:
                pass

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Main()
