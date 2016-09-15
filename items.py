'''	===		Items	==='''

all_items = []
all_weaps = []

class item(object):
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
	def __init__(self, name, descrip, quanity, speed, value, damage, unique):
		self.name = name
		self.descrip = descrip
		self.quanity = quanity
		self.speed = speed
		self.value = value
		self.damage = damage
		self.unique = unique
		self.equippable = True
		all_weaps.append(self)
		all_items.append(self)
		
	def inquire(self):
		return "{}\n==========\n{}\n    speed = {}\n    Damage = {}\n    Value = {}\n".format(self.name,self.descrip, self.speed, self.damage, self.value)
		
class gold(item):
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
	unique = True
	)
		
sword_1 = weapon("Broadsword",
	"The steel glistens in the sunlight",
	quanity=1, speed = 15, value=100, damage=20,
	unique = False
	)

sword_2 = weapon("Longsword",
	"A thin, narrow, and long blade. Perfect for a knight",
	quanity=1, speed = 10, value=115, damage=25,
	unique = False
	)
	
dougsword = weapon("Sword of Douglas",
	"This ledgendary blade is the only of it's kind. \nForged in the flames of Douglas, \nthe Payne it can bring is extraordinary",
	quanity = 0, speed = 15, value = 250, damage = 30,
	unique = True
	)
	
demon_blade = weapon("Demon Sword",
	"This sword glows red with the power of the Demon who once weilded it.\nIt will make short work of any opponent in the hands of a true hero.",
	quanity = 0, speed = 15, value = 200, damage = 50,
	unique = True
	)

axe_1 = weapon("Waraxe",
	"This double bladed weapon is meant for agile warriors.",
	quanity=1, speed = 30, value=100, damage=15,
	unique = False
	)

axe_2 = weapon("Battlexe",
	"Slow-swinging speed does great damage, but is also extremely heavy.",
	quanity=1, speed = 5, value=150, damage=35,
	unique = False
	)
karls_axe = weapon("65' Berretta",
	"This gun is not a gun, but instead actually an axe.",
	quanity= 1, speed = 15, value = 125, damage = 25,
	unique = True
	)
	
genes_axe = weapon("Gene Simmons' Axe",
	"Strings made from Demon veins run across this weapon, when used it screams with the voice of a thousand sexy sirens.",
	quanity = 0, speed = 20, value = 300, damage = 50,
	unique = True
	)

'''===		Items		==='''
pock_watch = item("Pocket Watch",
	"This pocket watch may not be worth much to others, but to you it holds value.",
	quanity = 1, speed = 1, value = 10,
	unique = True
	)
	
pearl = item("Pear",
	"This shiny pear should catch a nice price at the market.",
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