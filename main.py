#Dark Souls
#first description
def main():
	print("Before playing, make sure the terminal is full screen and cleared\n")
	print("""

▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀     ██████  ▒█████   █    ██  ██▓      ██████    ▄▄▄█████▓▓█████ ▒██   ██▒▄▄▄█████▓   ▓█████ ▓█████▄  ██▓▄▄▄█████▓ ██▓ ▒█████   ███▄    █ 
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒    ▒██    ▒ ▒██▒  ██▒ ██  ▓██▒▓██▒    ▒██    ▒    ▓  ██▒ ▓▒▓█   ▀ ▒▒ █ █ ▒░▓  ██▒ ▓▒   ▓█   ▀ ▒██▀ ██▌▓██▒▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ 
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░    ░ ▓██▄   ▒██░  ██▒▓██  ▒██░▒██░    ░ ▓██▄      ▒ ▓██░ ▒░▒███   ░░  █   ░▒ ▓██░ ▒░   ▒███   ░██   █▌▒██▒▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄      ▒   ██▒▒██   ██░▓▓█  ░██░▒██░      ▒   ██▒   ░ ▓██▓ ░ ▒▓█  ▄  ░ █ █ ▒ ░ ▓██▓ ░    ▒▓█  ▄ ░▓█▄   ▌░██░░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄   ▒██████▒▒░ ████▓▒░▒▒█████▓ ░██████▒▒██████▒▒     ▒██▒ ░ ░▒████▒▒██▒ ▒██▒  ▒██▒ ░    ░▒████▒░▒████▓ ░██░  ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒   ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░     ▒ ░░   ░░ ▒░ ░▒▒ ░ ░▓ ░  ▒ ░░      ░░ ▒░ ░ ▒▒▓  ▒ ░▓    ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░   ░ ░▒  ░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░ ▒  ░░ ░▒  ░ ░       ░     ░ ░  ░░░   ░▒ ░    ░        ░ ░  ░ ░ ▒  ▒  ▒ ░    ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░    ░  ░  ░  ░ ░ ░ ▒   ░░░ ░ ░   ░ ░   ░  ░  ░       ░         ░    ░    ░    ░            ░    ░ ░  ░  ▒ ░  ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ 
   ░          ░  ░   ░     ░  ░            ░      ░ ░     ░         ░  ░      ░                 ░  ░ ░    ░                 ░  ░   ░     ░            ░      ░ ░           ░ 
 ░                                                                                                                               ░                                           

	""")
	#adding in variables
	canLightBonfires = False
	inventory = ["Leather_armour", "Broken_Iron_Sword"]
	chest1 = "Black_Iron_Sword"
	chest2 = "Grass_Crest_Shield"
	chest3 = "Fine_Iron_Armor"
	chest4 = "Undefinable_Thing"
	north = ""
	south = ""
	east = ""
	west = ""
	down = ""
	up = ""
	swing = ""
	bonfire1 = False
	bonfire2 = False
	player_position = ""
	elevator_position = 1
	ending = False
	ending1 = False
	ending2 = False
	ending3 = False
	chandelierFallen = False
	fakewall = False
	firstspawn = True
	pathlever = False
	BK1 = True
	BK2 = True
	BK3 = True
	BK4 = True
	BK5 = True
	bosses = True
	robedguys = True
	secret = False
	bonfire_save = 0
	#laying out print variables labled by their height, then distance based on the amount of rooms after the first platform
	platform111 = ("You wake up on a small platform of complex tiles with guard rails made of marble on all sides except north. The world is a yellow-ish red color and the sun is blaring on you. In the distance there is a forrest full of fall leaves and to the north-west you see a large catherdral of red stone. You are wearing blackened leather armour, but you can tell it won't last long, and you are holding a broken iron sword")
	platform212 = ("You head towards the north and see a staircase going downwards and to the left hanging along the side of a building made of the same red stone. When you reach the bottom of the staircase you see a giant Knight dressed in black iron armour. The walkway ends where the Knight is standing and there is a door to the south that leads into a room.")
	platform211 = ("The building is tall and has arches for doorways. Inside the room you see a pair of the giant Knights across the room from each other. There is a \x1B[3mchest\x1B[0m that the two are gaurding. To the West you see an exit to the building")
	platform222 = ("You exit the building and step out to another open platform, this one much larger than the last. To the south there is a doorway leading into a building. To the north there is a round building that appears to lead downwards. To the east is the covered building")
	platform221 = ("You go down the stairs and see a \033[1;31;40m\x1B[3mbonfire\x1B[0m and, leaning against a wall opposite you, you see a \033[1;31;40m\x1B[3mFirebearer\x1B[0m")
	platform223 = ("You go to the round building and see that when you step inside there is an elevator that leads downwards.")
	platform310s = ("You step inside the building and there is an elevator that goes up after curved stairways lead to the elevator floor, to the north is an exit.")
	platform311 = ("There is a curved stairway that leads you to a stone walkway. There are small, spiked gaurd rails lining the path to the elevator that only go up to your ankles. You can see a small ledge around the round elevator entrance and you can see another elevator to the north. To the west there are buttresses that lead to another building with multiple levels inside.")
	platform310 = ("You walk around the edge of the rounded elevator walls and you find a \x1B[3mchest\x1B[0m")
	platform312 = ("You find a missing link in the small gaurd rails that allows you to climb the buttress. When you reach the top there is a broken window to the west")
	platform231 = ("You step into the building and find that there are wooden rafters leading to a chandelier to the north. The building is made of a white marble.")
	platform232 = ("While walking along the butresses you encounter the chandelier. The chain holding onto the chandelier looks brittle. To the north you can see the exit.")
	platform233 = ("You step out off the rafters and see a \x1B[3mlever\x1B[0m at the exit.")
	platform224 = ("You step onto the large elevator and see that there is a spiral staircase leading down. There is the door to the west leading into the marbel room rafters, and there is a path leading south.")
	platform411 = ("You reach the bottom floor of the elevator and pathway leading north and a pathway leading to the marble building bottom floor")
	platform333 = ("You go into the bottom floor of the building and there are many soldiers in white robes standing around the room. They all have throwing knives at the ready to protect something.")
	platform323 = ("You walk to where the chandelier is and find many soldiers ")
	platform321 = ("You see a \x1B[3mchest\x1B[0m in the corner of the room.")
	platform412 = ("The pathway leads to a dead end with a wall in front of you.")
	platform413 = ("There is a dark room with a bonfire in the center")
	platform314 = ("You are on a pathway with a \x1B[3mlever\x1B[0m. You can see the other path you were on before to the south.")
	platform225 = ("You walk onto the pathway going north. There are steps going upward towards the large cathedral. To the left of you there is a \x1B[3mlever\x1B[0m")
	platform121 = ("There are another two large black knights to your left and right. To the north, the large door to the cathedral.") 
	platform122 = ("When you walk into the cathedral it is lit by candle light. There are large cloumns leading up to the ceilings that are about forty feet tall. The walls are made of red stone and marble. To the north you can see large staircases to either side.")
	platform021 = ("When you walk up the stairs you see a magnificent lancet stained glass window. One panel of the window is shattered.")
	platform020 = ("You found a chest while walking just outside the lancet window")
	platform122 = ("You step into the fog and see steps leading upwards. When you walk up you see two fighters: Dragon Slayer Ornstein and Executioner Smough. They are standing at the back of a battle worn area and the columns holding up this ceiling are close to crumbling.")
	platform123 = ("A fog behind where they were first seen disapears, leading to a staircase to the north.")
	platform000 = ("You walk up the stairs and see the Princess of Sunlight, Gwindolyn. She thanks you for ending the terror that ornstein and smough have caused and gives you a piece to teleport you back home.")
