# Filename: map.py
import sys

class Map(object):
	
	def __init__(self, game):
		''' initialize the map '''
		self.key = {
			'door':'+',
			'wallX':'-',
			'wallY':'|',
			'floor':'.',
			'empty':'',
			'player':'@'
			}
		self.game = game
		self.width = 80
		self.height = 23
#		self.layout = [ ['@'] * self.height ] * self.width
		self.layout = []
		for i in range(self.height): self.layout.append([self.key['empty']] * self.width)
#		print "layout is: %s" % self.layout

	def add_item(self, item=[]):
		if ( item['type'] == 'door' ):
			self.game.map.layout[ item['location']['y']-1 ][ item['location']['x']-1 ] = self.key['door']
		elif (item['type'] == 'room'):
			for y in xrange(item['size']['y']):
				locationY = ( item['location']['y'] + y )-1
				for x in xrange(item['size']['x']):
					locationX = (item['location']['x'] + x) - 1
					if(y == 0 or y == item['size']['y']-1):
						self.game.map.layout[locationY][locationX] = self.key['wallX']
					else:
						if(x == 0 or x == item['size']['x']-1):
							self.game.map.layout[locationY][locationX] = self.key['wallY']
						else:
							self.game.map.layout[locationY][locationX] = self.key['floor']
		else:
			# to be added later
			pass
	
	def draw(self):
		for y in self.layout:
			for x in y:
				sys.stdout.write(x)
			sys.stdout.write("\n")
