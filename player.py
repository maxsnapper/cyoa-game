# Filename: player.py

class Player(object):
	
	def __init__(self, game):
		''' initialize the player '''
		self.game = game
		self.username = ''
		self.health = 100
		self.treasure = {'gold':0, 'rubies':0, 'diamonds':0}

	def createPlayer(self):
		self.default_username = 'Player'
		''' Setup for the game, obtain username and start the game '''
		print "Hi, what is your name?"
		self.username = raw_input('> ').title()
		# print "You want to set your name as: %s" % self.username
		if(self.username == 'quit' or self.username == 'Quit'):
			self.dead("Exiting, although it's a shame you didn't even start the game!", False)
		elif(self.username == '' or self.username == ' '):
			print "What's in a name anyways"
			print "Instead I will call you, %s" % self.default_username
			self.username = self.default_username 
		print "Thanks %s" % self.username

	def dead(self, reason = 'Being plain silly', try_again = True):
		''' Player has died '''
		print reason
		if(try_again):
			self.try_again()
		else:
			exit(0)

	def try_again(self):
		print "-" * 20
		question = "%s did you want to play again? (Y/N)" % self.username
		play_again = self.game.ask_question( options=['Yes', 'No'], question=question )
		if(play_again == 'y' or play_again == 'Y'):
			self.game.play()
		else:
			exit(0)

