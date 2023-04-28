#Dark Souls
#first description
def main():
	print("""
	
▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀     ██████  ▒█████   █    ██  ██▓      ██████ 
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒    ▒██    ▒ ▒██▒  ██▒ ██  ▓██▒▓██▒    ▒██    ▒ 
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░    ░ ▓██▄   ▒██░  ██▒▓██  ▒██░▒██░    ░ ▓██▄   
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄      ▒   ██▒▒██   ██░▓▓█  ░██░▒██░      ▒   ██▒
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄   ▒██████▒▒░ ████▓▒░▒▒█████▓ ░██████▒▒██████▒▒
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒   ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░   ░ ░▒  ░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░ ▒  ░░ ░▒  ░ ░
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░    ░  ░  ░  ░ ░ ░ ▒   ░░░ ░ ░   ░ ░   ░  ░  ░  
   ░          ░  ░   ░     ░  ░            ░      ░ ░     ░         ░  ░      ░  
 ░                                                                               

	""")
	inventory = ["Leather_armour", "Iron_Sword"]
	chest1 = ["Black_Iron_Sword"]
	chest2 = ["Grass_Crest_Shield"]
	chest3 = ["Fine_Iron_Armour"]
	q = ""
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
	elevator_postition = 1
	ending = False
	ending1 = False
	ending2 = False
	bonfire_respawn_positioning = ""
	#laying out print variables labled by their height, then distance based on the amount of rooms after the first platform
	platform111 = ("You wake up on a small platform of complex tiles with guard rails made of marble on all sides except north. The world is a yellow-ish red color and the sun is blaring on you. In the distance there is a forrest full of fall leaves and to the north-west you see a large catherdral of red stone. You are wearing blackened leather armour, but you can tell it won't last long.")
	platform212 = ("You head towards the north and see a staircase going downwards and to the left hanging along the side of a building made of the same red stone. When you reach the bottom of the staircase you see a giant Knight dressed in black iron armour. The walkway ends where the Knight is standing and there is a door to the south that leads into a room.")
	platform211 = ("The building is tall and has arches for doorways. Inside the room you see a pair of the giant Knights across the room from each other. There is a chest that the two are gaurding. To the West you see an exit to the building")
	platform222 = ("You exit the building and step out to another open platform, this one much larger than the last. To the south there is a doorway leading into a building. To the north there is a round building that appears to lead downwards.")
	platform221 = ("You go down the stairs and see a \x1B[3mbonfire\x1B[0m and, leaning against a wall opposite you, you see a \x1B[3mFirebearer\x1B[0m")
	platform223 = ("You go to the round building and see that when you step inside there is an elevator that leads downwards.")
	platform311 = ("There is a curved stairway that leads you to a stone walkway. There are small, spiked gaurd rails lining the path to the elevator that only go up to your ankles. You can see a small ledge around the round elevator entrance and you can see another elecator to the north. To the west there are buttresses that lead to another building with multiple levels inside.")
	platform310 = ("You walk around the edge of the rounded elevator walls and you find a \x1B[3chest\x1B[0m")
	platform312 = ("You find a missing link in the small gaurd rails that allows you to climb the buttress. When you reach the top there is a broken window")
	platform231 = ("You step into the building and find that there are wooden rafters leading to a chandelier. The building is made of a white marble. When you reach the end of the rafters there are stairs that lead down to the east.")
	platform232 = ("While walking along the butresses you encounter the chandelier. The chain holding onto the chandelier looks brittle. To the north you can see the exit.")
	platform233 = ("You step out off the rafters and see a \x1B[3lever\x1B[0m to the north.")
	platform224 = ("You step onto the large elevator and see that there is a spiral staircase leading down. There is the door to the west leading into the marbel room rafters, and there is a path leading south.")
	platform411 = ("You reach the bottom floor of the elevator and pathway leading north and a pathway leading to the marble building bottom floor")
	platform333 = ("You go into the bottom floor of the building and there are many soldiers in white robes standing around the room. They all have throwing knives at the ready to protect something.")
	platform412 = ("The pathway leads to an open door and you can see something inside.")
	platform413 = ("There is a dark room with a bonfire in the center")
	platform314 = ("You are on a pathway with a \x1B[3lever\x1B[0m. You can see the other path you were on before to the south.")
	platform225 = ("You walk onto another pathway going north. There are steps going upward towards the large cathedral. To the left of you there is a \x1B[3lever\x1B[0m")
	platform121 = ("There are another two large black knights to your left and right. to the north the large door to the cathedral.") 
	platform122 = ("When you walk into the cathedral it is lit by candle light. There are large cloumns leading up to the ceilings that are about forty feet tall. The walls are made of red stone and marble. To the north you can see large staircases to either side.")
	platform021 = ("When you walk up the stairs you see a magnificent lancet stained glass window. One panel of the window is shattered.")
	platform020 = ("You found a chest while walking just outside the lancet window")
	platform122 = ("You step into the fog and see steps leading upwards. When you walk up you see two fighters: Dragon Slayer Ornstein and Executioner Smough. They are standing at the back of a battle worn area and the columns holding up this ceiling are close to crumbling.")
	platform123 = ("When you get the final slash on the two great foes a fog behind where they were first seen disapears, leading to a staircase.")
	platform000 = ("You walk up the stairs and see the Princess of Sunlight, Gwindolyn. She thanks you for ending the terror that ornstein and smough have caused and gives you a piece to teleport you back home.")

	player_position = platform111
	print(f"{player_position}")
	player_input = ""
	while player_input != "q":
		player_input = input("What do you do?\n").lower()

		if player_input == "north" and player_position == platform111:
			player_position = platform212
			print(f"{player_position}")
		else:
			print("That is not a direction or action you can do.")

		if player_input == "south" and player_position == platform212:
			player_position = platform211
			print(f"{player_position}")
		elif player_input == "north" and player_position == platform212:
			player_position = platform111
			print(f"{player_position}")
		else:
			print("That is not a direction or action you can do.")

	
	
if __name__ == "__main__":
	main()