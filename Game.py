"""===		Testing For Anything		==="""

import items, actions, encounters, world, enemies, player, events, time, sys
player = player.hero
places = world.all_places


def travel_choices():
																					#need alll these variables for controlling my loops, without these, ifinite recursion.
	north = 0
	south = 0
	east = 0
	west = 0
																					#these just make it easier for me to make the data I need
	play_x = player.get_loc().x
	play_y = player.get_loc().y
	loc = [play_x, play_y]
																					#made these variables so I can modify a integer without affecting the actual value 
	Nplay_y = play_y
	Splay_y = play_y
	Eplay_x = play_x
	Wplay_x = play_x
	world.all_coords.remove(loc)										#removes player location from list. Allows me to actually iterate becasue player location is not listed	
																					#hey, check out some loops in loops in loops, dudes.
	while north == 0:																				#checks that North is still 0
		if Nplay_y > 21:																					#ensures that I don't go off the map
			north = 1																						#if I am off the map, there must be no location north of me.
			print("   1)	There is no location North of you.")
			break																								#Therefore, done with north, move on to next.	
		elif [play_x, Nplay_y] not in world.all_coords:
			Nplay_y += 1																					#compares player loc to whateve is north of him/her
		else:
			for item in places:
				coord = [item.x, item.y]
				if [play_x, Nplay_y] == coord:
					north_place = item
			print("   1)  Travel North to {}.".format(north_place.name))
			north = 2
	while south == 0:																					#Refer to comments beginning on line 34
		if Splay_y < -1:
			south = 1
			print("   2)	There is no location South of you.")
			break
		elif [play_x, Splay_y] not in world.all_coords:
			Splay_y -= 1
		else:
			for item in places:
				coord = [item.x, item.y]
				if [play_x, Splay_y] == coord:
					south_place = item
			print("   2)  Travel South to {}.".format(south_place.name))
			south = 2
	while east == 0:																					#Refer to comment on line 48
		if Eplay_x > 21:
			east = 1
			print("   3)	There is no location East of you.")
			break
		elif [Eplay_x, play_y] not in world.all_coords:
			Eplay_x += 1
		else:
			for item in places:
				coord = [item.x, item.y]
				if [Eplay_x, play_y] == coord:
					east_place = item
			print("   3)  Travel East to {}.".format(east_place.name))
			east = 2
	while west == 0:																					#Refer to comment on line 62
		if Wplay_x < -10:
			west = 1
			print("   4)	There is no location West of you.")
			break
		elif [Wplay_x, play_y] not in world.all_coords:
			Wplay_x -= 1
		else:
			for item in places:
				coord = [item.x, item.y]
				if [Wplay_x, play_y] == coord:
					west_place = item
			print("   4)  Travel West to {}.".format(west_place.name))
			west = 2
	world.all_coords.append([play_x, play_y])																				#Relisting that player location
	print("   5)	Go back to other Menu.")
	print("Where would you like to travel to?")																		#Time for some action
	choice_trav = int(input())
	if choice_trav == 1 and 'north_place' in locals():
		encounters.travel(player, north_place.x, north_place.y)
		print("\n" +"You have arrived at:\n" +north_place.inquire())
	elif choice_trav == 1 and 'north_place' not in locals():
		print("You can't travel to 'No Location,' ya dingus.\n You remain at {}\n".format(player.get_loc().name))
	elif choice_trav == 2 and 'south_place' in locals():
		encounters.travel(player, south_place.x, south_place.y)
		print("\n" + "You have arrived at:\n" +south_place.inquire())
	elif choice_trav == 2 and 'south_place' not in locals():
		print("You can't travel to 'No Location,' ya dingus.\n You remain at {}\n".format(player.get_loc().name))
	elif choice_trav == 3 and 'east_place' in locals():
		encounters.travel(player, east_place.x, east_place.y)
		print("\n" +"You have arrived at:\n" +east_place.inquire())
	elif choice_trav == 3 and 'east_place' not in locals():
		print("You can't travel to 'No Location,' ya dingus.\n You remain at {}\n".format(player.get_loc().name))
	elif choice_trav == 4 and 'west_place' in locals():
		encounters.travel(player, west_place.x, west_place.y)
		print("\n" +"You have arrived at:\n" + west_place.inquire())
	elif choice_trav == 4 and 'west_place' not in locals():
		print("You can't travel to 'No Location,' ya dingus.\n You remain at {}\n".format(player.get_loc().name))
		
	
	play()
		
