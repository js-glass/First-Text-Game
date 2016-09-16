import actions, world, enemies, items, player, events



bandit = 0

orc = 0

demon = 0



shop_items = []
	if player.x in world.all_cities_x and player.y in world.all_cities_y:
		print("You walk into the local Market.")
		print("\n\n	1)	Buy.")
		print("	2)	Sell")
		print("	3)	Exit the Shop")
		print("\n\n What would you like to do?")
		choice_shop = int(input())
		if choice_shop == 1:
			pos_shop = [items.gold_blade]
			for item in items.all_items:
				if item.unique == False and item.name != "Gold":
					pos_shop.append(item)
			while len(shop_items) != 10:
				shop_items.append(pos_shop[random.randint(0,len(pos_shop)-1)])
		count = 0
		for item in shop_items:
			count += 1
			print("    " + str(count) + ")  " + item.name)
		count += 1
		print("    " + str(count) + ")  " + "Nothing")
		print("\n\n What would you like to purchase?")
		choice_buy = int(input())
		if choice_buy < (len(shop_items)+ 1):
			choice_index = choice_buy - 1
			player.inv.append(shop_items[choice_index])
			items.money.sub_gold(shop_items[choice_index].value)
			shop_items.pop(choice_buy - 1)
			print("You Purchased a {}, Which cost {} Gold.".format(shop_items[choice_index].name, shop_items[choice_index].value))
			print("You have {} Gold remaining.".format(items.money.quanity))
			shop()
		else:
			shop()