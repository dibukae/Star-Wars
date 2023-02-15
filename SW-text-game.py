diedEnd = "You died and failed to save the chancellor..."
goodEnd = "You successfully saved the Chancellor! The Jedi Council promoted you to the rank of Jedi Master! Hooray!"

jediPlyrHP = 35
lightsaberDMG = 5
B1DroidHP = 10
blasterDMG = 2
import random



print("Welcome to Star Wars: Save the Chancellor!")
print("In this game your main objective is to save Chancellor Palpatine, who has been captured by the Separatists.\n")
plyrName = input("Enter your epic Jedi name:\n")

print(f"Greetings, {plyrName}! Here is a key to navigate in the game.")
input("KEY: north/n, south/s, east/e, west/w, up, down, flee, fight, use, take, inventory, save, load\nPress enter to continue.")

input(f"\nHello there, Jedi {plyrName}. We need your help to save Chancellor Palpatine.\nHe has been captured by the Separatists. It is rumored that he was captured by the leader of the droid army, General Grievous.")
print("\nPrepare your starfighter and be prepared to board his ship.")
input("<You start up your starfighter and fly over to the the Separatist Frigate.>")

print("\nThere is only one way in, through the hangar.")
pathOption = input("Available paths: north\n")
print()
if pathOption == "north" or "n":
	print("You swoop into the hangar and quickly exit your ship.\nSuddenly, a large group of Separatist battle droids are surrounding you. They have been awaiting your arrival.")
	fleeOrfight = input("Do you flee or fight?:\n")
	if fleeOrfight == "flee":
		print("\nYou try to flee, the battle droids instantly shoot you down.")
		print(diedEnd)
	elif fleeOrfight == "fight":
		print("\nYou ignite your lightsaber and begin fighting the battle droids.")
		hitMiss = random.randint(1,2)
		while B1DroidHP >= 0:
			print("\nYou deflect several blaster bullets and send them right back to the enemy.")
			B1DroidHP -= lightsaberDMG
			print(B1DroidHP)
			if hitMiss == 2:
				jediPlyrHP -= blasterDMG
				print(f"\nA droid hits you, your HP is now: {jediPlyrHP}")
			elif hitMiss == 1:
				print("\nA droid shoots at you but misses.")
			