""" ===		World 		==="""

all_places = []
all_x = []
all_y = []
all_cities_x = []
all_cities_y = []

class place(object):
	"""	Base Class for all locations		"""
	def __init__(self, name, descrip, city, x, y):
		self.name = name
		self.descrip = descrip
		self.x = x
		self.y = y
		self.city = city
		all_places.append(self)
		
		
	def inquire(self):
		return "{}\n ========\n{}\n\nLocation: ({},{})\n".format(self.name, self. descrip, self.x, self.y)

mando = place("Mandonia",
	"The main trading hub of this area, This is where King Todd sits upon his throne",
	city = True,
	x = 1, y = 1
	)

elf_place = place("Strukes city", 
	"Rope bridges string each building together in this city hanging off the \ncliffside overlooking the great Calipran Sea.",
	city = True,
	x = 15, y = 1
	)
	
port_city = place("Portside city",
	"A creatively named port place. All trade routes out come through this seaside town.",
	city = True,
	x = 15 ,y = 5 
	)

dwarf_north = place("Azkabar (North)",
	"An underground cave system transformed by Dwarves into a metropolis of weapon crafting.",
	city = True,
	x = 10, y = 15
	)
	
dwarf_south = place("Azkabar (South)",
	"An underground cave system transformed by Dwarves into a metropolis of weapon crafting.",
	city = True,
	x = 10, y = 5
	)
	
island_paradise = place("Easter Island",
	"Known by the first word spoken by the primitave natives, this island paradise is named after and expression of confusion.",
	city = True,
	x = 20, y = 20
	)

	
wicked = place("Witches Shack",
	"A small hut in the woods known to house a witch with control over magics of all kind.",
	city = False,
	x = 6, y = 15
	)
	
demon_pit = place("Demon Pitt",
	"Demons who escape the underworld find themselves in this pseudo-underworld.",
	city = False,
	x = 7, y = 5
	)

fork = place("Fork in the Road",
	"Two signs show. To the north, a sign reads 'There be Dragons', and to the east, 'Azkabar'",
	city = False,
	x = 1, y = 15
	)
		
dragon_lair = place("Dragon's Lair",
	"A large dragon holds onto King Todd's Macguffin. This is the treasure you seek.",
	city = False,
	x = 1, y = 20
	)

all_coords = []
	
for item in all_places:
	all_coords.append([item.x, item.y])

for item in all_places:
	all_x.append(item.x)
	all_y.append(item.y)
	
for item in all_places:
	if item.city == True:
		all_cities_x.append(item.x)
		all_cities_y.append(item.y)