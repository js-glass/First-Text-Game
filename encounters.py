"""	=== Travel===	"""
import random, time, items, player, enemies, events

player = player.hero

def travel_chance(nsew):
	"""			REDO THIS ENTIRE FUNCTION!			"""



	chance = random.randint(0, 1000)
	if chance < 665:
		time.sleep(1)
		print("You travel a mile {}".format(nsew))
	elif chance >= 665 and chance < 765:
		time.sleep(1)
		chest()
	elif chance >=765 and chance < 836:
		time.sleep(1)
		bandit()
	elif chance >=836 and chance < 918:
		time.sleep(1)
		corpse()
	elif chance >= 918 and chance < 953:
		time.sleep(1)
		orcs()
	elif chance >= 953 and chance < 959:
		time.sleep(1)
		doug()
	elif chance >= 959 and chance < 962:
		time.sleep(1)
		karl()
	elif chance >= 962 and chance < 977:
		time.sleep(1)
		barry()
	elif chance >= 977 and chance <= 1000:
		time.sleep(1)
		demon()
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

def loot(amt):
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

'''===		Travel Events	==='''
				

def chest():
	"""	Provides loot to player	"""

	print("""
	As you walk, you notice a chest slightly off of your path. You open the chest and plunder it's contents.
	""")
	loot(random.randint(1,5))

def bandit():
	"""	Provides an easy challange to player	"""
	"""	Bug!!! if player has no weapon, can dupe rewards from "fighting" Bandit	"""
	print("""
	A bandit creeps up behind you. Before you are able to react, you have a weapon poking your back
	and a voice demanding you give himn your money.
	""")
	print(enemies.bandit.inquire())
	if items.money.quanity > 99:
		print("	1)	Give him 100 Gold Coins.")
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
		print("You have {} Gold remaining.".format(str(items.money.quanity)))
	elif choice_band == 1 and mon == False:
		print("Your coinpurse is nearly empty, it won't be enough to make this man happy.")
		bandit()
	elif choice_band == 2:
		print("You decide, fuck this guy for trying to steal from you!")
		events.battle(player, enemies.bandit, bandit)
		print("You take the Bandit's previous \"earnings\"")
		earnings = random.randint(50, 200)
		if len(player.inv) > 0:
			items.money.add_gold(earnings)
			print("You have aquired {} Gold Coins!".format(earnings))
		else:
			return None
	elif choice_band == 3:	
		print("You figure you can get away from this guy, just by running fast.")
		#time.sleep(1)
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
	"""	An ethical dilemma where choosing the "Good" option provides no bonus	"""

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
		loot(random.randint(1,3))
	else:
		print("You didn't choose any possible option.")
		
def orcs():
	"""	Challangeing fight, shows players that sometimes enemies are not alone.	"""

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
			events.battle(player, enemies.orc_1,orcs)
			print("Do you want to try to fight the next one, or run?")
			print("	1)	Run")
			print("	2) Keep Fighting!")
			choice_orc2 = int(input())
			if choice_orc2 == 1:
				print("You, bing smaller and faster than the lumbering orcs, dart away successfully.")
			elif choice_orc2 == 2:
				events.battle(player, enemies.orc_2,orcs)
				print("Do you want to try to fight the last one, or run? This guy does look a bit tougher")
				print("	1)	Run")
				print("	2) Keep Fighting!")
				choice_orc3 = int(input())
				if choice_orc3 == 1:
					print("You, bing smaller and faster than the lumbering orcs, dart away successfully.")
				elif choice_orc3 == 2:
					events.battle(player, enemies.orc_3,orcs)
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
	"""	Will absolutly murder a lower player. REMEMBER TO MAKE THIS RARE OR HAVE A DAMAGE REQUIRMENT FOR THIS TO OCCUR	"""
	
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
		events.battle(player, enemies.demon_1, demon)
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
	"""	Provides reprieve on long travels. MODIFY TO SHOW UP MORE OFTEN AS HEALTH LOWERS	"""
	
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
	"""	Provide unique weapon	"""
	
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
			events.battle(player, enemies.doug, doug)
			print("""
			"Thank you, warrior!" The knight says as teh helmet bounces on the ground.
			"I am a man of honor, so I will bestow this blade unto you."
			""")
			print("You have aquired the Blade of Douglas!")
			items.dougsword.quanity += 1
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
	"""	Provide unique weapon	"""
	
	print("karl")
	
def barry():
	"""	Provide unique weapon	"""
	
	print("Barry")
	
def connor():
	"""	Provide unique weapon	"""
	
	print("Connor")
	
def jimmy():
	"""	Provide unique weapon	"""
	
	print("jimmy")
	
