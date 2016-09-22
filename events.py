'''===		Events		==='''

import enemies, items, world, random, player, time, actions, bar_talk, sys

player = player.hero

"""===		Repeated Events	==="""

def battle(player, opponent):
	""" REDO THIS ENTIRE FUNCTION. BATTLE IS BUGGY(WELL, NOT BUGGY, but just not .... idk... intuitive)	"""



	battle_hp = opponent.hp
	if len(player.equipped) > 0:
		while player.hp > 0 and battle_hp > 0:
			if opponent.speed > player.equipped[0].speed:
				player.hp = player.hp - opponent.damage
				#time.sleep(1)
				print("\n{} attacked you and did {} damage!\n Your remaining life is {}!".format(opponent.name, opponent.damage, player.hp))
				battle_hp = battle_hp - player.equipped[0].damage
				#time.sleep(1)
				print("\nYou attacked using your {}, and did {} damage!\n{} has {} hp left!".format(player.equipped[0].name, player.equipped[0].damage, opponent.name, battle_hp))
			elif opponent.speed < player.equipped[0].speed or opponent.speed == player.equipped[0].speed:
				battle_hp = battle_hp - player.equipped[0].damage
				#time.sleep(1)
				print("\nYou attacked using your {}, and did {} damage!\n{} has {} hp left!".format(player.equipped[0].name, player.equipped[0].damage, opponent.name, battle_hp))
				player.hp = player.hp - opponent.damage
				#time.sleep(1)
				print("\n{} attacked you and did {} damage!\n Your remaining life is {}!".format(opponent.name, opponent.damage, player.hp))
		if player.hp > 0:
			print("\n========\nThe battle is over and you survive with {} hp remaining.".format(player.hp))
		else:
			print("You have been defeated.")
			game_over()
	else:
		print("	===	You can not battle without a weapon.	===	")

def game_over():
	#time.sleep(1)
	print("You Were Unable to Complete your Quest.")
	#time.sleep(1)
	print("=====	GAME OVER, MAN		======")
	print("	1)	Close the Program.")
	print("	3)	Close the Program.")
	print("	4)	Close the Program.")
	print("	5)	Close the Program.")
	print("	6)	Close the Program.")
	print("	7)	Close the Program.")
	print("	8)	Close the Program.")
	print("	9)	Close the Program.")
	#time.sleep(2)
	print("\n\nWhat would you like to do?")
	choice= input()
	sys.exit()

	
class victory(object):
	""" The many possible ways to win!	"""
	def __init__(self, name):
		self.name = name
		
	def macguffin_Todd(self):
		"""	Todd gets the MacGuffin and reveals that he is a reptile overlord. Using the power of the MacGuffin, begins a terrible 1000 year Reign over Mitovar.	"""
		pass
	
	def macguffin_Sold(self):
		"""	I guess you just forgot the quest. You sold the MacGuffin. Wonder who ended up buying it.	"""
		pass
	
	def macguffin_Witch(self):
		"""	The witch can harness and share the power of the MacGuffin with you!	"""
		pass
	
	def NewKing(self):
		"""	Forget the MacGuffin, You want to be king. It is revealed that King T is a Reptile alien	"""
		pass
	
	def dragonFriend(self):
		"""	The Dragon likes your pocket watch. You become friends with the Dragon, and together you and him ride to an island paradise!	"""
		pass
		
win = victory("Victory")
	
'''===		City Events	==='''

class city_event(object):
	"""Basic Class for things that can happen in the city"""
	
	def __init__(self, name):
		self.name = name
		
