
#unused code
###i don't have enough time to figure out to do this. also i am lazy. so im just gonna keep the code here and hope for some points on save/load
#the prettiest menu
def menu(plyrName):
	print('\t*.+|-MENU-|+.*\ns - [Start new game]\nl - [Load game]\nq - [Quit]')
	o = input("Choose an option:\n").lower()
	while o not in ("s", 'l', 'q'):
		print('\t*.+|-MENU-|+.*\ns - [Start new game]\nl - [Load game]\nq - [Quit]')
		o = input("Choose an option:\n").lower()
	if o == "s":
		print("Starting game...\n")
	if o == "l":
		game = load(plyrName, Items, rooms)
		if game:
			print("Retrieving data...\n")
		else:
			print("\nFile could not be found. Try starting a new game.")
			menu(plyrName)
	if o == "q":
		print("Goodbye, may the force be with you.")
		exit()


#saving game
def save(plyrName, Items, rooms):
	print("\nNow seems like a good time to [save] the game...")
	r = input("[Save] game?:\n").lower()
	if r != "save":
		print("Are you sure you don't want to save your game?")
		r = input("[Save] game?:\n").lower()
	if r == "save":
		with open(plyrName + ".bin", "wb")as file:
			pickle.dump({'name':plyrName,'items':Items,'rooms':rooms}, file)
		
	else:
		print("You did not save the game.")
		input("Press enter to continue")

#loading game
def load(plyrName, Items, rooms):
	
	plyrName = input("Enter player name:\n")
	if os.path.exists(plyrName + ".bin"):
		with open(plyrName + ".bin", "rb")as file:
			loaded = pickle.load(file)
			plyrName = loaded['name']
			Items = loaded['items']
			rooms = loaded['rooms']
		return True
	else:
		return False


#quit
def exit_game():
	q = input("Would you like to [quit] the game?:\n").lower()
	if q != "quit":
		q = input("Are you sure you don't want to [quit] the game?:\n").lower()
	if q == "quit":
		exit()
	else:
		input("Press enter to continue")

#menu(plyrName)

#imported stuff
from Items import Items
import random
import pickle
import os#someone helped me

diedEnd = "\tYou died and failed to save the chancellor..."
goodEnd = "\tYou successfully saved the Chancellor! The Jedi Council promoted you to the rank of Jedi Master! Yippee!"

#max HP for player
jediPlyrHP = 35

lightsaberDMG = 5
B1DroidHP = 10
blasterDMG = 2
droidekaHP = 15
#boss battle
magnaGuardHP = 40
magnaDMG = 5
#recovers player HP
stimPak = 20



#all the frickin rooms
rooms = {'Hangar': '\nYou spot a hallway and a door. Find a port for your droid.',
		'Elevator': '\nYou go through the hallway. At the end of the hallway, there are elevators.\nLooks like you need a droid to operate the elevators.',
		'tinyRoom': "\nYou enter a small control room, and to your luck, it has a port for your droid.\nYour droid plugs into the port and gets the location of Chancellor Palpatine. He is in the command bridge!\nBefore you leave the room, you spot something shiny. It's some droid poppers! Wonder how these got here...",
		'elevatorEnter': "\nThe elevator doors open. You and your droid enter the elevator.\nYou press a button and the elevator begins to move.\n...\nThe elevator comes to a stop and the doors open.",
		'puzzleRoom': "\nYou and your droid enter the room and hear a 'click' sound. You turn around to see what made the noise.\nOh no!\nYou're locked in the room!\nTry and a find a way out, you still need to get to Chancellor Palpatine.\n\t<There is a strange mechanism at the center of the room.>",
		"hallway": "\nThere is a hallway leading to a door at the end.",
		"droideka": "\nThe door opens as you approach it. Once it opens, 2 droidekas roll in and begin shooting at you!",
		"bridge": "\nThis door won't budge! What could be hiding in there? Could it be the Chancellor?\nYou take out your lightsaber and begin cutting a hole through the door, because why would you waste time finding some key card when you literally have a lightsaber that can cut through pretty much anything?(im looking at you jedi fallen order).\nYou finally make it in the command bridge, and there he is! The Chancellor!"}

