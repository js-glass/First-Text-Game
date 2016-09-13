"""===		Enemies		==="""


all_enemies = []

class enemy(object):
	def __init__(self, name, descrip, hp, damage, speed):
		self.name = name
		self.descrip = descrip
		self.hp = hp
		self.damage = damage
		self.speed = speed
		all_enemies.append(self)
		
	def is_alive(self):
		return self.hp > 0
		
	def inquire(self):
		return "{}\n========== \n{}\n    Health = {}\n    Damage = {}\n".format(self.name, self.descrip, self.hp, self.damage)
	
	def hit(self, hit):
		self.hp = self.hp - hit
		return self.hp
	
	def potion_use(self, hit):
		self.hp = self.hp + hit
		return self.hp
		
		
		
orc_1 = enemy("Orcish Warrior",
	"A lumbering mountain of muscle and strength weilding a battleaxe.\n",
	hp = 75,
	damage = 15,
	speed = 10
	)
	
orc_2 = enemy("Orcish Crusader",
	"A muscular green humanoid with an angry grin on his face.\n",
	hp =75,
	damage = 15,
	speed = 10
	)
	
orc_3 = enemy("Orcish Leader",
	"This orc appears to have command over the others.\n",
	hp = 100,
	damage = 25,
	speed = 15
	)


giant_spider = enemy("Giant Spider",
	"Crawls around on eight legs ready to wrap it's prey in a \nweb for later consumption.\n",
	hp = 50,
	damage = 15,
	speed = 25
	)


demon_1 = enemy("Demon Knight",
	"Red skinned and 6 and a half feet tall, this Demon holds tightly to its blade, ready for combat.\n",
	hp = 100,
	damage = 20,
	speed = 20
	)
	
demon_2 = enemy("Demon Fighter",
	"Large and imposing, this Demon is ready to devour any living thing \nthat comes its way.\n",
	hp = 100,
	damage = 20,
	speed = 20
	)
	
demon_lord = enemy("Demon Lord",
	"Holding a red trident, this Demon looks like the Devil himself.\n",
	hp = 125,
	damage = 30,
	speed = 25
	)
	
witch = enemy("Witch",
	"wrinkled and ugly, this creature of greed and anger slinks along casting spells and incantations",
	hp = 150,
	damage = 15,
	speed = 5
	)

dragon = enemy("High Dragon",
	"Sitting atop a mountain of Gold alongside the MacGuffin, this dragon waits your approach.",
	hp = 250,
	damage = 30,
	speed = 15
	)
	
bandit = enemy("Bandit",
	"Aproaching from behind, this guy wants to steal your money.",
	hp = 50,
	damage = 5,
	speed = 50
	)
	
slime = enemy("Slime",
	"Gross, slimey gelatinous blob.",
	hp = 25,
	damage = 5,
	speed = 100
	)

	
'''for item in all_enemies:
	print(item.inquire())
	print(item.is_alive())'''