"""===		Actions		==="""

import random, events, player, time

def rest(player):
	if player.hp < 100:
		print("========\nYour health has been restored.\n========")
		player.hp = player.hp + (100 - player.hp)
	else:
		print("========\nYou rest, but your health is already full.\n========")
	
def travel_chance(nsew):
	chance = random.randint(0, 1000)
	if chance < 665:
		time.sleep(1)
		print("You travel a mile {}".format(nsew))
	elif chance >= 665 and chance < 765:
		time.sleep(1)
		events.chest()
	elif chance >=765 and chance < 836:
		time.sleep(1)
		events.bandit()
	elif chance >=836 and chance < 918:
		time.sleep(1)
		events.corpse()
	elif chance >= 918 and chance < 953:
		time.sleep(1)
		events.orcs()
	elif chance >= 953 and chance < 959:
		time.sleep(1)
		events.doug()
	elif chance >= 959 and chance < 962:
		time.sleep(1)
		events.karl()
	elif chance >= 962 and chance < 977:
		time.sleep(1)
		events.barry()
	elif chance >= 977 and chance <= 1000:
		time.sleep(1)
		events.demon()
	else:
		print("==============\nI am not sure what has gone wrong here.\n===============")
	
def travel(player, new_x, new_y):
	if player.x == new_x and player.y == new_y:
		print("You are already at the new location.")
	elif player.x != new_x and player.y == new_y:
		while player.x > new_x:
			direction = "West"
			player.x = player.x -1
			travel_chance(direction)
		while player.x < new_x:
			direction = "East"
			player.x = player.x + 1
			travel_chance(direction)
	elif player.x == new_x and player.y != new_y:
		while player.y > new_y:
			direction = "South"
			player.y = player.y -1
			travel_chance(direction)
		while player.y < new_y:
			direction = "North"
			player.y = player.y + 1
			travel_chance(direction)
	elif player.x != new_x and player.y != new_y:
		print("This should not have happened.")
			
	
def equip(player, item):
	if item.equippable == True and item in player.inv and len(player.equipped) < 1:
		print("You have equipped your {}".format(item.name))
		player.inv.remove(item)
		player.equipped.append(item)
	elif item.equippable == True and item in player.inv and len(player.equipped) >= 1:
		print("You can only equip one weapon at a time. Try Unequip.")
	elif item.equippable == False and item in player.inv:
		print("You can't equip your {}.".format(item.name))

def unequip(player, item):
	if item in player.equipped:
		player.inv.append(item)
		player.equipped.remove(item)
		print("You have unequipped your {}".format(item.name))
	else:
		print("You are trying to unequip something you don't have.")
		
def inquire(thing):
	print(thing.inquire())	