paths = ('north', 'n', 'south', 's', 'east', 'e', 'west', 'w')
error_msg = "Invalid input. You need to use either north/n, south/s, east/e, or west/w."

#silly little fill in the blank of star wars quotes
def mini_game():
	print("\nYou walk up to the strange mechanism, you see a button and press it.")
	print("A hologram pops up and begins speaking to you.")
	print('''"Welcome to the galaxy's best fill in the blank game!"''')
	print('"In this game you must fill in the blank of iconic quotes from Star Wars!"')
	print('"If you want to escape this room, you must get all three answers correct!"')
	print('''"If you don't get the all answers correct, you'll get killed by the blasters pointed directly at your head at your head!" :D''')
	print(f"\nBlast! There really are blasters pointed at your head! Guess you better play along!")
	
	print("\n\t~|STAR WARS FILL IN THE BLANK|~")
	print("\nHere is your first quote! You are allowed to ask for one hint! Just type '?'")
	print('"Why, you stuck up, half-witted, scruffy-looking, ____ herder!" -Leia Organa') #nerf
	
	correct = 0
	answer1 = "nerf"
	answer2 = "shorter"
	answer3 = "force"

	ans = input("What word should go in the blank?:\n").lower()
	while correct != 3:
		if ans == answer1:
			print("\nCorrect!\nNow on to the second quote!")
			input("Press enter to continue")
			correct += 1
		elif ans == "?":
			print("\nYour hint is: It's 'nerf' or nothing")
			ans = input("What word should go in the blank?:\n").lower()
			if ans == answer1:
				print("Correct!\nNow on to the second quote!")
				input("Press enter to continue")
				correct += 1
			else:
				print(f"Whoops! That wasn't correct!\nThe correct anwser was '{answer1}'.")
				print("The blasters instantly fire at you!")
				print(diedEnd)
				input("Press enter to restart")
				return mini_game()
		else:
			print(f"Whoops! That wasn't correct!\nThe correct anwser was '{answer1}'.")
			print("The blasters instantly fire at you!")
			print(diedEnd)
			input("Press enter to restart")
			return mini_game()
			
		
		print("\nHere is your second quote! You are allowed to ask for one hint! Just type '?'")
		print('''"General Grievous, you're _______ than I expexted." -Anakin Skywalker''')#shorter
		ans = input("What word should go in the blank?:\n").lower()
		if ans == answer2:
			print("\nCorrect!\nNow on to the third and final quote!")
			input("Press enter to continue")
			correct += 1
		elif ans == "?":
			print("\nYour hint is: The opposite of taller")
			ans = input("What word should go in the blank?:\n").lower()
			if ans == answer2:
				print("\nCorrect!\nNow on to the third and final quote!")
				input("Press enter to continue")
				correct += 1
			else:
				print(f"\nWhoops! That wasn't correct!\nThe correct anwser was '{answer2}'.")
				print("The blasters instantly fire at you!")
				print(diedEnd)
				input("Press enter to restart")
				return mini_game()
		else:
			print(f"\nWhoops! That wasn't correct!\nThe correct anwser was '{answer2}'.")
			print("The blasters instantly fire at you!")
			print(diedEnd)
			input("Press enter to restart")
			return mini_game()

		print("\nHere is your third quote! You are allowed to ask for one hint! Just type '?'")
		print('"May the _____ be with you"')#force
		ans = input("What word should go in the blank?:\n").lower()
		if ans == answer3:
			print("\nCorrect!\nYou got all of them correct! Hooray!")
			input("Press enter to continue")
			correct += 1
		elif ans == "?":
			print("\nYour hint is: A power the Jedi possess")
			ans = input("What word should go in the blank?:\n").lower()
			if ans == answer3:
				print("\nCorrect!\nYou got all of them correct! Hooray!")
				input("Press enter to continue")
				correct += 1
			else:
				print(f"\nWhoops! That wasn't correct!\nThe correct anwser was '{answer3}'.")
				print("The blasters instantly fire at you!")
				print(diedEnd)
				input("Press enter to restart")
				return mini_game()
		else:
			print(f"\nWhoops! That wasn't correct!\nThe correct anwser was '{answer3}'.")
			print("The blasters instantly fire at you!")
			print(diedEnd)
			input("Press enter to restart")
			return mini_game()
	if correct == 3:
		print("\nAll of the doors have been unlocked!\nYou can now continue with your mission!")
		



