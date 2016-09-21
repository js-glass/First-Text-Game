"""	=== Quest Log	===		"""

class quest(object):
	
	def __init__(self, name, descrip, stage):
		self.name = name
		self.descrip = descrip
		self.stage = stage
		
	def getname(self):
		return self.name
		
	def getdescrip(self):
		return self.descrip
		
	def getstage(self):
		return self.stage
		
	def __str__(self):
		return "{} \n === \n {}".format(self.name, self.descrip)


class Main(quest):
	
	def __init__(self, name, descrip, stage):
		self.name = "Main Quest."
		self.descrip = "King Todd has asked you to defeat the Dragon and retrieve his MacGuffin."
		self.stage = 1
		is_active = True
		
	def stage_1(self):
		pass
		
	def stage_2(self):
		pass
		
	def stage_3(self)
		pass

class Witch_q(quest):

	def __inti__(self, name, descrip, stage):
		self.name = "WHitch Witch is Witch?"
		self.descrip = "Lunk the Elf wants you to kill a witch in exchance for his demonic essence retrieval."
		self.stage = 0
		is_active = False
		
	def stage_1(self):
		pass
		
	def stage_2(self):
		pass
		
	def stage_3(self):
		pass