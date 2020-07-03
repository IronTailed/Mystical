#Locations.py
class Location:
	def __init__(self):
		pass

class Field(Location):
	def __init__(self):
		self.name = 'field'
		self.lvl_req = 0
		self.adjacent = ['road']
		self.NPC = None

class Road(Location): 
	def __init__(self):
		self.name = 'road'
		self.lvl_req = 0
		self.adjacent = ['field', 'forest']
		self.NPC = ['old man']


class Forest(Location):
	def __init__(self):
		self.name = 'forest'
		self.lvl_req = 5
		self.adjacent = ['road', 'cave']
		self.NPC = None

class Cave(Location):
	def __init__(self):
		self.name = 'cave'
		self.lvl_req = 20
		self.adjacent = ['forest', 'otherworld' ]
		self.NPC = None

class Otherworld(Location):
	def __init__(self):
		self.name = 'otherworld'
		self.lvl_req = 35
		self.adjacent = ['forest', 'throne']
		self.NPC = None

class Throne(Location):
	def __init__(self):
		self.name = 'throne'
		self.lvl_req = 50
		self.adjacent = ['otherworld']
		self.NPC = None