#fight B1 battledroids
def fight_B1():
	jediPlyrHP = 35
	lightsaberDMG = 5
	blasterDMG = 2
	
	print("\nYou ignite your lightsaber and begin fighting the battle droids.")
	defeatedDroids = 0
	while defeatedDroids != 3:
		B1DroidHP = 10
		while B1DroidHP > 0 and defeatedDroids != 3:
			hit = random.randrange(2)
			if hit:
				jediPlyrHP -= blasterDMG
				print(f"\nA droid hits you, your HP is now: {jediPlyrHP}")
			else:
				print("\nA droid shoots at you but misses.")
			print("\nYou deflect several blaster bullets and send them right back to the enemy.")
			B1DroidHP -= lightsaberDMG
			print(f"Droid HP:{B1DroidHP}")
			if B1DroidHP == 0:
				defeatedDroids += 1
				input(f"\nYou defeated {defeatedDroids} droid(s)!\nPress enter to continue")
	if defeatedDroids == 3:
		print("\nYou defeated all the droids!")

#fight droidekas. if player didn't get droid poppers they lose a little extra health because they have to get closer to the droideka and can't deflect blaster shot cuz shield idk

def fight_ekas(taken):
	jediPlyrHP = 35
	lightsaberDMG = 5
	blasterDMG = 2
	items = Items()
#when you say things are roger roger, but they are not roger roger :'(
	defeatedDroids = 0
	print("\nYou ignite your lightsaber and begin fighting the droidekas.")

#this is if the player took the droid poppers from earlier.
	if taken == True:#sorry im gonna force you to use them or something i cant figure out how to do crap. ur not gonna use them after this and i need to finish this quickly
		while defeatedDroids != 2:
			print(items.use_pop())
			print("\nYou chuck a droid popper at one of the droidekas. It rolls into its shield.")
			print("The droideka is instantly taken out!")
			defeatedDroids += 1
			
			input("Press enter to continue")
		if defeatedDroids == 2:
			print("\nYou defeated all the droidekas!")

#this is if the player didn't take the droid poppers from earlier
	else:
		while defeatedDroids != 2:
			droidekaHP = 15
			while droidekaHP > 0 and defeatedDroids != 2:
				hit = random.randrange(2)
				if hit:
					jediPlyrHP -= blasterDMG
					print(f"\nA droid hits you, your HP is now: {jediPlyrHP}")
				else:
					print("\nA droid shoots at you but misses.")
				print("\nYou deflect several blaster bullets and send them right back to the enemy.")
				droidekaHP -= lightsaberDMG
				print("Since there are blaster shields protecting the droidekas, you have to get close to kill the droidekas.\nYou lose extra HP. :(")
				jediPlyrHP -= blasterDMG
				print(f"Your HP is now: {jediPlyrHP}")
				print(f"Droid HP:{droidekaHP}")
				if droidekaHP == 0:
					defeatedDroids += 1
					input(f"\nYou defeated {defeatedDroids} droid(s)!\nPress enter to continue")
		if defeatedDroids == 2:
			print("\nYou defeated all the droidekas!")

