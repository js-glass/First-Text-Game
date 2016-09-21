'''	===		Items	==='''
import random
all_items = []
all_weaps = []

class item(object):
	"""Base Class for all items"""
	def __init__(self, name, descrip, quanity, speed, value, unique):
		self.name = name
		self.descrip = descrip
		self.quanity = quanity
		self.speed = speed
		self.value = value
		self.equippable = False
		self.unique = unique
		all_items.append(self)
		
	def inquire(self):
		return "{}\n========== \n{}\n    Value = {}\n".format(self.name, self.descrip,  self.value)
	
class weapon(item):
	"""		Subclass of item that is used as weapon	"""
	def __init__(self, name, descrip, quanity, speed, value, damage, unique):
		self.name = name
		self.descrip = descrip
		self.quanity = quanity
		self.speed = speed
		self.value = value
		self.damage = damage
		self.unique = unique
		self.demonic = False
		self.equippable = True
		all_weaps.append(self)
		all_items.append(self)
		
	def inquire(self):
		if self.demonic == False:
			return "{}\n==========\n{}\n    speed = {}\n    Damage = {}\n    Value = {}\n".format(self.name,self.descrip, self.speed, self.damage, self.value)
		elif self.demonic == True:
			return "Demonic {}\n==========\n{}\n    speed = {}\n    Damage = {}\n    Value = {}\n".format(self.name,self.descrip, self.speed, self.damage, self.value)
		
	def infuse(self):
		self.demonic = True
		self.speed = self.speed *2
		self.damage = self.damage *2
		self.value = self.value * 2
		
		
class gold(item):
	"""		Subclass of item that is MMMmmmmmoney		"""
	def _init__(self, name, descrip, quanity):
		self.name = name
		self.descrip = descrip
		self.quanity = quanity
		self.equippable = True
		all_items.append(self)

	def add_gold(self, amt):
		self.amt = amt
		self.quanity = self.quanity + amt
		
	def sub_gold(self, amt):
		self.amt = amt
		self.quanity = self.quanity - amt
		
	def inquire(self):
		return "{}\n=========\n{}\n    You have {} Gold coins\n".format(self.name,self.descrip,self.quanity)

'''===		Weapons		==='''

fists = weapon("Fists",
	"Your Bare Hands!!!",
	quanity = 0, speed = 5, value = 0, damage = 5,
	unique = True,
	)
		
sword_1 = weapon("Broadsword",
	"The steel glistens in the sunlight",
	quanity=1, speed = 15, value=100, damage=20,
	unique = False,
	)

sword_2 = weapon("Longsword",
	"A thin, narrow, and long blade. Perfect for a knight",
	quanity=0, speed = 10, value=115, damage=25,
	unique = False,
	)
	
spear = weapon("Spear",
	"Sharpened metal point on the end of a long staff.",
	quanity = 0, speed = 15, value = 110, damage = 20,
	unique = False,
	)

flail = weapon("Flail",
	"A spikey metal ball and a handle strung together with a thick metal chain.",
	quanity = 0, speed = 20, value = 130, damage = 30,
	unique = False,
	)
	
mace = weapon("Mace",
	"Spiked ball at the end of a handle.",
	quanity = 0, speed = 15, value = 125, damage = 20,
	unique = False,
	)
	
hammer = weapon("Blacksmith's Hammer",
	"A hammer intended for the forming of metal, not the deforming of enemies.",
	quanity = 0, speed = 20, value = 90, damage = 10,
	unique = False,
	)
	
battle_hammer = weapon("Battle Hammer",
	"A Hammer designed with bashing skulls in mind.",
	quanity = 0, speed = 10, value = 130, damage = 30,
	unique = False,
	)
	
dougsword = weapon("Sword of Douglas",
	"This ledgendary blade is the only of it's kind. \nForged in the flames of Douglas, \nthe Payne it can bring is extraordinary",
	quanity = 0, speed = 15, value = 250, damage = 30,
	unique = True,
	)
	
axe_1 = weapon("Waraxe",
	"This double bladed weapon is meant for agile warriors.",
	quanity=0, speed = 30, value=100, damage=15,
	unique = False,
	)

axe_2 = weapon("Battlexe",
	"Slow-swinging speed does great damage, but is also extremely heavy.",
	quanity=0, speed = 5, value=150, damage=35,
	unique = False,
	)
	
karls_axe = weapon("65' Berretta",
	"This gun is not a gun, but instead actually an axe.",
	quanity= 0, speed = 15, value = 125, damage = 25,
	unique = True,
	)
	
genes_axe = weapon("Gene Simmons' Axe",
	"Strings made from Demon veins run across this weapon, when used it screams with the voice of a thousand sexy sirens.",
	quanity = 0, speed = 20, value = 300, damage = 50,
	unique = True,
	)
	
connor_sword = weapon("Sidewinder",
	"Long curved blade passed down from the father of that one dude who couldn't fight.",
	quanity = 0, speed = 15, value = 200, damage = 40,
	unique = True,
	)
	
gold_blade = weapon("Blade of Pure Gold",
	"A blade forged from pure Gold. Worth a lot, but not very practical for battle.",
	quanity = 0, speed = 10, value = 5000, damage = 5,
	unique = True,
	)

