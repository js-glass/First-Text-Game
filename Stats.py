import actions, world, enemies, items, player, events
from operator import itemgetter, attrgetter, methodcaller

places = world.all_places
player = player.hero

def player_loc():
	for item in places:
		if (player.x,player.y) == (item.x, item.y):
			return item
			
def map_test():
	print(player_loc().name)
	actions.travel(player, 15, 1)
	print(player_loc().name)
	actions.travel(player, 15, 5)
	print(player_loc().name)
	actions.travel(player, 10, 5)
	print(player_loc().name)
	actions.travel(player, 10, 15)
	print(player_loc().name)
	actions.travel(player, 6, 15)
	print(player_loc().name)
	actions.travel(player, 1, 15)
	print(player_loc().name)
	actions.travel(player, 1, 1)
	print(player_loc().name)
	

map_test()