#BOSS FIGHT magna guards
def boss_fight():
	magnaGuardHP = 40
	magnaDMG = 5
	jediPlyrHP = 35
	lightsaberDMG = 5
	items = Items()
	
	print("\nYou ignite your lightsaber and begin fighting the MagnaGuards.")
	defeatedDroids = 0
	while defeatedDroids != 2:
		magnaGuardHP = 40
		while magnaGuardHP > 0 and defeatedDroids != 2:
			hit = random.randrange(2)
			if hit:
				jediPlyrHP -= magnaDMG
				print(f"\nOne of the MagnaGuards hits you, your HP is now: {jediPlyrHP}")
				if jediPlyrHP <= 10:
					items.use_stim(jediPlyrHP, stimPak)
					jediPlyrHP += stimPak
					print(f"Your HP is now: {jediPlyrHP}")
				if jediPlyrHP == 0: #if player somehow dies
					print("The MagnaGuards electrocute you to death.")
					print(diedEnd)
					input("Press enter to restart")
					return boss_fight()
			else:
				print("\nOne of the MagnaGuards strikes at you, but you dodge out of harms way.")
			
			print("\nYou parry several attacks and attack when you have the chance.")
			magnaGuardHP -= lightsaberDMG
			print(f"MagnaGuard HP: {magnaGuardHP}")
			if magnaGuardHP == 0:
				defeatedDroids += 1
				print(f"\nYou defeated {defeatedDroids} MagnaGuard(s)!")
				input("Press enter to continue")
	if defeatedDroids == 2:
		print("\nYou've successfully defeated the MagnaGuards!")



print("Welcome to\n\t*.-|Star Wars: Save the Chancellor!|-.*")
print("In this game your main objective is to save Chancellor Palpatine, who has been captured by the Separatists.\n")
#player needs to enter name plz
plyrName = input("Enter your epic Jedi name:\n")
while plyrName == "":
	print("Please enter your name to continue.")
	plyrName = input("Enter your epic Jedi name:\n")


#key and greeting player.
print(f"Greetings, {plyrName}! Here is a key to navigate in the game.")
print("KEY: north/n, south/s, east/e, west/w, flee, fight, use, take") 
print("\t(Note: You only use your inventory while in battle. Also I apologize if I have any missed spelling errors in the game.)")
input("Press enter to continue")

print(f"\nHello there, Jedi {plyrName}. We need your help to save Chancellor Palpatine.\nHe has been captured by the Separatists. It is rumored that he was captured by the leader of the droid army, General Grievous.")
input("Press enter to continue")
print("\nPrepare your starfighter and be prepared to board his ship. Good luck! And may the force be with you!")
print("<You start up your starfighter and fly over to the the Separatist Frigate.>")
input("Press enter to continue")

print("\nThere is only one way in, through the hangar.")
pathOption = input("Available paths: north\n").lower()
print()
while pathOption not in paths:
	print(error_msg)
	print("\nThere is only one way in, through the hangar.")
	pathOption = input("Available paths: north\n").lower()
if pathOption == "north" or pathOption == "n":
	print("You swoop into the hangar and quickly exit your ship.\nSuddenly, a large group of Separatist battle droids are surrounding you. They have been awaiting your arrival.")
	fleeOrfight = input("Do you flee or fight?:\n").lower()
	while fleeOrfight not in ('flee', 'fight'):
		print('\nInvalid input. Are you going to "FLEE" or "FIGHT?"')
		fleeOrfight = input("Do you flee or fight?:\n").lower()
	if fleeOrfight == "flee":
		print("\nYou try to flee, the battle droids instantly shoot you down.")
		print(f'\t{diedEnd}')
		input("\nPress enter to restart.\n")
		print("You swoop into the hangar and quickly exit your ship.\nSuddenly, a large group of Separatist battle droids are surrounding you. They have been awaiting your arrival.")
		fleeOrfight = input("Do you flee or fight?:\n").lower()
	while fleeOrfight not in ('flee', 'fight'):
		print('\nInvalid input. Are you going to "FLEE" or "FIGHT?"')
		fleeOrfight = input("Do you flee or fight?:\n").lower()
	if fleeOrfight == 'fight':
		fight_B1()
		input("Press enter to continue")

print(f"\nNow that you've taken down those clankers, you must locate where the Chancellor is Jedi {plyrName}.")
print("Good thing you have your trusty astromech droid to help!")
print("But first your droid needs a port to plug into.")
#save point
##save(plyrName, Items, rooms)
##exit_game()
print(rooms['Hangar'])
option = input("Available paths: north, east\n").lower()

#time to find the location of chancellor poopy
palpsLocation = False
while option not in paths:
	print(error_msg)
	print(rooms['Hangar'])
	option = input("Available paths: north, east\n").lower()

