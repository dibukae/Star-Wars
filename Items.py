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
			print("\nDroid Poppers added to your inventory.")
			print(f"You have {self.inventory[0]} droid popper(s).\n")
			taken = True
			return taken
		else:
			print("You did not take the droid poppers.")
			print(f"You have {self.droidPop} droid popper(s).\n")
			taken = False
			return taken

	def use_pop(self):
		print("It'll be difficult to deflect blaster bullets with those shields up.\nThose droid poppers will sure be helpful!")
		use = input("[Use] droid poppers?\n").lower()
		while use != 'use':
			print('''You should "USE" them! It's an easy win!''')
			use = input("[Use] droid poppers?\n").lower()

		if use == 'use':
			self.inventory[0] -= 1
			print(f"You used 1 droid popper. You have {self.inventory[0]} left.")#i don't know why it's returning none here

	def stim(self):
		tak = input("[Take] stimpaks? (Who knows, you may need them.):\n").lower()
		if tak != "take":
			print('''Are you sure you don't want to "TAKE" them?''')
			tak = input("[Take] stimpaks? (Who knows, you may need them.):\n").lower()
		if tak == "take":
			self.stimpak += 3
			self.inventory.append(self.stimpak)
			print("Stimpaks added to your inventory.")
			print(f"You have {self.inventory[1]} stimpak(s).\n")

		else:
			print("You did not take the stimpaks.")
			print(f"You have {self.stimpak} stimpak(s).\n")
			self.inventory.append(self.stimpak)

	
	def use_stim(self, jediPlyrHP, stimPak):
		if jediPlyrHP <= 12:
			print("Your HP is getting pretty low, you should use your stimpaks!")
			print(f"You have {self.inventory[1]} stimpak(s).\n")
			use = input("[Use] stimpaks?:\n")/lower()
			while use != "use":
				print('You should "USE" them! DO YOU WANT TO DIE?!')
				use = input("[Use] stimpaks?:\n")/lower()
			if use == "use":
				self.inventory[1] -= 1
				print(f"You used 1 stimpak. You have {self.inventory[1]} left.")
				
				jediPlyrHP += stimPak
				print(f"Your HP is now: {jediPlyrHP}")
