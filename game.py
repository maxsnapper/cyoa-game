# Filename: game.py
#imports
from rooms import Rooms
from player import Player

class Game(object):
	''' Main game controller '''
	def __init__(self):
		''' Setup the game object'''
		self.player = Player(game=self) 
		self.room = Rooms(game=self)
		self.last_question = ''
		#if(self.player.username == ''):
		#	self.player.createPlayer()
			

	def play(self):
		''' Starting the game '''

		try:
			print "Let's play!"
			question = 'Which way would you like to go? Left or Right?'
			choice = self.ask_question( options=['Left', 'Right'], question=question)
			if(choice == 1):
				next_room = "left"
			elif(choice == 2):
				next_room = "right"
			else:
				self.player.dead("Well that was daft, you died")
		
			print "move onto the %s room" % next_room
			self.room.move_to_room(next_room)
		
		except KeyboardInterrupt:
			self.player.dead("Quitter, you will never know how it finishes!", False)


	def ask_question(self, options = {'y': True, 'n': False, 'quit': 'quit'}, prompt='> ', question='', fail_count=0):
		''' Custom input retrieval to help clean up inputs
			Allows for a quit '''
		### kill the player off because they don't type an appropriate choice
		if(fail_count > 5):
			self.player.dead("You died as you made too many mistakes!")
		option_count = len(options)
		self.last_question = question
		print "%s\n" % question
		counter = 1
		### loop through the options and display them
		for option in options:	
			print "\t[%s] %s" % (counter, option)
			counter = counter + 1
		### display the other options such as quit and help.
		print "\n\t[h] Help"
		print "\t[q] Quit"
#		print "\t[hp] Check health"
#		print "\t[gc] Check gold"
		input_data = raw_input(prompt)
		
		### Options to run other actions
		if(input_data == 'quit' or input_data == 'q'):
			self.player.dead("Quitter, you will never know how it finishes!", False)
		elif(input_data == 'help' or input_data == 'h'):
			self.help_files()
			self.ask_question(options=options, prompt=prompt, question=self.last_question)
		else:
			try: 
				input_data = self.check_input(input_data, option_count)
				return input_data
			except ValueError:
				print "Not a valid input, please try again"
				self.ask_question(options=options, prompt=prompt, question=self.last_question, fail_count=fail_count+1)
		

	def check_input(self, value, count):
		value = int(value)
		count = int(count)
		if(type(value) == int and value <= count):
			return value
		else:
			raise ValueError("%s is not a valid number")

	def escape(self):
		''' Player has managed to find their way out '''
		print "Congratulations %s, you managed to escape" % self.player.username
		print "You Win!!!"
		self.player.try_again()

	def help_files(self):
		print "-" * 20
		print "Help Files"
		print "-" * 20
		print "When asked any question you can run any of the following commands"
		print "\t help \t\t show this help"
		print "\t quit \t\t Exit out of the game regardless where you are"
		print "\t rename \t Rename your existing character\n"
		print "\t check \t\t get info for some things"
		print "\t\t health \t get amount of health"
		print "\t\t gold \t\t get amount of gold"
		print "\n"
		

game = Game()
game.play()