acts = [
	"Travel",
	"Manage Inventory", 
	"Interact with {}".format(player.get_loc().name),
	"Check Character Information.",
	"Close the Program"
	]
	
def play():
	print("You are currently at {}\n".format(player.get_loc().name))
	time.sleep(1)
	print(	"	1) Travel",
	"\n	2) Manage Inventory", 
	"\n	3) Interact with {}".format(player.get_loc().name),
	"\n	4) Check Character Information.",
	"\n	5) Close the Program"
	)
	print("What would you like to do?\n")
	choice = int(input())
	if choice == 1:
		travel_choices()
	elif choice == 2:
		print("==== You have the following items ====\n\n\n")
		player.check_inv()
		print(
		"   1)  Go Back\n",
		"  2)  Equip\n",
		"  3)  Check Equipped Item\n",
		"  4)  Unequip\n",
		)
		print("What would you like to do?\n")
		choice_inv = int(input())
		if choice_inv == 1:
			play()
		elif choice_inv == 2:
			count = 0
			for item in player.inv:
				count += 1
				print("    " + str(count) + ")  " + item.name )
			print("What would you like to equip?\n")
			choice_equip = int(input())
			player.equip(player.inv[choice_equip - 1])
			print("\n\n")
			play()
		elif choice_inv == 3:
			print("=== You have the following item equipped.===\n\n")
			player.check_equip()
			play()
		elif choice_inv == 4:
			if len(player.equipped) > 0:
				player.unequip(player.equipped[0])
				play()
			else:
				print("Not a Damn thing, good sir or madam.")
				play()
	elif choice == 3:
		count = 0
		local_events = []
		for item in events.all:
			if item.in_list() != "Nothing":
				count += 1
				local_events.append(item)
				print("	" + str(count) + ") " + item.in_list())
		count += 1
		print("	" + str(count) + ") " + "Back")
		choice_interact = int(input())
		if choice_interact == len(events.all) + 1:
			play()
		elif choice_interact <= len(events.all):
			mod_choice = choice_interact - 1
			if len(local_events) > 0:
				if local_events[mod_choice].in_list() == "King Todd":
					local_events[mod_choice].enter_1()
				else:
					local_events[mod_choice].enter()
			else:
				play()
		play()
	elif choice == 4:
		print("Your health is at {} points.".format(player.hp))
		print("You have {} Gold Coins.".format(items.money.quanity))
		if len(player.equipped) > 0:
			print("You have your {} Equipped, which does {} damage.".format(player.equipped[0].name, player.equipped[0].damage))
		else:
			print("You do not have a weapon currently Equipped. You should equip one.")
		play()
	elif choice == 5:
		pass
		#sys.exit()
	else:
		print("You did not choose a valid option.")
		play()
		
print("""	
	Welcome to Mitovar!
	You are in the great city of Mitovar City
	Speaking to Todd, the King of Mitovar City!

	King Todd says to you, a valient hero, 
	 "I need you to go North to the Dragon's Lair
	 and defeat the Dragon! There you will find my 
	 MacGuffin, which I had lost. Retrieve it for me!"
	 
	 You may not have the equpment right now to face
	 such a creature, I recommend going East to 
	 Sturkes City and exploring a bit first.
	 
	 It is probably a good idea to check your inventory 
	 for a weapon. If you don't have a weapon equipped,
	 you will have to fight with your bare hands!
	 And lose. You will die in agony if you have no weapon.
""")

play()
