'''===		Events		==='''

import enemies, items, world, random, player, time, actions, sys

player = player.hero

"""===		Repeated Events	==="""

def loot(amt):
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

def battle(player, opponent, event):
	battle_hp = opponent.hp
	if len(player.equipped) > 0:
		while player.hp > 0 and battle_hp > 0:
			if opponent.speed > player.equipped[0].speed:
				player.hp = player.hp - opponent.damage
				time.sleep(1)
				print("\n{} attacked you and did {} damage!\n Your remaining life is {}!".format(opponent.name, opponent.damage, player.hp))
				battle_hp = battle_hp - player.equipped[0].damage
				time.sleep(1)
				print("\nYou attacked using your {}, and did {} damage!\n{} has {} hp left!".format(player.equipped[0].name, player.equipped[0].damage, opponent.name, battle_hp))
			elif opponent.speed < player.equipped[0].speed or opponent.speed == player.equipped[0].speed:
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
			game_over()
	else:
		print("	===	You can not battle without a weapon.	===	")
		event()

def game_over():
	time.sleep(1)
	print("You Were Unable to Complete your Quest.")
	time.sleep(1)
	print("=====	GAME OVER, MAN		======")
	print("	1)	Close the Program.")
	print("	3)	Close the Program.")
	print("	4)	Close the Program.")
	print("	5)	Close the Program.")
	print("	6)	Close the Program.")
	print("	7)	Close the Program.")
	print("	8)	Close the Program.")
	print("	9)	Close the Program.")
	time.sleep(2)
	print("\n\nWhat would you like to do?")
	choice= input()
	sys.exit()
	
'''===		City Events	==='''

def shop():
	shop_items= []
	pos_items = [items.gold_blade]
	shop_gen = False
	print("""
	You enter the local market, 
	all around are vendors selling various things.
	Gold and items change hands at an alarmingly fast rate.
	""")
	print("	1)	Buy")
	print("	2)	Sell")
	print("	3)	Exit The Market")
	print("\n\n What would you like to do?")
	choice_shop = int(input())
	if choice_shop == 1:
		for item in items.all_items:
			if item.unique != True and item.name != "Gold" and item.name != "Paper Clip":
				pos_items.append(item)
		while len(shop_items) < 11 and shop_gen == False:
			shop_items.append(pos_items[random.randint(0, len(pos_items) - 1)])
			if len(shop_items) == 11:
				shop_gen = True
		count = 0
		print("You have {} Gold".format(items.money.quanity))
		for item in shop_items:
			count += 1
			print("	" + str(count) + ")	" + str(item.value) + " Gold        " + item.name)
		count += 1
		print("	" + str(count) + ")	" + "Nothing.")
		print("\n\n What would you like to purchase?")
		choice_buy = int(input())
		if choice_buy == len(shop_items) + 1:
			print("\nYou purchase nothing.")
			shop()
		else:
			purch = shop_items[choice_buy - 1]
			if items.money.quanity < purch.value:
				print("You so not have enough Gold.")
				shop()
			else:
				print("You have purchased {} for {} Gold!".format(purch.name, str(purch.value)))
				player.add_item(purch)
				shop_items.pop(choice_buy - 1)
				items.money.sub_gold(purch.value)
				print("\n You have {} Gold remaining!".format(items.money.quanity))
				shop()
				
	elif choice_shop == 2:
		count = 0
		for item in player.inv:
			if item.name != "Gold":
				count += 1
				print("    " + str(count) + ")  " + str(item.value) + " Gold        " + item.name)
		count += 1
		print("    " + str(count) + ")  " + "Nothing.")
		print("\n\n What would you like to sell?")
		choice_sell = int(input())
		if choice_sell == len(player.inv):
			print("\n You didn't sell anything.")
			shop()
		elif choice_sell < len(player.inv) + 1:
			sold = player.inv[choice_sell]
			items.money.add_gold(sold.value)
			player.inv.pop(choice_sell)
			print("\n You sold your {} for {} Gold!".format(sold.name, sold.value))
			shop()
		else:
			print("You did not choose a valid option.")
			shop()
			
	elif choice_shop == 3:
		print("You exit the shop and head back to the Town Square.")
		
	else:
		print("You did not choose a valid option.")
		shop()
			
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
	
def flight():
	pass
	
'''===		Travel Events	==='''
				

def chest():
	print("""
	As you walk, you notice a chest slightly off of your path. You open the chest and plunder it's contents.
	""")
	loot(2)

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
		print("You decide, fuck this guy for trying to steal from you!")
		battle(player, enemies.bandit, bandit)
		print("You take the Bandit's previous \"earnings\"")
		earnings = random.randint(50, 200)
		items.money.add_gold(earnings)
		print("You have aquired {} Gold Coins!".format(earnings))
	elif choice_band == 3:	
		print("You figure you can get away from this guy, just by running fast.")
		time.sleep(1)
		success = random.randint(0,100)
		if success >25:
			print("And you were right, you made it out of the Bandit's sight.")
		else:
			print("But you were wrong. He followed you and poked the same blade toward you.")
			bandit()
	else:
		print("You didn't chose any of the possible choices.")
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
		loot(2)
	else:
		print("You didn't choose any possible option.")
		
