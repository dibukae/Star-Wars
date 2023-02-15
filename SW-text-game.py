diedEnd = "You died and failed to save the chancellor..."

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
		print("You try to flee, the battle droids instantly shoot you down.")
		print(diedEnd)