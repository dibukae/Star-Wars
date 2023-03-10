diedEnd = "You died and failed to save the chancellor..."
goodEnd = "You successfully saved the Chancellor! The Jedi Council promoted you to the rank of Jedi Master! Hooray!"

jediPlyrHP = 35
lightsaberDMG = 5
B1DroidHP = 10
blasterDMG = 2
import random

rooms = {'Hangar': '\nYou spot a hallway and a door. Find a port for your droid.',
		'Elevator': '\nYou go through the hallway. At the end of the hallway, there are elevators.\nLooks like you need a droid to operate the elevators.',
		'tinyRoom': 'You enter a small control room, and to your luck, it has a port for your droid.\nYour droid plugs into the port and gets the location of Chancellor Palpatine. He is in the command bridge!',
		}

paths = {'north', 'n', 'south', 's', 'east', 'e', 'west', 'w'}

def valid_move(question, allowed):
	choice = None
	final = []
	for p in paths:
		for each in allowed:
			if each == p[0]:
				final.append(p)
	while choice not in allowed:
		choice = input(question)
	return choice



print("Welcome to Star Wars: Save the Chancellor!")
print("In this game your main objective is to save Chancellor Palpatine, who has been captured by the Separatists.\n")
plyrName = input("Enter your epic Jedi name:\n")

print(f"Greetings, {plyrName}! Here is a key to navigate in the game.")
print("KEY: north/n, south/s, east/e, west/w, up, down, flee, fight, use, take, inventory, save, load")
input("Press enter to continue")

print(f"\nHello there, Jedi {plyrName}. We need your help to save Chancellor Palpatine.\nHe has been captured by the Separatists. It is rumored that he was captured by the leader of the droid army, General Grievous.")
input("Press enter to continue")
print("\nPrepare your starfighter and be prepared to board his ship. Good luck! And may the force be with you!")
print("<You start up your starfighter and fly over to the the Separatist Frigate.>")
input("Press enter to continue")

print("\nThere is only one way in, through the hangar.")
pathOption = input("Available paths: north\n")
print()
while pathOption != "north" and pathOption != "n":
	print("Invalid input. You need to use either north/n, south/s, east/e, or west/w.")
	print("\nThere is only one way in, through the hangar.")
	pathOption = input("Available paths: north\n")
if pathOption == "north" or "n":
	print("You swoop into the hangar and quickly exit your ship.\nSuddenly, a large group of Separatist battle droids are surrounding you. They have been awaiting your arrival.")
	fleeOrfight = input("Do you flee or fight?:\n")
	while fleeOrfight != "fight":
		print("\nInvalid input. Are you going to FLEE or FIGHT?")
		fleeOrfight = input("Do you flee or fight?:\n")
		if fleeOrfight == "flee":
			print("\nYou try to flee, the battle droids instantly shoot you down.")
			print(diedEnd)
			input("\nPress enter to restart.\n")
			print("You swoop into the hangar and quickly exit your ship.\nSuddenly, a large group of Separatist battle droids are surrounding you. They have been awaiting your arrival.")
			fleeOrfight = input("Do you flee or fight?:\n")
	if fleeOrfight == "fight":
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
			input("Press enter to continue")

print("\nNow that you've taken down those clankers, you must locate where the Chancellor is.")
print("Good thing you have your trusty astromech droid to help!")
print("But first your droid needs a port to plug into.")
print(rooms['Hangar'])
hangarOption = input("Available paths: north, east\n")

palpsLocation = False
while hangarOption not in paths:
	try:
		hangarOption = valid_move("Available paths: north, east\n", "ne")
	except:
		print("Invalid input. You need to use either north/n, south/s, east/e, or west/w.")
		hangarOption = valid_move("Available paths: north, east\n", "ne")
	else:
		print("\nYou spot a hallway and a door. Find a port for your droid.")


hangarOption = input("Available paths: north, east\n")
if hangarOption == "north" or "n":
	print("\nYou go through the hallway. At the end of the hallway, there are elevators.")
	print("Looks like you need a droid to operate the elevators.")
	useDroid = input("Use droid?:\n")
if useDroid and palpsLocation == False:
	print("\nYou need to find the location of Chancellor Palpatine first.")
	option = input("Available paths: south\n")
while option != "south" and "s":
	if option == "south" or "s":
		print("\nYou head back to the hangar.")
		print("You spot a hallway and a door. Find a port for your droid.")
		option = input("Avaiable paths: north, east")
