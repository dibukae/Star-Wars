#trying to add certain number of items to inventory idk if this will work
class Items():
	def __init__(self):
		self.droidPop = 0
		takeP = input("Take droid poppers? (Who knows, you may need them.):\n").lower()
		if takeP == "take":
			self.droidPop = 2
			inventory.append(self.droidPop)
		
	def stimpak(self):
		self.stimpak = 0