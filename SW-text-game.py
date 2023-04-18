from Items import Items


#imported stuff above
diedEnd = "You died and failed to save the chancellor..."
goodEnd = "You successfully saved the Chancellor! The Jedi Council promoted you to the rank of Jedi Master! Yippee!"

#max HP for player
jediPlyrHP = 35
#can add more damage to weapon during game
lightsaberDMG = 5
B1DroidHP = 10
blasterDMG = 2
droidekaHP = 15
B2droidHP = 25
#boss battle
magnaDroidHP = 40
magnaDMG = 5
#helps recover player HP
stimpak = 6
import random

inventory = []

#all the frickin rooms
rooms = {'Hangar': '\nYou spot a hallway and a door. Find a port for your droid.',
		'Elevator': '\nYou go through the hallway. At the end of the hallway, there are elevators.\nLooks like you need a droid to operate the elevators.',
		'tinyRoom': "\nYou enter a small control room, and to your luck, it has a port for your droid.\nYour droid plugs into the port and gets the location of Chancellor Palpatine. He is in the command bridge!\nBefore you leave the room, you spot something shiny. It's some droid poppers! Wonder how these got here...",
		'elevatorEnter': "\nThe elevator doors open. You and your droid enter the elevator.\nYou press a button and the elevator begins to move.\n...\nThe elevator comes to a stop and the doors open.",
		'PuzzleRoom': "\nYou and your droid enter the room and hear a 'click' sound. You turn around to see what made"}

paths = ('north', 'n', 'south', 's', 'east', 'e', 'west', 'w')
error_msg = "Invalid input. You need to use either north/n, south/s, east/e, or west/w."




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


print("Welcome to Star Wars: Save the Chancellor!")
print("In this game your main objective is to save Chancellor Palpatine, who has been captured by the Separatists.\n")
#player needs to enter name plz
plyrName = input("Enter your epic Jedi name:\n")
while plyrName == "":
	print("Please enter your name to continue.")
	plyrName = input("Enter your epic Jedi name:\n")

#key and greeting player.
print(f"Greetings, {plyrName}! Here is a key to navigate in the game.")
print("KEY: north/n, south/s, east/e, west/w, up, down, flee, fight, use, take, inventory, save, load, quit")
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
		print("\nInvalid input. Are you going to FLEE or FIGHT?")
		fleeOrfight = input("Do you flee or fight?:\n").lower()
		if fleeOrfight == "flee":
			print("\nYou try to flee, the battle droids instantly shoot you down.")
			print(f'\t{diedEnd}')
			input("\nPress enter to restart.\n")
			print("You swoop into the hangar and quickly exit your ship.\nSuddenly, a large group of Separatist battle droids are surrounding you. They have been awaiting your arrival.")
			fleeOrfight = input("Do you flee or fight?:\n").lower()
	if fleeOrfight == 'fight':
		fight_B1()
input("Press enter to continue")

print("\nNow that you've taken down those clankers, you must locate where the Chancellor is.")
print("Good thing you have your trusty astromech droid to help!")
print("But first your droid needs a port to plug into.")
print(rooms['Hangar'])
hangarOption = input("Available paths: north, east\n").lower()

palpsLocation = False
while hangarOption not in paths:
	print(error_msg)
	print(rooms['Hangar'])
	hangarOption = input("Available paths: north, east\n").lower()

	if hangarOption in ("north", "n"):
		print("\nYou go through the hallway. At the end of the hallway, there are elevators.")
		print("Looks like you need a droid to operate the elevators.")
		useDroid = input("Use droid?:\n")

		if useDroid and palpsLocation == False:
			print("\n*You need to find the location of Chancellor Palpatine first.*")
			option = input("Available paths: south\n").lower()

			if hangarOption in ("north", "n"):
			print("\nYou go through the hallway. At the end of the hallway, there are elevators.")
			print("Looks like you need a droid to operate the elevators.")
			useDroid = input("Use droid?:\n")

			if useDroid and palpsLocation == False:
				print("\n*You need to find the location of Chancellor Palpatine first.*")
				option = input("Available paths: south\n").lower()
				if option in ("south", "s"):
					print("\nYou head back to the hangar.")
					print(rooms['Hangar'])
					option = input("Avaiable paths: north, east\n")


if hangarOption in ("east", "e"):
	print(rooms['tinyRoom'])
	palpsLocation = True
	items = Items()
	items.droid_pop()
	option = input("Available paths: west\n")

	if option in ("west", "w"):
		print("\nYou head back to the hangar.")
		print(rooms['Hangar'])
		option = input("Available paths: north, east\n").lower()

		if option in ("north", "n"):
			print("\nYou go through the hallway. At the end of the hallway, there are elevators.")
			print("Looks like you need a droid to operate the elevators.")
			useDroid = input("Use droid?:\n").lower()
		if useDroid == "use" and palpsLocation == False:
			print("\n*You need to find the location of Chancellor Palpatine first.*")
			option = input("Available paths: south\n").lower()
		else:
			print("Your droid plugs into the elevator port.")
			print(rooms['elevatorEnter'])


