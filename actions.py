"""===		Actions		==="""

import random, events, player, time

def rest(player):
	"""		Used in Inns and othe places for rest	"""
	if player.hp < 100:
		print("========\nYour health has been restored.\n========")
		player.hp = player.hp + (100 - player.hp)
	elif player.hp > 100:
		print("========\nYou rest, but your health is buffed to above full.\n========")
	else:
		print("========\nYou rest, but your health is already full\n========")
					
def equip(player, item):
	if item.equippable == True and item in player.inv and len(player.equipped) < 1:
		print("You have equipped your {}".format(item.name))
		time.sleep(1)
		player.inv.remove(item)
		player.equipped.append(item)
	elif item.equippable == True and item in player.inv and len(player.equipped) >= 1:
		print("You can only equip one weapon at a time. Try Unequip.")
		time.sleep(1)
	elif item.equippable == False and item in player.inv:
		print("You can't equip your {}.".format(item.name))
		time.sleep(1)

def unequip(player, item):
	if item in player.equipped:
		player.inv.append(item)
		player.equipped.remove(item)
		print("You have unequipped your {}".format(item.name))
		time.sleep(1)
	else:
		print("You are trying to unequip something you don't have.")
		time.sleep(1)
		
def inquire(thing):
	print(thing.inquire())	