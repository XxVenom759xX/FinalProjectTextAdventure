#Dark Souls
import pickle
#adding class
class Bk:
	def __init__(self, talk):
		self.talk = talk

bk1 = Bk("You should turn back.")
bk2 = Bk("We gaurd what you need most.")
bk3 = Bk("We gaurd what you need most.")
bk4 = Bk("Be wise with what you have.")
bk5 = Bk("Lest you might be what you least want.")
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
	death_count = 0
	#laying out print variables labled by their height, then distance based on the amount of rooms after the first platform
	platform111 = ("\nYou wake up on a small platform of complex tiles with guard rails made of marble on all sides except north. The world is a yellow-ish red color and the sun is blaring on you. In the distance there is a forrest full of fall leaves and to the north-west you see a large catherdral of red stone. You are wearing blackened leather armour, but you can tell it won't last long, and you are holding a broken iron sword")
	platform212 = ("\nYou head towards the north and see a staircase going downwards and to the left hanging along the side of a building made of the same red stone. When you reach the bottom of the staircase you see a giant Knight dressed in black iron armour. The walkway ends where the Knight is standing and there is a door to the south that leads into a room.")
	platform211 = ("\nThe building is tall and has arches for doorways. Inside the room you see a pair of the giant Knights across the room from each other. There is a \x1B[3mchest\x1B[0m that the two are gaurding. To the West you see an exit to the building")
	platform222 = ("\nYou exit the building and step out to another open platform, this one much larger than the last. To the south there is a doorway leading into a building. To the north there is a round building that appears to lead downwards. To the east is the covered building")
	platform221 = ("\nYou go down the stairs and see a \033[1;31:0m\x1B[3mbonfire\x1B[0m and, leaning against a wall opposite you, you see a \033[1;31:0m\x1B[3mFirebearer\x1B[0m")
	platform223 = ("\nYou go to the round building and see that when you step inside there is an elevator that leads downwards.")
	platform310s = ("\nYou step inside the building and there is an elevator that goes up after curved stairways lead to the elevator floor, to the north is an exit.")
	platform311 = ("\nThere is a curved stairway that leads you to a stone walkway. There are small, spiked gaurd rails lining the path to the elevator that only go up to your ankles. You can see a small ledge around the round elevator entrance and you can see another elevator to the north. To the west there are buttresses that lead to another building with multiple levels inside.")
	platform310 = ("\nYou walk around the edge of the rounded elevator walls and you find a \x1B[3mchest\x1B[0m")
	platform312 = ("\nYou find a missing link in the small gaurd rails that allows you to climb the buttress. When you reach the top there is a broken window to the west")
	platform231 = ("\nYou step into the building and find that there are wooden rafters leading to a chandelier to the north. The building is made of a white marble.")
	platform232 = ("\nWhile walking along the butresses you encounter the chandelier. The chain holding onto the chandelier looks brittle. To the north you can see the exit.")
	platform233 = ("\nYou step out off the rafters and see a \x1B[3mlever\x1B[0m at the exit.")
	platform224p1 = ("\nYou step onto the large elevator and see that there is a spiral staircase leading down. There is the door to the west leading into the marbel room rafters, and there is a path leading south.")
	platform411p1 = ("\nYou reach the bottom floor of the elevator and there is a pathway leading north and a pathway leading to the marble building bottom floor. There is a staircase leading upwards.")
	platform224p2 = ("\nYou can see a path to the north.")
	platform411p2 = ("\nYou can see a path the the west that leads to the marble room rafters. To the south there is a path leading back the way you were at the first elevator.")
	platform333 = ("\nYou go into the bottom floor of the building and there are many soldiers in white robes standing around the room. They all have throwing knives at the ready to protect something.")
	platform323 = ("\nYou walk to where the chandelier is and find many soldiers ")
	platform321 = ("\nYou see a \x1B[3mchest\x1B[0m in the corner of the room.")
	platform412 = ("\nThe pathway leads to a dead end with a wall in front of you.")
	platform413 = ("\nThere is a dark room with a bonfire in the center")
	platform314 = ("\nYou are on a pathway with a \x1B[3mlever\x1B[0m. You can see the other path you were on before to the south.")
	platform225 = ("\nYou walk onto the pathway going north. There are steps going upward towards the large cathedral. To the left of you there is a \x1B[3mlever\x1B[0m")
	platform121 = ("\nThere are another two large black knights to your left and right. To the north, the large door to the cathedral.") 
	platform122 = ("\nWhen you walk into the cathedral it is lit by candle light. There are large cloumns leading up to the ceilings that are about forty feet tall. The walls are made of red stone and marble. To the north you can see large staircases to either side.")
	platform021 = ("\nWhen you walk up the stairs you see a magnificent lancet stained glass window. One panel of the window is shattered.")
	platform020 = ("\nYou found a chest while walking just outside the lancet window")
	platform123 = ("\nYou step into the fog and see steps leading upwards. When you walk up you see two fighters: Dragon Slayer Ornstein and Executioner Smough. They are standing at the back of a battle worn area and the columns holding up this ceiling are close to crumbling.")
	platform124 = ("\nA fog behind where they were first seen disapears, leading to a staircase to the north.")
	platform000 = ("\nYou walk up the stairs and see the Princess of Sunlight, Gwindolyn. She thanks you for ending the terror that ornstein and smough have caused and gives you a piece to teleport you back home.")