def orcs():
	print("""
	You see a few big dumb orcs travelling the opposite direction of you.
	Hoping silently to yourself he won't think you are a challange, you pass by him.
	""")
	chance = random.randint(0,100)
	if chance < 0:
		print("The orcs decided to leave you alone and travel on their way.")
	elif chance >= 0 < 99:
		print("You must have looked a bit too strong. They gather around you.")
		print("""
		The orcs stand around you, there are three of them. One looks a little tougher than the other two.
		Why do they always travel in groups of three.
		""")
		print("	1)	Fight these guys, show them what you're made of.")
		print("	2)	Try to slip away and escape. You can't take all three of them.")
		print("	3)	Inquire about the Orc's stats.\n")
		choice_orc = int(input())
		if choice_orc == 1:
			battle(player, enemies.orc_1,orcs)
			print("Do you want to try to fight the next one, or run?")
			print("	1)	Run")
			print("	2) Keep Fighting!")
			choice_orc2 = int(input())
			if choice_orc2 == 1:
				print("You, bing smaller and faster than the lumbering orcs, dart away successfully.")
			elif choice_orc2 == 2:
				battle(player, enemies.orc_2,orcs)
				print("Do you want to try to fight the last one, or run? This guy does look a bit tougher")
				print("	1)	Run")
				print("	2) Keep Fighting!")
				choice_orc3 = int(input())
				if choice_orc3 == 1:
					print("You, bing smaller and faster than the lumbering orcs, dart away successfully.")
				elif choice_orc3 == 2:
					battle(player, enemies.orc_3,orcs)
					print("You have defeated all of the orcs! You rightfully take what is yours.")
					loot(3)
		elif choice_orc == 2:
			print("You, bing smaller and faster than the lumbering orcs, dart away successfully.")
			return None
		elif choice_orc == 3:
			print(enemies.orc_1.inquire())
			print(enemies.orc_2.inquire())
			print(enemies.orc_3.inquire())
			orcs()
		else:
			print("You didn't type one of the possible choices.")
			orcs()
	
def demon():
	print("""
	Floating in the sky above you see a demon. 
	Its red wings flap to keep it afloat.
	It approaches you.
	""")
	print("	1)	Run Away as fast as you can!")
	print("	2)	Stand your ground and fight the demon.")
	print("	3)	Inquire about the Demon's stats.")
	choice_demon = int(input())
	if choice_demon == 1:
		flee_chance = random.randint(0,100)
		if flee_chance < 50:
			print("You manage to escape the Demon's sight and continue on your path.")
		else:
			print("The Demon still sees you and is probably more angry now that you ran.")
			demon()
	elif choice_demon == 2:
		battle(player, enemies.demon_1, demon)
		print("Knowing the value of Demon's blood, You collect some in a small vial.")
		if items.demons_blood in player.inv:
			items.demons_blood.quanity = items.demons_blood.quanity + 1
		else:
			player.inv.append(items.demons_blood)
		print("You have aquired a Vial of Demon's Blood!")
	elif choice_demon == 3:
		print(enemies.demon_1.inquire())
		demon()
	else:
		print("You did not choose a valid option.")
		demon()
	
def rest_stop():						#HAVE NOT ADDED TO LIST! NEED TO!
	print("""
	You see a small group of people gathered around a campfire.
	They beckon you over to them offering food and rest.
	""")
	print("	1)	Sit at campfire and rest.")
	print("	2)	Continue on your journey.")
	print("/n/n What would you like to do?")
	choice_rest = int(input())
	if choice_rest == 1:
		actions.rest(player)
		print("You wake fully rested and contine on your path.")
	elif choice_rest == 2:
		pass
	else:
		print("You did not choose a valid option.")
		rest_stop()
	
"""===		Rare Occurances		==="""	
	
	
def doug():
	count = 0
	if count >= 1:
		return None
	else:
		print("""
		A Knight in an all Black suit of armor approaches.
		His hair flows out of the back of his helmet in thick locks.
		He draws his weapon, a large sword with golden features.
		
		"I do not wish to fight you," He says, "This armor is possesed
		help me get rid of it, and this blade is yours!
		
		The only way I know of to get this armor off of me is to be defeated in combat!"
		""")
		print("	1)	Accept his quest.")
		print("	2)	This Knigh is scary. Run away.")
		print("	3)	Check his stats.")
		print("	4)	Check Your stats.")
		print("\n\n What would you like to do?")
		choice_doug = int(input())
		if choice_doug == 1:
			print("""
		Thank you! I shall try to go easy on you, but really you are fighting demonic armor and not me.
			""")
			battle(player, enemies.doug, doug)
			print("""
			"Thank you, warrior!" The knight says as teh helmet bounces on the ground.
			"I am a man of honor, so I will bestow this blade unto you."
			""")
			print("You have aquired the Blade of Douglas!")
			player.inv.append(items.dougsword)
			count = count + 1
		elif choice_doug == 2:
			print("spooked by the spooky dude, you run away.")
		elif choice_doug == 3:
			print(enemies.doug.inquire())
			doug()
		elif choice_doug == 4:
			print(player.check_equip())
			doug()
		else:
			print("You did not choose a valid option.")
			doug()
				
def karl():
	print("karl")
	
def barry():							#GIVES GENE'S AXE! BEST ITEM IN GAME!
	print("Barry")
	
def connor():
	print("Connor")
	
def jimmy():
	print("jimmy")
	
