# Filename: rooms.py
from random import randint
import sys
from map import Map

class Rooms(object):
	
	def __init__(self, game):
		''' initialize the room '''
		self.game = game
		self.room_name = ''
		self.next_room = ''
		self.map = Map(game=self)

        def move_to_room(self, room_name):
                print "You have entered the %s room" % self.rename(room_name)
		themes = [
			'Dark room',
			'Lovely room',
			'Treasure room',
			'Cold and smelly room'
			]

		theme = randint( 0, len(themes)-1 )
                question = "You find yourself in a %s. As you look around you find an orc asleep, what would you like to do?" % themes[theme]
                options = [ "Run", "tread carefully around orc", "slap the orc" ]
		self.game.ask_question(question=question, options=options)
#                exit()

	def create(self):
		name=''
		size={ 'x': randint(5,10) , 'y': randint(5,10) }
		location = {'x': randint(1, (self.map.width-size['x']) ), 'y': randint(1,(self.map.height-size['y']) ) }
		items={
			'door': {
				'type':'door',
				'location': {'x': location['x'],
					     'y': randint(1, size['y']-1 )+(location['y']) },
				 'size': {'x': 1, 'y':1} 
			}
		}
		room = {'size': size, 'location': location, 'name': name, 'type':'room' }
		self.map.add_item(room)
		self.map.add_item(items['door'])
		self.map.draw()

        def rename(self, room_name):
                new_room_name = room_name.upper()
                return new_room_name