class market(city_event):
	'''	Make dat M-M-M money	'''
	def __init__(self, name, inv):
		self.name = name
		self.inv = inv
		
	def in_list(self):
		if player.get_loc().city == True:
			return "Shop"
		else:
			return "Nothing"
		
	def gen_items(self):
		option = False
		
		pos_items = [items.gold_blade]
		for item in items.all_items:
			if item.unique == False and item.name != "Gold" and item.name != "Paper Clip":
				pos_items.append(item)
		for item in pos_items:
			while len(self.inv) < 10:
				self.inv.append(pos_items[random.randint(0, len(pos_items) - 1)])
							
	def buy(self):
		count = 0
		print("You have {} Gold".format(items.money.quanity))
		for item in self.inv:
			count += 1
			print("	" + str(count) + ")	" + str(item.value) + " Gold        " + item.name)
		count += 1
		print("	" + str(count) + ")	" + "Exit The Shop.")
		print("What would you like to purchase?")
		choice_buy = int(input())
		if choice_buy == len(self.inv) + 1:
			print("You exit the shop, and return to Town square.")
			return None
		elif choice_buy <= len(self.inv):
			purch = self.inv[choice_buy - 1]
			if items.money.quanity < purch.value:
				print("You do not have enough Gold.")
				shop.buy(self)
			else:
				print("You have purchased {} for {} Gold!".format(purch.name, str(purch.value)))
				player.add_item(purch)
				self.inv.pop(choice_buy - 1)
				items.money.sub_gold(purch.value)
				print("\n You have {} Gold remaining!".format(items.money.quanity))
				shop.buy(self)
		else:
			print("You did not choose a valid option.")
			shop.buy(self)
				
	def sell(self):
		count = 0
		for item in player.inv:
			if item.name != "Gold":
				count += 1
				print("    " + str(count) + ")  " + str(item.value) + " Gold        " + item.name)
		count += 1
		print("    " + str(count) + ")  " + "Nothing.")
		count += 1
		print("    " + str(count) + ")  " + "Exit the Shop.")
		print("\n\n What would you like to sell?")
		choice_sell = int(input())
		if choice_sell == len(player.inv):
			print("\n You didn't sell anything.")
			shop.sell(self)
		elif choice_sell == len(player.inv) +1:
			print("You exit the shop and return to the Town Square.")
			return None
		elif choice_sell < len(player.inv) + 1:
			sold = player.inv[choice_sell]
			items.money.add_gold(sold.value)
			player.remove_item(sold)
			print("\n You sold your {} for {} Gold!".format(sold.name, sold.value))
			shop.sell(self)
		else:
			print("You did not choose a valid option.")
				
	def enter(self):
		print("""
		You enter the local market, 
		all around are vendors selling various things.
		Gold and items change hands at an alarmingly fast rate.
		""")
		print("	1)	Buy")
		print("	2)	Sell")
		print("	3)	Exit the Shop.")
		print("\n\n What would you like to do?")
		choice_shop = int(input())
		if choice_shop == 1:
			self.gen_items()
			self.buy()
		elif choice_shop == 2:
			self.sell()
		elif choice_shop == 3:
			return None
		else:
			print("You did not choose a valid option.")
			self.enter()

shop = market("Shop", [])
			
class broth(city_event):
	"""	Brothel buffs health to 150, or gives you a disease.	"""
	def __init__(self, name):
		self.name = name
	
	def in_list(self):
		if player.get_loc().city == True:
			return "Brothel"
		else:
			return "Nothing"
			
	def enter(self):
		print('''
			You walk into the local Brothel, hoping to relieve some stress
			''')
		print("	1) Request Services (200 Gold Coins)")
		print("	2) Exit the Brothel")
		print("\n\n What would you like to do?")
		choice_broth = int(input())
		if choice_broth == 1:
			if items.money.quanity >= 200:
				self.service()
				items.money.quanity = items. money.quanity - 200
			elif items.money.quanity < 200:
				print("You can't afford services here, The matron asks you to leave.")
				return None
		elif choice_broth == 2:
			print("You leave and return to Town Square.")
			return None
		else:
			print("You did not choose a valid option.")
			self.enter(self)
			
	def service(self):
		print("You go to the back room, lay and wait.")
		chance = random.randint(0,100)
		#time.sleep(5)
		if chance > 5:
			print("You feel reinvigorated! Much better than before.")
			player.hp = 150
		else:
			print("You feel worse. As if you have cotracted something, might want to rest a while longer.")
			player.hp =75
			
brothel = broth("Brothel")
		
