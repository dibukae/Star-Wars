#trying to add certain number of items to inventory idk if this will work
class Items():
	def __init__(self, droidPop = 0, inventory = [], stimpak = 3):
		self.droidPop = droidPop
		self.inventory = inventory
		self.stimpak = stimpak

	def droid_pop(self):
		takeP = input("[Take] droid poppers? (Who knows, you may need them.):\n").lower()
		
		if takeP != "take":
			print('''Are you sure you don't want to "TAKE" them?''')
			takeP = input("[Take] droid poppers? (Who knows, you may need them.):\n").lower()
		if takeP == "take":
			self.droidPop = 2
			self.inventory.append(self.droidPop)
			print("\nDroid Poppers added to your inventory.\n")
			print(f"You have {self.inventory[0]}")
			taken = True
			return taken
		else:
			print("You did not take the droid poppers.")
			taken = False
			return taken

	def use_inv(self):
		print("It'll be difficult to deflect blaster bullets with those shields up.\nThose droid poppers will sure be helpful!")
		use = input("[Use] droid poppers?\n").lower()
		while use != 'use':
			print('''You should "USE" them! It's an easy win!''')
			use = input("[Use] droid poppers?\n").lower()

		if use == 'use':
			self.inventory[0] -= 1
			print(f"You used 1 droid popper. You have {self.inventory[0]} left.")

	def stim(self):
		tak = input("[Take] stimpaks? (Who knows, you may need them.):\n").lower()
		if tak != "take":
			print('''Are you sure you don't want to "TAKE" them?''')
			tak = input("[Take] stimpaks? (Who knows, you may need them.):\n").lower()
		if tak == "take":
			self.stimpak += 3
			self.inventory.append(self.stimpak)
			print("Stimpaks added to your inventory.\n")
			print(f"You have {self.inventory[1]}")
			Taknn = True
			return Taknn
		else:
			print("You did not take the stimpaks.")
			print(f"You have {self.inventory[1]}")
			Taknn = False
			return Taknn