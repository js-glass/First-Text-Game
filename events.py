'''===		Events		==='''

import enemies, items, world, random, player, time

player = player.hero

"""===		Repeated Events	==="""

def randItems(amt):
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

def battle(player, opponent):
	battle_hp = opponent.hp
	while player.hp > 0 and battle_hp > 0:
		if opponent.speed > player.equipped[0].speed:
			player.hp = player.hp - opponent.damage
			time.sleep(1)
			print("\n{} attacked you and did {} damage!\n Your remaining life is {}!".format(opponent.name, opponent.damage, player.hp))
			battle_hp = battle_hp - player.equipped[0].damage
			time.sleep(1)
			print("\nYou attacked using your {}, and did {} damage!\n{} has {} hp left!".format(player.equipped[0].name, player.equipped[0].damage, opponent.name, battle_hp))
		elif opponent.speed < player.equipped[0].weight or opponent.speed == player.equipped[0].weight:
			battle_hp = battle_hp - player.equipped[0].damage
			time.sleep(1)
			print("\nYou attacked using your {}, and did {} damage!\n{} has {} hp left!".format(player.equipped[0].name, player.equipped[0].damage, opponent.name, battle_hp))
			player.hp = player.hp - opponent.damage
			time.sleep(1)
			print("\n{} attacked you and did {} damage!\n Your remaining life is {}!".format(opponent.name, opponent.damage, player.hp))
	if player.hp > 0:
		print("\n========\nThe battle is over and you survive with {} hp remaining.".format(player.hp))
	else:
		print("You have been defeated.")

'''===		City Events	==='''

def shop(x, y):
	pass
	
def broth(x, y):
	pass

def bar(x, y):
	pass
	
def kingT():
	pass
	
def mage():
	pass

def inn():
	pass
	
def dwarf_smith():
	pass
	
def elf_smith():
	pass
	
def sailor():
	pass
	
'''===		Travel Events	==='''
				

def chest():
	print("""
	As you walk, you notice a chest slightly off of your path. You open the chest and plunder it's contents.
	""")
	randItems(2)
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

def bandit():
	print("""
	A bandit creeps up behind you. Before you are able to react, you have a weapon poking your back
	and a voice demanding you give himn your money.
	""")
	print(enemies.bandit.inquire())
	if items.money.quanity > 99:
		print("	1)	Give him some of your money.")
		mon = True
	else:
		print("	1)	You do not have enough money to appease him.")
		mon = False
	print("	2)	Turn around and attack him.")
	print("	3)	Try to flee from the highwayman.")
	print("\n\nWhat would you like to do?")
	choice_band = int(input())
	if choice_band == 1 and mon == True:
		print("""
		You give the bandit a sack of 100 gold coins. He walks away satisfied, you walk away ashamed.
		""")
		items.money.sub_gold(100)
	elif choice_band == 1 and mon == False:
		print("Your coinpurse is nearly empty, it won't be enough to make this man happy.")
		bandit()
	elif choice_band == 2:
		if len(player.equipped) > 0:
			print("You decide, fuck this guy for trying to steal from you!")
			battle(player, enemies.bandit)
			print("You take the Bandit's previous \"earnings\"")
			earnings = random.randint(50, 200)
			items.money.add_gold(earnings)
			print("You have aquired {} Gold Coins!".format(earnings))
		else:
			print("You have no weapon equipped and cannot fight.")
			time.sleep(1)
			bandit()
	elif choice_band == 3:
		print("You figure you can get away from this guy, just by running fast.")
		time.sleep(1)
		success = random.randint(0,100)
		if success >25:
			print("And you were right, you made it out of the Bandit's sight.")
		else:
			print("But you were wrong. He followed you and poked the same blade toward you.")
			bandit()

def corpse():
	print("""
	You stumble upon the corpse of a fallen warrior.
	Is it ethical to take what he has dropped? Do you care?
	""")
	print("	1)	You do not take the poor soul's items out of respect for the dead.")
	print("	2)	This is a stupid text based game. Ethics be damned, I want stuff.")
	print("\n\nWhat would you like to do?")
	choice_corpse = int(input())
	if choice_corpse == 1:
		print("You look down in mourning at the stranger at your feet. You hope to yourself that you don't end up like him.")
	elif choice_corpse == 2:
		print("You search the cadaver for anything of value. \n You find the following:")
		randItems(2)
		
	
def orcs():
	print("orcs")
	
def doug():
	print("doug")
	
def karl():
	print("karl")
	
def demon():
	print("demon")
	
def barry():							#GIVES GENE'S AXE! BEST ITEM IN GAME!
	print("Barry")
	
def rest_stop():						#HAVE NOT ADDED TO LIST! NEED TO!
	print("rest_stop")