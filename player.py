"""===		Player		==="""

import items, actions, world

class player(object):
	def __init__(self):
		self.inv = [items.money, items.sword_1, items.pock_watch]
		self.hp = 100
		self.x = 1
		self.y = 1
		self.equipped = []
		
	def equip(self, item):
		if len(self.equipped) == 1:
			print("You can't equip more than one weapon. Try to uneqiup something.")
		elif item.equippable == False:
			print("you can't equip your {}, you little fuck.".format(item.name))
		else:
			if item.quanity == 1:
				print("You have equipped your {}".format(item.name))
				self.inv.remove(item)
				self.equipped.append(item)
			elif item.quanity > 1:
				print("You have equipped your {}.".format(item.name))
				item.quanity = item.quanity - 1
				self.equipped.append(item)
		
	def unequip(self,item):
		if len(self.equipped) == 0:
			print("You have nothing equipped. Try Equipping something first.")
		else:
			if item not in self.inv:
				self.inv.append(item)
				self.equipped.pop(0)
				print("You have unequipped your {}".format(item.name))
				print("Your weapon is back in your inventory.")
			else:
				item.quanity = item.quanity + 1
				print("You have unequipped your {}.".format(item.name))
				print("Your weapon is back in your inventory.")
				self.equipped.pop(0)
	
	def is_alive(self):
		if self.hp > 0:
			return True
		else:
			return False
			
	def check_inv(self):
		for item in self.inv:
			if item.name != "Gold":
				print("	{}:  ".format(item.quanity), item.inquire())
			else:
				print("        " + item.inquire())
	
	def check_equip(self):
		if len(self.equipped) > 0:
			for item in self.equipped:
				print(item.inquire())
		else:
			print("You have nothing equipped.")
	
	def add_item(self, item):
		if item not in self.inv:
			self.inv.append(item)
		else:
			item.quanity = item.quanity + 1
			
	def remove_item(self, item):
		if item.quanity > 1:
			item.quanity = item.quanity - 1
		elif item.quanity == 1:
			self.inv.remove(item)
		
	def get_loc(self):
		for item in world.all_places:
			if (self.x,self.y) == (item.x, item.y):
				return item

hero = player()