if option in ("north", "n"):
	print(rooms['Elevator'])
	useDroid = input("[Use] droid?:\n").lower()
#can't use elevator unless you have chancellor's location
	while useDroid != "use":
			print('You should probably "USE" your droid')
			useDroid = input("[Use] droid?:\n").lower()
	
	if useDroid == "use" and palpsLocation == False:
		print("\n*You need to find the location of Chancellor Palpatine first.*")
		option = input("Available paths: south\n").lower()

		while option not in paths:
			print(error_msg)
			print("\n*You need to find the location of Chancellor Palpatine first.*")
			option = input("Available paths: south\n").lower()

		if option in ("south", "s"):
			print("\nYou head back to the hangar.")
			print(rooms['Hangar'])
			option = input("Available paths: north, east\n")#i have no idea what im doing
			while option not in paths:
				print(error_msg)
				print(rooms['Hangar'])
				option = input("Available paths: north, east\n").lower()

			if option in ("north", "n"):
				print(rooms['Elevator'])
				useDroid = input("[Use] droid?:\n").lower()
			#can't use elevator unless you have chancellor's location
				while useDroid != "use":
						print('You should probably "USE" your droid')
						useDroid = input("[Use] droid?:\n").lower()
				
				if useDroid == "use" and palpsLocation == False:
					print("\n*You need to find the location of Chancellor Palpatine first.*")
					option = input("Available paths: south\n").lower()

					while option not in paths:
						print(error_msg)
						print("\n*You need to find the location of Chancellor Palpatine first.*")
						option = input("Available paths: south\n").lower()

					if option in ("south", "s"):
						print("\nYou head back to the hangar.")
						print(rooms['Hangar'])
						option = input("Available paths: east\n").lower() #no more going north the game will crash and idk what to do
						while option not in paths:
							print(error_msg)
							option = input("Available paths: east\n").lower()

#this is where you find the location of the chancellor
if option in ("east", "e"):
	print(rooms['tinyRoom'])
	palpsLocation = True
	items = Items()
	taken = items.droid_pop()
	option = input("Available paths: west\n").lower()

	while option not in ("west", "w"):
		print(error_msg)
		option = input("Available paths: west\n").lower()

	if option in ("west", "w"):
		print("\nYou head back to the hangar.")
		print(rooms['Hangar'])
		option = input("Available paths: north, east\n").lower()

		while option not in paths:
			print(error_msg)
			option = input("Available paths: north, east\n").lower()
		if option in ("north", "n"):
			print(rooms['Elevator'])
			useDroid = input("[Use] droid?:\n").lower()
		
			while useDroid != "use":
				print('You should probably "USE" your droid')
				useDroid = input("[Use] droid?:\n").lower()

			if useDroid == "use" and palpsLocation == False:
				print("\n*You need to find the location of Chancellor Palpatine first.*")
				option = input("Available paths: south\n").lower()
			else:
				print("Your droid plugs into the elevator port.")
				print(rooms['elevatorEnter'])
				input("Press enter to continue")
		
		while option not in paths:
			print(error_msg)
			option = input("Available paths: north, east\n").lower()
		if option in ("east", "e") and taken == True:
			print("\nYou enter a small control room.")
			palpsLocation = True
			option = input("Available paths: west\n").lower()
			while option not in ("west", "w"):
					print(error_msg)
					option = input("Available paths: west\n").lower()

			if option in ("west", "w"):
				print("\nYou head back to the hangar.")
				print(rooms['Hangar'])
				option = input("Available paths: north\n").lower()
				while option not in paths:
					print(error_msg)
					option = input("Available paths: north\n").lower()
				if option in ("north", "n"):
					print(rooms['Elevator'])
					useDroid = input("[Use] droid?:\n").lower()
				
					while useDroid != "use":
						print('You should probably "USE" your droid')
						useDroid = input("[Use] droid?:\n").lower()

					if useDroid == "use" and palpsLocation == False:
						print("\n*You need to find the location of Chancellor Palpatine first.*")
						option = input("Available paths: south\n").lower()
					else:
						print("Your droid plugs into the elevator port.")
						print(rooms['elevatorEnter'])
						input("Press enter to continue")

		while option not in paths:
			print(error_msg)
			option = input("Available paths: north, east\n").lower()
		if option in ("east", "e") and taken == False:
			print(rooms['tinyRoom'])
			palpsLocation = True
			items = Items()
			taken = items.droid_pop()
			option = input("Available paths: west\n").lower()
			while option not in ("west", "w"):
					print(error_msg)
					option = input("Available paths: west\n").lower()

			if option in ("west", "w"):
				print("\nYou head back to the hangar.")
				print(rooms['Hangar'])
				option = input("Available paths: north\n").lower()#no more east
				while option not in paths:
					print(error_msg)
					option = input("Available paths: north\n").lower()
				if option in ("north", "n"):
					print(rooms['Elevator'])
					useDroid = input("[Use] droid?:\n").lower()
				
				while useDroid != "use":
					print('You should probably "USE" your droid')
					useDroid = input("[Use] droid?:\n").lower()

				if useDroid == "use" and palpsLocation == False:
					print("\n*You need to find the location of Chancellor Palpatine first.*")
					option = input("Available paths: south\n").lower()
				else:
					print("Your droid plugs into the elevator port.")
					print(rooms['elevatorEnter'])
					input("Press enter to continue")#im sure there is an easier way to do whatever i just did, i just don't know it ;-;