class pub(city_event):

	def __inti__(self, name):
		self.name = name
		
	def in_list(self):
		if player.get_loc().city == True:
			return "Bar"
		else:
			return "Nothing"
	
	
	def enter(self):
		"""	Bars will provide some information as to what you can do in the game.	"""

		print("You enter the local Tavern, thirsty and tired.")
		#time.sleep(1)
		print("You sit at the bar and order a drink. The drink costs 6 Gold.")
		#time.sleep(1)
		if items.money.quanity >= 6:
			items.money.sub_gold(6)
			print("in the hustle and bustle of the Tavern, you overhear a nearby conversation.")
			#time.sleep(1)
			bar_talk.all[random.randint(0, len(bar_talk.all))]()
			print("You finish up your drink and head back out to the Town Square.")
		else:
			print("You don't even have 6 Gold, dude. Get your alchoholic ass out of here.")
			return None
			
bar = pub("Bar")
	
class king(city_event):

	def __init__(self, name):
		self.name = name
	
	def in_list(self):
		if player.get_loc().name == "Mitovar City":
			return "King Todd"
		else:
			return "Nothing"
			
	def enter_1(self):
		print("""
			You enter Castle Mitovar to speak to King Todd.
			Guards on either side of the long ornate chamber stand alert
			At the far end from the entrance, upon a large throne, King Todd sits.
			""")
		#time.sleep(2)
		print("It takes you a moment to travel to where he sits.")
		#time.sleep(2)
		self.enter_2()
		
		
	def enter_2(self):
		print("	1) Give him an item.")
		print("	2) Ask for more information about the Dragon.")
		print("	3) Exit the Castle.")
		print("\n\nWhat would you liek to do?")
		choice_king = int(input())
		if choice_king == 1:
			self.item()
		elif choice_king == 2:
			self.quest()
		elif choice_king == 3:
			print("You turn around and walk down the chamber toward the exit.")
			#time.sleep(1)
			print("...")
			#time.sleep(1)
			print("...")
			#time.sleep(1)
			print("... Almost out...")
			#time.sleep(1)
			print("You return to the Town Square.")
			return None
			
	def item(self):
		print("You present the King with an item.")
		count = 0
		for item in player.inv:
			count += 1
			print("	" +str(count) + "	" + item.name)
		count += 1
		print("	" +str(count) + "	Exit back to other Menu.")
		print("\n\n What would you like to give the King?")
		choice_item = int(input())
		if choice_item == len(player.inv) + 1:
			self.enter_2()
		elif choice_item <= len(player.inv):
			given = player.inv[choice_item - 1]
			if given.name == "Gold":
				print("King Todd refuses your money. \" I already have all the Gold I could ever want!\" He says..")
				self.enter_2()
			elif given.name == "MacGuffin":
				win.macguffin_Todd()
			elif hasattr(given, 'damage'):
				print("	1) Yes")
				print("	2) No")
				print("\n\nAre you sure? Giving the King a weapon will be seen as a challange. \n ==== THIS IS A TOUGH FIGHT ====\n ====THERE IS NO GOING BACK ====")
				choice_fight = int(input())
				if choice_fight == 1:
					self.fight()
				elif choice_fight == 2:
					self.item()
				else:
					print("You did not choose a valid option.")
					self.item()
					
	def fight(self):
		print("""
		"What is this?" King Todd looks down at the weapon you handed him.
		"Is this a challange?" His voice raises, "You dare challange your King!?
		"So be it. To arms!"
		""")
		print("King Todd grabs for his blade and paitently stand his ground waiting for your first move.")
		battle(player, enemies.kingT, None)
		#time.sleep(1)
		print("The clanging of metal ceases. You have defeated the King in honorable combat.")
		#time.sleep(2)
		print("As you approach your rightfully earned Throne, behind you, you hear him stand once more.")
		print("""
		"You think you can defeat me so easily!?"
		His skin slides off revealing slimey green scales below.
		"This is my final form!"
		""")
		battle(player, enemies.kingT_reptile, None)
		win.NewKing()
		
	def quest(self):
		print("""
		The dragon lurks at the top of the mountain up north!
		it took my MacGuffin and a large amount of my Gold!
		I need you to go get my stuff back and slay the beast!
		
		The dragon is feirce and will be able to resist a large amoutn of damage,
		Be sure you are ready before facing it.
		""")
		self.enter_2()
		
kingT = king("King Todd")
		
