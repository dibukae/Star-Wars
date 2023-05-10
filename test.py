#def valid_move(question, allowed):
#	choice = None
#	final = []
#	for p in paths:
#		for each in allowed:
#			if each == p[0]:
#				final.append(p)
#	while choice not in allowed:
#		choice = input(question)
#	return choice
#
#	while hangarOption not in paths:
#	try:
#		hangarOption = valid_move("Available paths: north, east\n", "ne")
#	except:
#		print(error_msg)
#		hangarOption = valid_move("Available paths: north, east\n", "ne")
#	else:
#		print("\nYou spot a hallway and a door. Find a port for your droid.")


def fight_t(taken):
	defeatedDroids = 0
	if taken == True:
		print(use_inv())
			while defeatedDroids != 2:
				print("\nYou chuck a droid popper at one of the droidekas. It rolls into its shield.")
				print("The droideka is instantly taken out!")
				defeatedDroids += 1
				input("Press enter to continue")
			if defeatedDroids == 2:
				print("\nYou defeated all the droidekas!")