#STARING GAME MATERIAL
	player_name = input("What is your name?\n")
	player_position = platform111
	player_input = ""
	print(f"{player_position}")
	print("Please use the full name or direction you want to go or do.")
	while "q" not in player_input:
		player_input = input("What do you do?\n").lower()

		if player_input == "north" and player_position == platform111:
			player_position = platform212
			print(f"{player_position}")
			firstspawn = False
		elif player_input == "swing" and player_position == platform212 and chest1 in inventory and BK1 == True:
			print("You swing and kill the Black Knight.")
			BK1 = False
			player_position = platform212
		elif player_input == "present" and player_position == platform111 and chest4 in inventory and ending1 == True and ending2 == True and ending3 == True:
			print("You present the undifinable object to the sun and it turns to a doll then disappears.")
			secret == True
		elif player_input == "swing" and player_position == platform212 and chest1 not in inventory and BK1 == True:
			print("You swing but the Black knight kills you.")
			print("""
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ 
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    
 ░ ░                           ░                  ░      """)
			if bonfire_save == 1:
				player_position = platform221
				print("You wake up in the room with the \x1B[3mFirebearer\x1B[0m.")
			elif bonfire_save == 2:
				player_position = platform413
				print("You wake up in the dark room with the bonfire.")
			else:
				player_position = platform111
				print("You wake up on the platform of complex tiles.")
		elif player_input == "open" and player_position == platform211 and BK2 == False and BK3 == False:
			print("You open the chest and find the \x1B[3mGrass Crest Shield\x1B[0m")
			inventory.append(chest2)
		elif player_input == "north" and player_position == platform211 and BK1 == False:
			player_position == platform212
			print("There is a path to the east leading to the complex tiled platform, and there is a building to the south with a tall arched doorway.")
		elif player_input == "south" and player_position == platform212:
			player_position = platform211
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform212 and BK2 == False and BK3 == False:
			player_position = platform211
			print("There is an exit to the north and west.")
		elif player_input == east and player_position == platform222 and BK2 == False and BK3 == False:
			player_position = platform211
			print("There is an exit to the north and west.")
		elif player_input == "north" and player_position == platform211:
			player_position = platform212
			print(f"{player_position}")
		elif player_input == "swing" and player_position == platform211 and chest1 in inventory and BK2 == True and BK3 == True:
			print("You swing and kill the two black knights.")
			BK2 = False
			BK3 = False
			player_position = platform211
		elif player_input == "swing" and player_position == platform211 and chest1 not in inventory and BK2 == True and BK3 == True:
			print("You swing but the Black Knights kill you.")
			print("""
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ 
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    
 ░ ░                           ░                  ░      """)
			if bonfire_save == 1:
				player_position = platform221
				print("You wake up in the room with the \x1B[3mFirebearer\x1B[0m")
			elif bonfire_save == 2:
				player_position = platform413
				print("You wake up in the dark room with the bonfire.")
			else:
				player_position = platform111
				print("You wake up on the platform of complex tiles.")
		elif player_input == "open" and player_position == platform211 and chest1 not in inventory and BK2 == True and BK3 == True:
			print("You go to open the chest but the Black Knights kill you.")
			print("""
			
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ 
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    
 ░ ░                           ░                  ░      
			""")
			if bonfire_save == 1:
				player_position = platform221
				print("You wake up in the room with the \x1B[3mFirebearer\x1B[0m")
			elif bonfire_save == 2:
				player_position = platform413
				print("You wake up in the dark room with the bonfire.")
			else:
				player_position = platform111
				print("You wake up on the platform of complex tiles.")
		elif player_input == "open" and player_position == platform211 and chest1 in inventory and BK2 == True and BK3 == True:
			print("You go to open the chest but the Black Knights kill you.")
			print("""
			
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ 
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    
 ░ ░                           ░                  ░      
			""")
			if bonfire_save == 1:
				player_position = platform221
				print("You wake up in the room with the \x1B[3mFirebearer\x1B[0m")
			elif bonfire_save == 2:
				player_position = platform413
				print("You wake up in the dark room with the bonfire.")
			else:
				player_position = platform111
				print("You wake up on the platform of complex tiles.")
		elif player_input == "east" and player_position == platform212 and firstspawn == False:
			player_position = platform111
			print(f"You walk up to the platform, The only place to go is north. The sun is blaring on you.")
		elif player_input == "west" and player_position == platform211:
			player_position = platform222
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform222:
			player_position = platform221
			print(f"{player_position}")
		elif player_input == "talk" and player_position == platform221:
			print(f"You are that chosen undead everyone is talking about, what was the name they were calling you, {player_name.title()}, yes? Do you see that \033[1;31;40m\x1B[3mbonfire\x1B[0m over there? you can light them with this and  \033[1;31;40m\x1B[3msave your progress\x1B[0m.")
			canLightBonfires = True
		elif player_input == "light" and player_position == platform221 and canLightBonfires == True:
			print("""
			
▄▄▄▄·        ▐ ▄ ·▄▄▄▪  ▄▄▄  ▄▄▄ .    ▄▄▌  ▪  ▄▄▄▄▄
▐█ ▀█▪▪     •█▌▐█▐▄▄·██ ▀▄ █·▀▄.▀·    ██•  ██ •██  
▐█▀▀█▄ ▄█▀▄ ▐█▐▐▌██▪ ▐█·▐▀▀▄ ▐▀▀▪▄    ██▪  ▐█· ▐█.▪
██▄▪▐█▐█▌.▐▌██▐█▌██▌.▐█▌▐█•█▌▐█▄▄▌    ▐█▌▐▌▐█▌ ▐█▌·
·▀▀▀▀  ▀█▄▀▪▀▀ █▪▀▀▀ ▀▀▀.▀  ▀ ▀▀▀     .▀▀▀ ▀▀▀ ▀▀▀ 

			""")
			bonfire1 = True
		elif player_input == "save" and player_position == platform221:
			print("Position saved.")
			bonfire_save = 1
		elif player_input == "north" and player_position == platform221:
			player_position = platform222
			print(f"{player_position}")
		elif player_input == "east" and player_position == platform222:
			player_position = platform211
			print(f"{player_position}")
		elif player_input == "north" and player_position == platform222:
			player_position = platform223
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform223:
			player_position = platform222
			print(f"{player_position}")
		elif player_input == "down" and player_position == platform223:
			player_position = platform310s
			print(f"{player_position}")
		elif player_input == "up" and player_position == platform310s:
			player_position = platform223
			print(f"{player_position}")
		elif player_input == "north" and player_position == platform310s:
			player_position = platform311
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform311:
			player_position = platform310s
			print(f"{player_position}")
		elif player_input == "east" and player_position == platform311:
			player_position = platform310
			print(f"{player_position}")
		elif player_input == "open" and player_position == platform310 and chest1 not in inventory:
			print("You open the \x1B[3mchest\x1B[0m and you find a \x1B[3mBlack Iron Sword\x1B[0m")
			inventory.append(chest1)
		elif player_input == "west" and player_position == platform310:
			player_position = platform311
			print(f"{player_position}")
		elif player_input == "west" and player_position == platform311:
			player_position = platform312
			print(f"{player_position}")
		elif player_input == "west" and player_position == platform312:
			player_position = platform231
			print(f"{player_position}")
		elif player_input == "north" and player_position == platform231:
			player_position = platform232
			print(f"{player_position}")
		elif player_input == "east" and player_position == platform312:
			player_position = platform311
			print(f"{player_position}")
		elif player_input == "east" and player_position == platform231:
			player_position = platform312
			print(f"{player_position}")
		elif player_input == "swing" and player_position == platform232 and chest1 in inventory:
			print(f"You swing and hit the brittle chain holding the chandelier, and it drops to the gorund crushing many foes beneath it.")
			chandelierFallen = True
		elif player_input == "swing" and player_position == platform232 and chest1 not in inventory:
			print("You reach out to swing for the chandelier but the broken sword is not long enough and you fall to the floor killing yourself.")
			print("""
			
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ 
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    
 ░ ░                           ░                  ░      
			""")
			if bonfire_save == 1:
				player_position = platform221
				print("You wake up in the room with the \x1B[3mFirebearer\x1B[0m")
			elif bonfire_save == 2:
				player_position == platform413
				print("You wake up in the dark room with the bonfire.")
			else:
				player_position = platform111
				print("You wake up on the platform of complex tiles.")
		elif player_input == "north" and player_position == platform232:
			player_position = platform233
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform233:
			player_position = platform232
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform232:
			player_position = platform231
			print(f"{player_position}")
		#elevator positioning
		elif player_input == "pull" and elevator_position == 1 and player_position == platform233:
			elevator_position = 2
		elif player_input == "pull" and elevator_position == 2 and player_position == platform233:
			elevator_position = 1
		elif player_input == "pull" and elevator_position == 1 and player_position == platform224:
			elevator_position == 2
		elif player_input == "pull" and elevator_position == 2 and player_position == platform224:
			elevator_position == 1
		elif player_input == "east" and player_position == platform233:
			player_position = platform224
			print(f"{player_position}")
		elif player_input == "down" and player_position == platform224:
			player_position = platform411
			print(f"{player_position}")
		elif player_input == "up" and player_position == platform411:
			player_position = platform224
			print(f"{player_position}")
			#make sure that the player cannot see the fog wall before and can after swinging
		elif player_input == "north" and player_position == platform411 and fakewall == True:
			print("You can see an arched doorway to the north.")
			player_position = platform412
		elif player_input == "north" and player_position == platform411 and fakewall == False:
			print("The pathway leads to a dead end.")
			player_position = platform412
		elif player_input == "south" and player_position == platform412:
			player_position = platform411
			print(f"{player_position}")
		elif player_input == "swing" and player_position == platform412 and chest1 in inventory:
			print("You swing at the wall and the wall turns to fog and disappears, an arched door is left in its place")
			fakewall = True
		elif player_input == "north" and player_position == platform412:
			player_position = platform413
			print(f"{player_position}")
		elif player_input == "light" and player_position == platform413 and canLightBonfires == True:
			print("""
			
▄▄▄▄·        ▐ ▄ ·▄▄▄▪  ▄▄▄  ▄▄▄ .    ▄▄▌  ▪  ▄▄▄▄▄
▐█ ▀█▪▪     •█▌▐█▐▄▄·██ ▀▄ █·▀▄.▀·    ██•  ██ •██  
▐█▀▀█▄ ▄█▀▄ ▐█▐▐▌██▪ ▐█·▐▀▀▄ ▐▀▀▪▄    ██▪  ▐█· ▐█.▪
██▄▪▐█▐█▌.▐▌██▐█▌██▌.▐█▌▐█•█▌▐█▄▄▌    ▐█▌▐▌▐█▌ ▐█▌·
·▀▀▀▀  ▀█▄▀▪▀▀ █▪▀▀▀ ▀▀▀.▀  ▀ ▀▀▀     .▀▀▀ ▀▀▀ ▀▀▀ 

			""")
		elif player_input == "save" and player_position == platform413:
			bonfire_save = 0
			print("Position saved")
		elif player_input == "south" and player_position == platform413:
			player_position = platform412
			print(f"{player_position}")
		elif player_input == "west" and player_position == platform411:
			player_position = platform333
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform333:
			player_position = platform323
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform323 and robedguys == False:
			player_position = platform321
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform323 and robedguys == True:
			print("You try to get by the soldiers but there are too many and they stab you to death.")
			print("""
			
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ 
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    
 ░ ░                           ░                  ░      
			""")
			if bonfire_save == 1:
				player_position = platform221
				print("You wake up in the room with the \x1B[3mFirebearer\x1B[0m")
			elif bonfire_save == 2:
				player_position == platform413
				print("You wake up in the dark room with the bonfire.")
			else:
				player_position = platform111
				print("You wake up on the platform of complex tiles.")
		elif player_input == "swing" and player_position == platform323 and chandelierFallen == True:
			print("You killed enought of the robed soldiers in order to kill the rest.")
			robedguys = False
		elif player_input == "swing" and player_position == platform323 and chandelierFallen == False:
			print("You get overun by robed soldiers and get stabbed to death.")
			print("""
			
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ 
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    
 ░ ░                           ░                  ░      
			""")
			if bonfire_save == 1:
				player_position = platform221
				print("You wake up in the room with the \x1B[3mFirebearer\x1B[0m")
			elif bonfire_save == 2:
				player_position == platform413
				print("You wake up in the dark room with the bonfire.")
			else:
				player_position = platform111
				print("You wake up on the platform of complex tiles.")
		elif player_input == "open" and player_position == platform321 and robedguys == False:
			print(f"you open the chest and find something, but you can't tell what it is.")
			inventory.append(chest4)
		elif player_input == "north" and player_position == platform321:
			player_position = platform322
			print(f"{player_position}")
		elif player_input == "north" and player_position == platform323:
			player_position = platform333
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform224:
			player_position = platform314
			print(f"{player_position}")
		elif player_input == "pull" and player_position == platform314:
			pathlever = True
			print("you pull the lever and see a path being extended from your feet to where you were before the marble building.")
		elif player_input == "south" and player_position == platform314 and pathlever == True:
			player_position = platform311
			print(f"{player_position}")
		elif player_input == "north" and player_position == platform311 and pathlever == True:
			player_position = platform314
			print(f"{player_position}")
		elif player_input == "north" and player_position == platform411 and elevator_position == 2:
			player_position = platform225
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform225 and elevator_position == 2:
			player_position = platform411
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform121:
			player_position = platform225
			print(f"{player_position}")
		elif player_input == "pull" and player_position == platform225 and elevator_position == 2:
			print("You pull the lever and the elevator drops.")
		elif player_input == "pull" and player_position == platform225 and elevator_position == 1:
			print("You pull the lever and the elevator rises up.")
		elif player_input == "north" and player_position == platform225:
			player_position = platform121
			print(f"{player_position}")
		elif player_input == "swing" and player_position == platform121 and chest1 in invetory and BK4 == True and BK5 == True:
			print("You swing and kill the Black Knights to your left and right.")
			BK4 == False
			BK5 == False
		elif player_input == "north" and player_position == platform121:
			player_position = platform122
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform122:
			player_position = platform121
			print(f"{player_position}")
		elif player_input == "west" and player_position == platform121:
			player_position = platform021
			print(f"{player_position}")
		elif player_input == "east" and player_position == platform121:
			player_position = platform021
			print(f"{player_position}")
		elif player_input == "west" and player_position == platform021:
			player_position = platform121
			print(f"{player_position}")
		elif player_input == "east" and player_position == platform021:
			player_position = platform121
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform021:
			player_position = platform020
			print(f"{player_position}")
		elif player_input == "open" and player_position == platform020:
			print("You open the chest and find Fine Iron Armor")
			inventory.append(chest3)
		elif player_input == "north" and player_position == platform020:
			player_position = platform021
			print(f"{player_position}")
		elif player_input == "north" and player_position == platform121:
			player_position = platform122
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform122 and bosses == True:
			print("You try to go south but there is now a fog wall covering the way. While trying to exit you get crushed by Ornstein")
			print("""
			
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ 
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    
 ░ ░                           ░                  ░      
			""")
			if bonfire_save == 1:
				player_position = platform221
				print("You wake up in the room with the \x1B[3mFirebearer\x1B[0m")
			elif bonfire_save == 2:
				player_position == platform413
				print("You wake up in the dark room with the bonfire.")
			else:
				player_position = platform111
				print("You wake up on the platform of complex tiles.")
		elif player_input == "swing" and player_position == platform122 and chest1 in inventory and chest2 in inventory and chest3 in inventory:
			print("You swing at the crumbling column and it falls and crushes Smough, you swing for a second time and kill Ornstein")
			bosses = False
		elif player_input == "swing" and player_position == platform122:
			if chest1 not in inventory or chest2 not in inventory or chest3 not in inventory:
				print("You go to swing at Ornstein and Smough but you were not prepared enough to meet them.")
				print("""
			
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ 
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    
 ░ ░                           ░                  ░      
				""")
				if bonfire_save == 1:
					player_position = platform221
					print("You wake up in the room with the \x1B[3mFirebearer\x1B[0m")
				elif bonfire_save == 2:
					player_position == platform413
					print("You wake up in the dark room with the bonfire.")
				else:
					player_position = platform111
					print("You wake up on the platform of complex tiles.")
		elif player_input == "north" and player_position == platform122 and bosses == False:
			player_position = platform123
			print(f"{player_position}")
		elif player_input == "south" and player_position == platform122 and bosses == False:
			player_position = platform121
			print("You are standing in a broken battlefield.")
		elif player_input == "north" and player_position == platform121 and bosses == False:
			player_position = platform122
			print("You are standing in a broken battlefield.")
		elif player_input == "north" and player_position == platform123:
			player_position == platform000
			print(f"{player_position}")
			if BK1 == False and Bk2 == False and BK3 == False and BK4 == False and BK5 == False and robedguys == False and chandelierFallen == True and pathlever == True and canLightBonfires == True and bonfire1 == True and bonfire2 == True and secret == True:
				ending3 = True
				ending = True
			elif BK1 == False and Bk2 == False and BK3 == False and BK4 == False and BK5 == False and robedguys == False and chandelierFallen == True and pathlever == True and canLightBonfires == True and bonfire1 == True and bonfire2 == True:
				ending2 = True
				ending = True
			else:
				ending1 = True
				ending = True
		elif player_input == "inventory":
			print(inventory)
		else:
			if "q" in player_input:
				print("You quit the game")
			elif ending == True:
				print("""
				
 ▄████▄   ▒█████   ███▄    █   ▄████  ██▀███   ▄▄▄     ▄▄▄█████▓ █    ██  ██▓    ▄▄▄     ▄▄▄█████▓ ██▓ ▒█████   ███▄    █   ██████    ▓██   ██▓ ▒█████   █    ██     ▄▄▄▄   ▓█████ ▄▄▄     ▄▄▄█████▓
▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █  ██▒ ▀█▒▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒ ██  ▓██▒▓██▒   ▒████▄   ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ ▒██    ▒     ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓█████▄ ▓█   ▀▒████▄   ▓  ██▒ ▓▒
▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▓██  ▒██░▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒░ ▓██▄        ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██▒ ▄██▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░
▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▓▓█  ░██░▒██░   ░██▄▄▄▄██░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒  ▒   ██▒     ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░█▀  ▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ 
▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ▒▒█████▓ ░██████▒▓█   ▓██▒ ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░▒██████▒▒     ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▓█  ▀█▓░▒████▒▓█   ▓██▒ ▒██▒ ░ 
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░      ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░▒▓███▀▒░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░   
  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░   ░    ░░▒░ ░ ░ ░ ░ ▒  ░ ▒   ▒▒ ░   ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒  ░ ░    ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ▒░▒   ░  ░ ░  ░ ▒   ▒▒ ░   ░    
░        ░ ░ ░ ▒     ░   ░ ░ ░ ░   ░   ░░   ░   ░   ▒    ░       ░░░ ░ ░   ░ ░    ░   ▒    ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ ░  ░  ░      ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░    ░    ░    ░   ▒    ░      
░ ░          ░ ░           ░       ░    ░           ░  ░           ░         ░  ░     ░  ░         ░      ░ ░           ░       ░      ░ ░         ░ ░     ░         ░         ░  ░     ░  ░        
░                                                                                                                                      ░ ░                                ░                         
▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀     ██████  ▒█████   █    ██  ██▓      ██████    ▄▄▄█████▓▓█████ ▒██   ██▒▄▄▄█████▓   ▓█████ ▓█████▄  ██▓▄▄▄█████▓ ██▓ ▒█████   ███▄    █                        
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒    ▒██    ▒ ▒██▒  ██▒ ██  ▓██▒▓██▒    ▒██    ▒    ▓  ██▒ ▓▒▓█   ▀ ▒▒ █ █ ▒░▓  ██▒ ▓▒   ▓█   ▀ ▒██▀ ██▌▓██▒▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █                        
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░    ░ ▓██▄   ▒██░  ██▒▓██  ▒██░▒██░    ░ ▓██▄      ▒ ▓██░ ▒░▒███   ░░  █   ░▒ ▓██░ ▒░   ▒███   ░██   █▌▒██▒▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒                       
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄      ▒   ██▒▒██   ██░▓▓█  ░██░▒██░      ▒   ██▒   ░ ▓██▓ ░ ▒▓█  ▄  ░ █ █ ▒ ░ ▓██▓ ░    ▒▓█  ▄ ░▓█▄   ▌░██░░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒                       
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄   ▒██████▒▒░ ████▓▒░▒▒█████▓ ░██████▒▒██████▒▒     ▒██▒ ░ ░▒████▒▒██▒ ▒██▒  ▒██▒ ░    ░▒████▒░▒████▓ ░██░  ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░                       
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒   ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░     ▒ ░░   ░░ ▒░ ░▒▒ ░ ░▓ ░  ▒ ░░      ░░ ▒░ ░ ▒▒▓  ▒ ░▓    ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒                        
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░   ░ ░▒  ░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░ ▒  ░░ ░▒  ░ ░       ░     ░ ░  ░░░   ░▒ ░    ░        ░ ░  ░ ░ ▒  ▒  ▒ ░    ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░                       
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░    ░  ░  ░  ░ ░ ░ ▒   ░░░ ░ ░   ░ ░   ░  ░  ░       ░         ░    ░    ░    ░            ░    ░ ░  ░  ▒ ░  ░       ▒ ░░ ░ ░ ▒     ░   ░ ░                        
   ░          ░  ░   ░     ░  ░            ░      ░ ░     ░         ░  ░      ░                 ░  ░ ░    ░                 ░  ░   ░     ░            ░      ░ ░           ░                        
 ░                                                                                                                               ░                                                                  

				""")
				if ending1 == True:
					print("You have ending 1")
				if ending2 == True:
					print("You have ending 2")
				if ending3 == True:
					print("You have ending 3")
				if ending1 == True and ending2 == True and ending3 == True:
					print("You have achieved all endings for the game. Thank you for playing.")
				#resetting all variables for another playthorugh except endings.
				canLightBonfires = False
				inventory.remove(chest1, chest2, chest3)
				if chest4 in inventory:
					inventory.remove(chest4)
				bonfire1 = False
				bonfire2 = False
				elevator_position = 1
				chandelierFallen = False
				fakewall = False
				firstspawn = True
				pathlever
				BK1 = True
				BK2 = True
				BK3 = True
				BK4 = True
				BK5 = True
				bosses = True
				robedguys = True
				secret = False
				bonfire_save = 0
				ending = False
			else:
				print("That is not a direction you can go or action you can do.")
				
if __name__ == "__main__":
	main()