class elf_mage(city_event):
	
	def __init__(self, name, inter_times):
		self.name = name
		self.inter_times = inter_times

	def in_list(self):
		if player.get_loc().name == "Strukes City":
			return "Elven Mage"
		else:
			return "Nothing"	
	
	def enter(self):
		"""	Infuses weapons with demon essence after you complete his quest of dealing with the witch		"""
		print("""
		You walk into the Mage's Shop knowing you are unable to use any of his wares.
		Looking all around, you see various staves, and magical trinkets.
		The owner of the shop, Lunk, approaches you.
		""")
		time.sleep(1)
		if self.inter_times == 0:
			print("You are a warrior of some renown. I see your strength. I need to ask a favor of you.")
			self.quest()
		elif self.inter_times == 1:
			print("You have returned! Do you have any news of the Witch?")
			self.inter()
			
	def quest(self):
		print("	1) What do you need, mage?")
		print("	2) I can't help you right now. (Leave the shop)")
		print("\n\n What would you like to say?")
		choice_mage_quest = int(input())
		if choice_mage_quest == 1:
			print("There is a witch in the northen woods. I bellieve she is what became of my first wife.\n I need you to find her for me.\n if she is corrupt, slay her.\n otherwise, give her this.\n From the rumurs I have heard, She is in the Western Woods.")
			player.inv.append(items.wedd_ring_1)
			items.wedd_ring_1.quanity = 1
			print("You have aquired {}!".format(items.wedd_ring_1.name))
			self.inter_times = 1
		elif choice_mage_quest == 2:
			print("You leave and return to Town Square.")
			return None
		else:
			print("You did not choose a valid option.")
			self.quest()
			
	def inter(self):
		if self.inter_times == 3:
			self.blood2ess()
		elif items.wedd_ring_1 in player.inv:
			print("	1) I am sorry, I have not gotten around to it. (Leave)")
			print("	2) What is it I am supposed to do again?")
			choice_inter = int(input())
			if choice_inter == 1:
				print("You return to the Town Square")
				return None
			elif choice_inter == 2:
				print("There is a witch in the northen woods. I bellieve she is what became of my first wife.\n I need you to find her for me.\n if she is corrupt, slay her.\n otherwise, give her this.")
				print("You remember the Wedding Ring.")
				self.inter()
		elif items.witch_blood in player.inv:
			print("	1) I am sorry, I have not gotten around to it. (Leave)")
			print("	2) The witch was Corrupt, I could not change her.")
			choice_inter = int(input())
			if choice_inter == 1:
				print("You return to the Town Square.")
				return None
			elif choice_inter == 2:
				print("I am sad that nothing could be done, but thank you for helping\nBring me demon's blood and I will convert it to Demon Essence for you.")
				self.inter_times = 3
			else:
				print("You did not choose a valid option.")
				self.inter()
		elif items.wedd_ring_2 in player.inv:
			print("	1) I am sorry, I have not gotten around to it. (Leave)")
			print("	2) I spoke to her, and she gave me this. (Hand him the Witch's Ring")
			choice_inter = int(input())
			if choice_inter == 1:
				print("You return to the Town Square")
				return None
			elif choice_inter == 2:
				print("My word... She is sentient... I must go visit her. I will return here after.")
				print("Bring me Demon's Blood and i will boil it down to essence for you.")
				self.inter_times = 3
				
	def blood2ess(self):
		print("Would you like me to turn your Demon's Blood into Essence?")
		print("\n\n1) Yes.")
		print("	2) No. (Leave)")
		choice_b2e = int(input())
		if choice_b2e == 1:
			player.inv.remove(items.demons_blood)
			player.inv.append(items.demons_essence)
			items.demons_essence.quanity += items.demons_blood.quanity
			items.demons_blood.quanity = 0
			print("You have aqquired {} Demon Essences!".format(items.demon_essence.quanity))
			return None
		elif choice_b2e ==2:
			print("You return to the Town Square.")
			return None
		else:
			print("You did not choose a valid option.")
			self.blood2essence()
				
lunk = elf_mage("Lunk", 0)

class rest(city_event):

	def __init__(self, name):
		self.name = name
		
	def in_list(self):
		if player.get_loc().city == True:
			return "Inn"
		else:
			return "Nothing"	
	
	def enter(self):
		"""	Allows players to rest and regain health	"""
		print("	1) Yes")
		print("	2) No. (Leave)")
		print("\n\n Would you like to rest?")
		choice_inn = int(input())
		if choice_inn == 1:
			actions.rest(player)
		elif choice_inn == 2:
			print("You return to the Town Square.")
			return None
				