print("\nYou and your droid exit the elevator.\nThere seems to be a room up ahead.")
op = input("Available paths: north\n").lower()

while op not in paths:
	print(error_msg)
	op = input("Available paths: north\n").lower()

if op in ("north", "n"):
	print(rooms['puzzleRoom'])
	op = input("Available paths: north\n").lower()

	while op not in paths:
		print(error_msg)
		op = input("Available paths: north\n").lower()
	if op in ("north", "n"):
		mini_game()

print(rooms['hallway'])
#save point
##save(plyrName, Items, rooms)
##exit_game()
op = input("Available paths: north\n").lower()
while op not in paths:
	print(error_msg)
	print(rooms['hallway'])
	op = input("Available paths: north\n").lower()

if op in ("north", "n"):
	print(rooms['droideka'])
	input("Press enter to continue")
	fight_ekas(taken)
input("Press enter to continue")
print("\nBefore you leave, you spot something in the corner of the room.\n...\nThey're stimpaks! You can use stimpaks to heal yourself during battle!")
items = Items()
items.stim()

op = input("Available paths: east\n").lower()
while op not in paths:
	print(error_msg)
	op = input("Available paths: east\n").lower()

if op in ("east", "e"):
	print(f"We're almost there Jedi {plyrName}! I feel it in the force!\nYou got this!")
	print("There are more elevators.\nLooks like you need a droid to operate the elevators.")
	use = input("[Use] droid?:\n").lower()

	while use != "use":
		print('You should probably "USE" your droid')
		useDroid = input("[Use] droid?:\n").lower()
	if use == "use":
		print("Your droid plugs into the elevator port.")
		print(rooms['elevatorEnter'])
input("Press enter to continue")

print(rooms['hallway'])
#save point
##save(plyrName, Items, rooms)
##exit_game()

print(rooms['bridge'])
input("Press enter to continue")
print(f'''\n"Not so fast Jedi {plyrName}."
It's General Grievous!
"If you want your Chancellor back, you must fight for it!"*coughing*
Suddenly, 2 MagnaGuards appear behind you!
It's time save the Chancellor, get rid of those guards Jedi {plyrName}!''')
input("Press enter to continue")
boss_fight()
input("Press enter to continue")
print('''The guards are now defeated, but it seems General Grievous has escaped.
Typical. Oh well, we'll get him next time.
You grab Chancellor Palpatine and head to the nearest escape pod, you need to get out quickly.''')
input("Press enter to continue")
print('''\n...
You and the Chancellor succesfully escape the Separatist Frigate and make your way back to Coruscant!\n''')
print(goodEnd)
print("May the force be with you!")