"""	=== Travel===	"""
import random, time, items, player, enemies, events

player = player.hero

class rand_event(object):
	def __init__(self, name, type, rarity, descrip):
		self.name = name
		self.type = type
		self.rarity = rarity
		self.descrip = descrip
		
	def get_name(self):
		return self.name
		
	def get_rarity(self):
		return self.rarity
		
	def get_descrip(self):
		return self.descrip
		
class loot_event(rand_event):
	def __init__(self, name, rarity, descrip):
		self.name = name
		self.type = "Loot"
		self.rarity = rarity
		self.descrip = descrip
		
	def gen_loot(self, amt):
		"""	Function for generating wonderful loot for the player! The bread and butter of RPGs	"""
		
		pos_cont = []
		for item in items.all_items:
			if item.unique == False:
				pos_cont.append(item)
		contents = []
		while len(contents) < amt:
			contents.append(pos_cont[random.randint(0, len(pos_cont) - 1)])
		for item in contents:
			if item.name == "Gold":
				quanity = random.randint(25, 200)
			else:
				quanity = ""
			if 'quanity' in locals():
				print(str(quanity) + "  " + item.inquire())
			else:
				print(item.inquire())
			print("Would you like to take this item with you?")
			print("	1) Yes")
			print("	2) No")
			choice_take = int(input())
			if choice_take == 1 and item.name == "Gold":
				print("You have aquired {} Gold Coins".format(quanity))
				items.money.add_gold(quanity)
			elif choice_take == 1 and quanity != int:
				print("You have aquired {}".format(item.name))
				if item not in player.inv:
					player.inv.append(item)
				if item in player.inv:
					item.quanity = item.quanity + 1
			elif choice_take == 2:
				print("You did not take the {}".format(item.name))
			else:
				print("You did not take the {}".format(item.name))
			
chest = loot_event("Chest", "Rare", "You see a chest slightly off the path.")
corpse = loot_event("Corpse", "Rare", "The remains of a fallen traveller sit at your feet.")
hollow_rock = loot_event("Hollow Rock", "Ultra Rare", "Something about this rock in your path seems a bit off.")
loots = [chest, corpse, hollow_rock]

class fight_event(rand_event):
	def __init__(self, name, rarity, reward, mob):
		self.name = name
		self.type = "Fight"
		self.rarity = rarity
		self.reward = reward
		self.mob = mob
		
	def enter(self):
		print("In your path, you encounter a {}.".format(self.mob.name))
		print(self.mob.inquire())
		if self.mob.name == "Bandit":
			self.bandit()	
		else:
			print("	1) Fight.")
			print("	2) Run.")
			print("\n\n What would you like to do?")
			choice = int(input())
			if choice == 1:
				self.fight()
			elif choice == 2:
				self.flee()
			else:
				print("You did not choose a valid option.")
				time.sleep(2)
				self.enter()
		
	def fight(self):
		events.battle(player, self.mob)
		self.rewards()
		
	def flee(self):
		print("You attempt to run.")
		chance = random.reandint(0, 100)
		if chance > 33:
			print("You make it away and continue on your path.")
			return None
		else:
			print("You could not escape.")
			self.enter()
			
	def bargin(self):
		pass
		
	def bandit(self):
		print("He wants 100 Gold for you to pass.")
		print("	1) Give him 100 Gold Coins.")
		print("	2) Fight him.")
		print("	3) Run.")
		print("\n\n What would you like to do?")
		choice = int(input())
		if choice == 1:
			self.bargin()
		elif choice == 2:
			self.fight()
		elif choice == 3:
			self.flee()
		else:
			print("You did not choose a valid option.")
			time.sleep(2)
			self.enter()
	
	def rewards(self):
		rewards = {
			1: items.money.add_gold(random.randint(50, 200)),
			2: 
			3: 
			4: items.spider_silk,
			5: items.slime,
			6: items.demons_blood
		}
		if self.rewards == 1:
			earnings = rewards[1]
			print("You defeat the Bandit and take his previous 'Earnings.'")
			print("You have obtained {} Gold Coins!".format(earnings))
		elif self.rewards == 2 or self.rewards == 3:
			print("You defeated the {}".format(self.mob.name))
			print("You Loot his belongings.")
			rewards[self.rewards]
		else:
			print("You defeated the {}!".format(self.mob.name))
			print("You have obtained {}".format(rewards[self.reward].name))
		
		

orc_1 = fight_event("Orcish Warrior", "Rare", 2, enemies.orc_1) 
orc_2 = fight_event("Orcish Crusader", "Rare", 2, enemies.orc_2)
orc_3 = fight_event("Orcish Leader", "Ultra Rare", 3, enemies.orc_3)
giant_spider = fight_event("Giant Spider", "Common", 4, enemies.giant_spider)
demon_1 = fight_event("Demon Knight", "Ultra Rare", 6, enemies.demon_1)
demon_2 = fight_event("Demon Fighter", "Ultra Rare", 6, enemies.demon_2)
bandit = fight_event("Bandit", "Common", 1, enemies.bandit)
slime = fight_event("Slime", "Common", 5, enemies.slime)