#STARING GAME MATERIAL

	player_name = input("What is your name?\n")
	player_position = platform111
	player_input = ""
	print("Please use the full name or direction you want to go or do.")
	print(f"{player_position}")
	while "q" not in player_input:
		player_input = input("What do you do?\n").lower()
#adding in controls print
		if player_input == "controls":
			print("""
possible inputs:
	controls
	inventory
	deathcount
	swing
	open
	talk
	light
	save
	load
directions:
	north
	south
	east
	west
	up
	down
			""")
		elif player_input == "north" and player_position == platform111:
			player_position = platform212
			print(f"{player_position}")
			firstspawn = False
		elif player_input == "deathcount":
			print(f"{death_count}")

		elif player_input == "swing" and player_position == platform212 and chest1 in inventory and BK1 == True:
			print("\nYou swing and kill the Black Knight.")
			BK1 = False
			player_position = platform212
		
		elif player_input == "present" and player_position == platform111 and chest4 in inventory and ending1 == True and ending2 == True and ending3 == True:
			print("\nYou present the undifinable object to the sun and it turns to a doll then disappears.")
			secret == True
		
		elif player_input == "talk" and player_position == platform212 and BK1:
			print("\n")
			print(bk1.talk)
		
		elif player_input == "swing" and player_position == platform212 and chest1 not in inventory and BK1 == True:
			print("\nYou swing but the Black knight kills you.")
			death_count = death_count + 1
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
			print("\nYou open the chest and find the \x1B[3mGrass Crest Shield\x1B[0m")
			inventory.append(chest2)

		elif player_input == "talk" and player_position == platform211 and BK2 == True and BK3 == True:
			print("\n")
			print(bk2.talk)
			print(bk3.talk)

		elif player_input == "north" and player_position == platform211 and BK1 == False:
			player_position == platform212
			print("\nThere is a path to the east leading to the complex tiled platform, and there is a building to the south with a tall arched doorway.")
		
		elif player_input == "south" and player_position == platform212:
			player_position = platform211
			print(f"{player_position}")
		
		elif player_input == "south" and player_position == platform212 and BK2 == False and BK3 == False:
			player_position = platform211
			print("\nThere is an exit to the north and west.")
		
		elif player_input == "east" and player_position == platform222 and BK2 == False and BK3 == False:
			player_position = platform211
			print("\nThere is an exit to the north and west.")
		
		elif player_input == "north" and player_position == platform211:
			player_position = platform212
			print(f"{player_position}")
		
		elif player_input == "swing" and player_position == platform211 and chest1 in inventory and BK2 == True and BK3 == True:
			print("\nYou swing and kill the two black knights.")
			BK2 = False
			BK3 = False
			player_position = platform211
		
		elif player_input == "swing" and player_position == platform211 and chest1 not in inventory and BK2 == True and BK3 == True:
			print("\nYou swing but the Black Knights kill you.")
			death_count = death_count + 1
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
			death_count = death_count + 1
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
				print("nYou wake up in the room with the \x1B[3mFirebearer\x1B[0m")
			elif bonfire_save == 2:
				player_position = platform413
				print("You wake up in the dark room with the bonfire.")
			else:
				player_position = platform111
				print("You wake up on the platform of complex tiles.")
		
		elif player_input == "open" and player_position == platform211 and chest1 in inventory and BK2 == True and BK3 == True:
			print("\nYou go to open the chest but the Black Knights kill you while you back is turned.")
			death_count = death_count + 1
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
			print(f"\nYou walk up to the platform, The only place to go is north. The sun is blaring on you.")
		
		elif player_input == "west" and player_position == platform211:
			player_position = platform222
			print(f"{player_position}")
		
		elif player_input == "south" and player_position == platform222:
			player_position = platform221
			print(f"{player_position}")
		
		elif player_input == "talk" and player_position == platform221:
			print(f"\nYou are that chosen undead everyone is talking about, what was the name they were calling you, {player_name.title()}, yes? Do you see that \033[1;31:0m\x1B[3mbonfire\x1B[0m over there? you can light them with this and  \033[1;31:0m\x1B[3msave your progress\x1B[0m.")
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
		elif player_input == "save" and player_position == platform221 and bonfire1 == True:
			print("\nPosition saved, and game data saved.")
			bonfire_save = 1
			with open("darksouls.dat", "wb") as file:
				pickle.dump((canLightBonfires, bonfire1, bonfire2, inventory, player_position, elevator_position, ending, ending1, ending2, ending3, chandelierFallen, fakewall, firstspawn, pathlever, bosses, robedguys, secret, bonfire_save), file)
		
		elif player_input == "load":
			print("\nPosition and game data loaded.")
			with open("darksouls.dat", "rb") as file:
				loaded_data = pickle.load(file)
			canLightBonfires, bonfire1, bonfire2, inventory, player_position, elevator_position, ending, ending1, ending2, ending3, chandelierFallen, fakewall, firstspawn, pathlever, bosses, robedguys, secret, bonfire_save = loaded_data
			print(f"{player_position}")

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
			print("\nYou open the \x1B[3mchest\x1B[0m and you find a \x1B[3mBlack Iron Sword\x1B[0m")
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
			print(f"\nYou swing and hit the brittle chain holding the chandelier, and it drops to the gorund crushing many foes beneath it.")
			chandelierFallen = True
		
		elif player_input == "swing" and player_position == platform232 and chest1 not in inventory:
			print("\nYou reach out to swing for the chandelier but the broken sword is not long enough and you fall to the floor killing yourself.")
			death_count = death_count + 1
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
		
		elif player_input == "east" and player_position == platform233 and elevator_position == 1:
			player_position = platform224p1
			print(f"{player_position}")
		
		elif player_input == "east" and player_position == platform233 and elevator_position == 2:
			player_position = platform411p2
			print(f"{player_position}")

		elif player_input == "west" and player_position == platform411p2:
			player_position = platform233
			print(f"{player_position}")

		elif player_input == "west" and player_position == platform224p1:
			player_position = platform233
			print(f"{player_position}")

		elif player_input == "down" and player_position == platform224p2:
			player_position = platform411p2
			print(f"{player_position}")
		
		elif player_input == "up" and player_position == platform411p2:
			player_position = platform224p2
			print(f"{player_position}")

		elif player_input == "down" and player_position == platform224p1:
			player_position = platform411p1
			print(f"{player_position}")

		elif player_input == "up" and player_position == platform411p1:
			player_position = platform224p1
			print(f"{player_position}")
			#make sure that the player cannot see the fog wall before and can after swinging
		elif player_input == "north" and player_position == platform411p1 and fakewall == True:
			print("\nYou can see an arched doorway to the north.")
			player_position = platform412
		
		elif player_input == "north" and player_position == platform411p1 and fakewall == False:
			print("\nThe pathway leads to a dead end.")
			player_position = platform412
		
		elif player_input == "south" and player_position == platform412:
			player_position = platform411p1
			print(f"{player_position}")
		
		elif player_input == "west" and player_position == platform411p1:
			player_position = platform333
			print(f"{player_position}")

		elif player_input == "swing" and player_position == platform412 and chest1 in inventory:
			print("\nYou swing at the wall and the wall turns to fog and disappears, an arched door is left in its place")
			fakewall = True
		
		elif player_input == "north" and player_position == platform412 and fakewall == True:
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

		elif player_input == "save" and player_position == platform413 and bonfire2 == True:
			print("\nPosition saved, and game data saved.")
			bonfire_save = 1
			with open("darksouls.dat", "wb") as file:
				pickle.dump((canLightBonfires, bonfire1, bonfire2, inventory, player_position, elevator_position, ending, ending1, ending2, ending3, chandelierFallen, fakewall, firstspawn, pathlever, bosses, robedguys, secret, bonfire_save), file)
		
		elif player_input == "load" and player_position == platform413 and bonfire2 == True:
			print("\nPosition and game data loaded.")
			with open("darksouls.dat", "rb") as file:
				loaded_data = pickle.load(file)
			canLightBonfires, bonfire1, bonfire2, inventory, player_position, elevator_position, ending, ending1, ending2, ending3, chandelierFallen, fakewall, firstspawn, pathlever, bosses, robedguys, secret, bonfire_save = loaded_data
		

		elif player_input == "save" and player_position == platform413:
			bonfire_save = 0
			print("\nPosition saved")

		elif player_input == "south" and player_position == platform413:
			player_position = platform412
			print("\nYou can see a dark room to the north.")
		
		elif player_input == "south" and player_position == platform333:
			player_position = platform323
			print(f"{player_position}")
		
		elif player_input == "south" and player_position == platform323 and robedguys == False:
			player_position = platform321
			print(f"{player_position}")
		
		elif player_input == "south" and player_position == platform323 and robedguys == True:
			print("\nYou try to get by the soldiers but there are too many and they stab you to death.")
			death_count = death_count + 1
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
			print("\nYou killed enought of the robed soldiers in order to kill the rest.")
			robedguys = False
		
		elif player_input == "swing" and player_position == platform323 and chandelierFallen == False:
			print("\nYou get overun by robed soldiers and get stabbed to death.")
			death_count = death_count + 1
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
			print(f"\nYou open the chest and find something, but you can't tell what it is.")
			inventory.append(chest4)

		elif player_input == "north" and player_position == platform321:
			player_position = platform322
			print(f"{player_position}")

		elif player_input == "north" and player_position == platform323:
			player_position = platform333
			print(f"{player_position}")

		elif player_input == "south" and player_position == platform224p1:
			player_position = platform314
			print(f"{player_position}")

		elif player_input == "south" and player_position == platform411p2:
			player_position = platform314
			print(f"{player_position}")

		elif player_input == "pull" and player_position == platform314:
			pathlever = True
			print("\nYou pull the lever and see a path being extended from your feet to where you were before the marble building.")
		
		elif player_input == "south" and player_position == platform314 and pathlever == True:
			player_position = platform311
			print(f"{player_position}")
		
		elif player_input == "north" and player_position == platform311 and pathlever == True:
			player_position = platform314
			print(f"{player_position}")
		
		elif player_input == "north" and player_position == platform314 and elevator_position == 1:
			player_position = platform224p1
			print(f"{player_position}")

		elif player_input == "north" and player_position == platform314 and elevator_position == 2:
			player_position = platform411p2
			print(f"{player_position}")

		elif player_input == "north" and player_position == platform224p2:
			player_position = platform225
			print(f"{player_position}")
		
		elif player_input == "south" and player_position == platform225 and elevator_position == 2:
			player_position = platform411p2
			print(f"{player_position}")
		
		elif player_input == "south" and player_position == platform121:
			player_position = platform225
			print(f"{player_position}")
		
		elif player_input == "pull" and player_position == platform225 and elevator_position == 2:
			print("\nYou pull the lever and the elevator drops.")
		
		elif player_input == "pull" and player_position == platform225 and elevator_position == 1:
			print("\nYou pull the lever and the elevator rises up.")
		
		elif player_input == "north" and player_position == platform225:
			player_position = platform121
			print(f"{player_position}")
		
		elif player_input == "talk" and player_position == platform121:
			print("\n")
			print(bk4.talk)
			print(bk5.talk)
		
		elif player_input == "swing" and player_position == platform121 and chest1 not in inventory and BK4 == True and BK5 == True:
			print("\nYou go to swing but the black night opposite you stabs you in the back.")
			death_count = death_count + 1
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
		
		elif player_input == "swing" and player_position == platform121 and chest1 in invetory and BK4 == True and BK5 == True:
			print("\nYou swing and kill the Black Knights to your left and right.")
			BK4 == False
			BK5 == False
		
		elif player_input == "north" and player_position == platform121:
			player_position = platform122
			print(f"{player_position}")
		
		elif player_input == "south" and player_position == platform122:
			player_position = platform121
			print(f"{player_position}")
		
		elif player_input == "west" and player_position == platform122:
			player_position = platform021
			print(f"{player_position}")
		
		elif player_input == "east" and player_position == platform122:
			player_position = platform021
			print(f"{player_position}")
		
		elif player_input == "west" and player_position == platform021:
			player_position = platform121
			print(f"{player_position}")
		
		elif player_input == "east" and player_position == platform021:
			player_position = platform122
			print(f"{player_position}")
		
		elif player_input == "south" and player_position == platform021:
			player_position = platform020
			print(f"{player_position}")
		
		elif player_input == "open" and player_position == platform020:
			print("\nYou open the chest and find Fine Iron Armor")
			inventory.append(chest3)
		
		elif player_input == "north" and player_position == platform020:
			player_position = platform021
			print(f"{player_position}")
		
		elif player_input == "north" and player_position == platform122:
			player_position = platform123
			print(f"{player_position}")
		
		elif player_input == "south" and player_position == platform123 and bosses == True:
			print("\nYou try to go south but there is now a fog wall covering the way. While trying to exit you get crushed by Ornstein")
			death_count = death_count + 1
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
		
		elif player_input == "swing" and player_position == platform123 and chest1 in inventory and chest2 in inventory and chest3 in inventory:
			print("\nYou swing at the crumbling column and it falls and crushes Smough, you swing for a second time and kill Ornstein")
			bosses = False
		
		elif player_input == "swing" and player_position == platform123:
			if chest1 not in inventory or chest2 not in inventory or chest3 not in inventory:
				print("You go to swing at Ornstein and Smough but you were not prepared enough to meet them.")
				death_count = death_count + 1
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
		
		elif player_input == "north" and player_position == platform123 and bosses == False:
			player_position = platform124
			print(f"{player_position}")
		
		elif player_input == "south" and player_position == platform124 and bosses == False:
			player_position = platform123
			print("\nYou are standing in a broken battlefield.")
		
		elif player_input == "north" and player_position == platform122 and bosses == False:
			player_position = platform123
			print("\nYou are standing in a broken battlefield.")
#figuring out endings.
		elif player_input == "north" and player_position == platform124:
			player_position = platform000
			print(f"{player_position}")
			if BK1 == False and BK2 == False and BK3 == False and BK4 == False and BK5 == False and robedguys == False and chandelierFallen == True and pathlever == True and canLightBonfires == True and bonfire1 == True and bonfire2 == True and secret == True:
				ending3 = True
				ending = True
			elif BK1 == False and BK2 == False and BK3 == False and BK4 == False and BK5 == False and robedguys == False and chandelierFallen == True and pathlever == True and canLightBonfires == True and bonfire1 == True and bonfire2 == True:
				ending2 = True
				ending = True
			else:
				ending1 = True
				ending = True
		
		elif player_input == "inventory":
			print(inventory)
#printing out ending.
		else:
			if ending == True:
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
					player_input = q
				#resetting all variables for another playthorugh except endings.
				print(f"Your death count {death_count}")
				canLightBonfires = False
				inventory.remove(chest1)
				inventory.remove(chest2)
				inventory.remove(chest3)
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
				player_position = platform111
				print(f"{player_position}")
			else:
				print("That is not a direction you can go or action you can do.")
				
if __name__ == "__main__":
	main()
#thanks for playing my game