demon_pock_watch = weapon("Pocket Watch",
	"Infused with demon essence, and your own sentimental value, your pocket watch has become a powerful weapon.",
	quanity = 0, speed = 25, value = 250, damage = 50,
	unique = True
	)
demon_pock_watch.infuse()			#Weapon only exists in demonic form.

dwarf_axe = weapon("Dwarven Axe",
	"Oversized axe forged by the smith at Azkabar.",
	quanity = 0, speed = 15, value = 200, damage = 30,
	unique = True
	)
	
elf_sword = weapon("Elven Sword",
	"Long and sleek blade forged by the smith at Strukes City.",
	quanity = 0, speed = 25, value = 200, damage = 25,
	unique = True
	)

'''===		Items		==='''
pock_watch = item("Pocket Watch",
	"This pocket watch may not be worth much to others, but to you it holds value.",
	quanity = 1, speed = 1, value = 10,
	unique = True
	)
	
pearl = item("Pearl",
	"This shiny pearl should catch a nice price at the market.",
	quanity = 0, speed = 1, value = 100,
	unique = False
	)
	
paintbrush = item("Paintbrush",
	"Small thin paintbrush with golden colored bristles.",
	quanity = 0, speed = 1, value = 10,
	unique = False
	)
	
broom = item("Broom",
	"A wooden handle with straw tied to one end. Come on, you know what a broom looks like.",
	quanity = 0, speed = 1, value = 20,
	unique = False
	)
	
bottle = item("Empty Wine Bottle",
	"An empty bottle of wine.",
	quanity = 0, speed = 1, value = 10,
	unique = False
	)
	
cup = item("Cup",
	"Container used for holding small amounts of liquid.",
	quanity = 0, speed = 1, value = 10,
	unique =  False
	)
	
iron = item("Iron Ingot",
	"Used in the construction of weapons and armor.",
	quanity = 0, speed = 1, value = 30,
	unique = False
	)
	
amythest = item("Amythest",
	"A shiny purpleish gem.",
	quanity = 0, speed = 1, value = 100,
	unique = False
	)
	
garnet = item("Garnet",
	"Shiny red and valuable.",
	quanity = 0, speed = 1, value = 75,
	unique = False
	)
	
ppr_clip = item("Paper Clip",
	"This item appears to be a complete anacronism,\n no one made paper clips in medievil high fantasy times.",
	quanity = 0, speed = 1, value = 0,
	unique = False
	)
	
demons_blood = item("Demon's Blood",
	"Small vial containing the blood of a demon.",
	quanity = 0, speed = 1, value = 25,
	unique = True
	)
	
drill = item("Drill",
	"A small drill, looks a bit out of place here.",
	quanity = 0, speed = 1, value = 50,
	unique = False
	)
	
bucket = item("Bucket",
	"Used for holding large quanities of various liquids.",
	quanity = 1, speed = 1, value = 50,
	unique = False
	)
	
bowl = item("Bowl",
	"Used for holding a medium quanity of various liquids. Usually edible.",
	quanity = 1, speed = 1, value = 20,
	unique = False
	)

spoon = item("Spoon",
	"Just a regular old spoon.",
	quanity = 0, speed = 1, value = 10,
	unique = False
	)

fork = item("Fork",
	"Just a regular old fork.",
	quanity = 0, speed = 1, value = 10,
	unique = False
	)

spork = item("Spork",
	"Being a spoon and a fork combined, you would think it would be worth the values combined.",
	quanity = 0, speed = 1, value = 5,
	unique = False
	)
	
plumbus = item("Plumbus",
	"Just a regular old Plumbus. I wonder how these things are made.",
	quanity = 0, speed = 1, value = 25,
	unique = False
	)

demon_essence = item("Demon Essence",
	"Magically enhanced Demon's blood.",
	quanity = 0, speed = 1, value = 200,
	unique = True
	)

lucky_feet = item("Lucky Rabbits Foot",
	"This foot raises your luck, or maybe it does nothing.",
	quanity = 0, speed = 0, value = 50,
	unique = False
	)

steven = item("Steven",
	"This is actually a rose quartz gem, but it looks like a kid.",
	quanity = 0, speed = 1, value = 50,
	unique = False
	)
	
wedd_ring_1 = item("Lunk's Wedding ring",
	"Trinket meant to bring back the Witch from her insanity",
	quanity = 0, speed = 1, value = 250,
	unique = True
	)
	
wedd_ring_2 = item("Witch's Ring",
	"The ring kept by the Witch of the Northen Woods.",
	quanity = 0, speed = 1, value = 250,
	unique = True
	)

witch_blood = item("Witch's Blood",
	"From the Witch of the Western Woods, a small vial of blood.",
	quanity = 0, speed = 1, value = 50,
	unique = True
	)
	
macguffin = item("MacGuffin",
	"This MacGuffin can destroy all evil, lighten all darkness, cure the sick,\n and make all evil disapear forever and ever et cetra.",
	quanity = 0, speed = 15, value = 2000,
	unique = True
	)

'''===		Gold		==='''

money = gold("Gold",
	"The shiny shiny coins that make the world go around.",
	quanity = 200, speed =  0, value = 1,
	unique = False
	)
	
'''for item in all_items:
	print(item.inquire())'''