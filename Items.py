#trying to add certain number of items to inventory idk if this will work
class Items():
	def __init__(self):
		self.droidPop = 0
		self.inventory = []

	def droid_pop(self):
		takeP = input("[Take] droid poppers? (Who knows, you may need them.):\n").lower()
		
		taken = ''
		while takeP != "take":
			print('''Are you sure you don't want to "TAKE" them?''')
			takeP = input("[Take] droid poppers? (Who knows, you may need them.):\n").lower()
			break
		if takeP == "take":
			self.droidPop = 2
			self.inventory.append(self.droidPop)
			print("\nDroid Poppers added to your inventory.\n")
			taken = True
			return taken
		else:
			print("You did not take the droid poppers.")
			taken = False
			return taken

	def use_inv(self):
		taken = True
		if self.droidPop in self.inventory:
			print("It'll be difficult to deflect blaster bullets with those shields up.\nThose droid poppers will sure be helpful!")
			use = input("[Use] droid poppers?").lower()
			if use == 'use':
				self.droidPop -= 1
				self.inventory.append(self.droidPop)
				print(f"You used 1 droid popper. You have {self.inventory} left.")
		