inn = rest("inn")

class Dsmith(city_event):
	"""	Provides a unique weapon and can infuse weapons.	"""
	
	def __init__(self, name):
		self.name = name
	
	def in_list(self):
		if player.get_loc().name == "Azkabar (North)":
			return "Dwarven Blacksmith"
		else:
			return "Nothing"
	
	def enter(self):
		print("""
		You walk into the Smith's forgery.
		The heat hits you just as if you walked into the sun.
		Near the forge, you see a dwarf pounding away at a red hot blade.
		
		He notices you. The blade hisses as he submerges it into water.
		"How can I help you?" he asks.
		""")
		print("	1) Can you make me a weapon that could defeat a Dragon?")
		print("	2) Can you do anything to improve the weapons I have?")
		print("	3) Exit the Dwarven Smith's Forge.")
		print("\n\n What would you like to do?")
		choice =int(input())
		if choice == 1:
			self.weapon()
		elif choice == 2:
			self.infuse()
		elif choice == 3:
			print("You leave and return to the Town Square.")
			return None
		else:
			print("You did not choose a valid option.")
			self.enter()
			
	def weapon(self):
		print("Yes, I am the best Smith in all of Azkabar. Of course I can.")
		time.sleep(1)
		print("Of course... I can't do it for free... 1000 Gold Coins.")
		print("\n\n	1) I have your money here. (1000 Gold Coins)")
		print("	2) I will be back later with your money.")
		choice = int(input())
		if choice == 1 and items.money.quanity > 999:
			print("You hand over a large sack of Gold.")
			print("The Dwarf begins working.")
			count = 0
			while count < 5:
				print("...")
				time.sleep(1)
			print("He hands you a Large Axe.")
			print("You have aquired {}".format(items.dwarf_axe.name))
			player.inv.append(items.dwarf_axe)
			items.dwarf_axe.quanity = 1
		elif choice == 1 and items.money.quanity < 1000:
			print("You do not have enough money. Come back later.")
			self.weapon()
		elif choice == 2:
			print("You leave and return to the Town Square.")
			
	def infuse(self):
		print("I can infuse any weapon you have with the power of a demon. I need the weapon and some Demon Essence.")
		if items.demon_essence in player.inv:
			weapons = []
			count = 0
			for item in player.inv:
				if item.equippable == True or item.name == "Pocket Watch":
					weapon.append(item)
			for item in weapons:
				count += 1
				print("    " + str(count) + ")  " + item.name )
			count += 1
			print("    " + str(count) + ")  " + "Exit the infuse Menu.")
			print("\n\n What would you like to infuse?")
			choice = int(input())
			if choice <= len(weapons):
				infused = weapons[choice -  1]
				if infused.name == "Pocket Watch":
					player.inv.remove(items.pock_watch)
					player.inv.append(items.demon_pock_watch)
					print("You have aquired the Demonic Pocket Watch!")
					print(items.demon_pock_watch.inquire())
				else:
					infused.infuse()
					print("If you come across another of these, I have given you the formula to infuse it yourself.")
			elif choice == len(weapons) + 1:
				self.enter()
			
		else:
			print("You don't have any Demon Essence. You ask the Dwarf where you might find some.")
			time.sleep(1)
			print("I know of an Elven Mage over in Strukes City who can extract it from Demon's blood. Try him.")
			self.enter()
			
dwarf = Dsmith("Dwarf")

class Esmith(city_event):
	
	def __init__(self, name):
		self.name = name
	
	def in_list(self):
		if player.get_loc().name == "Strukes City":
			return "Elven Blacksmith"
		else:
			return "Nothing"
	
	def elf_smith():
		"""	Provides a Unique weapon	"""
		
		pass

class Dragon_E(city_event):
	
	def __init__(self, name):
		self.name = name
		
	def in_list(self):
		if player.get_loc().name == "Dragon's Lair":
			return "Dragon"
		else:
			return "Nothing"
		
	def flight():
		"""	For secret "Befriending the dragon" ending	"""
		
		pass


all = [shop, brothel, inn, bar, kingT, lunk, dwarf]		
