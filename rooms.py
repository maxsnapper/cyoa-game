# Filename: rooms.py
class Rooms(object):
	
	def __init__(self, game):
		''' initialize the room '''
		print "setup the room"
		self.game = game
		self.room_name = ''
		self.next_room = ''

        def move_to_room(self, room_name):
                print "You have entered the %s room" % self.rename(room_name)
                question = "As you look around you find an orc asleep, what would you like to do?"
                options = [ "Run", "tread carefully around orc", "slap the orc" ]
		self.game.ask_question(question=question, options=options)
#                exit()

        def rename(self, room_name):
                new_room_name = room_name.upper()
                return new_room_name

	
