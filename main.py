import random
import sys
import time
#variables
options = ["snake","water","gun"]
p_s = 0
ai_s = 0
running = 0
winner = " "
game = "This game was devloped by Onix."
special_acces = False
#Game Loop
while True:
	print("<---------*------------------*-------------------*------------->")
	ai = random.choice(options)
	print("""Choose one:
	             --------> Snake
	             --------> Water 
	             --------> Gun    """)
	time.sleep(0.5)  
	print("-----------------------------------------------------------")
	data = input("Choose: ").lower()
	print("-----------------------------------------------------------")	
	time.sleep(0.5)
		# Logic for player choosing Snake
	if data == 'snake' and ai == options[0]:
		print(F"the ai choose {ai}")
		time.sleep(0.5)
		print("Nothing happens....")
		time.sleep(0.5)
		print("-----------------------------------------------------------")
		print(f"player: {p_s} , {ai_s} : ai")
	elif data == 'snake' and ai == options[1]:
		p_s += 1
		print(F"the ai choose {ai}")
		time.sleep(0.5)
		print("the SNAKE drinks the WATER.")
		time.sleep(0.5)
		print("-----------------------------------------------------------")
		print(f"player: {p_s} , {ai_s} : ai")
	elif data == 'snake' and ai == options[2]:
		ai_s += 1
		print(F"the ai choose {ai}")
		time.sleep(0.5)
		print("the SNAKE is shot with the GUN.")
		time.sleep(0.5)
		print("-----------------------------------------------------------")
		print(f"player: {p_s} , {ai_s} : ai")
		# Logic for player choosing water
	elif data == 'water' and ai == options[0]:
		ai_s += 1
		print(F"the ai choose {ai}")
		time.sleep(0.5)
		print("the SNAKE drinks the WATER.")
		time.sleep(0.5)
		print("-----------------------------------------------------------")
		print(f"player: {p_s} , {ai_s} : ai")
	elif data == 'water' and ai == options[1]:
		print(F"the ai choose {ai}")
		time.sleep(0.5)
		print("nothing happens....")
		time.sleep(0.5)
		print("-----------------------------------------------------------")
		print(f"player: {p_s} , {ai_s} : ai")
	elif data == 'water' and ai == options[2]:
		p_s += 1
		print(F"the ai choose {ai}")
		time.sleep(0.5)
		print("the WATER is poured on the GUN.")
		time.sleep(0.5)
		print("-----------------------------------------------------------")
		print(f"player: {p_s} , {ai_s} : ai")
	# Logic for player choosing GUN
	elif data == 'gun' and ai == options[0]:
		p_s += 1
		print(F"the ai choose {ai}")
		time.sleep(0.5)
		print("the SNAKE is shot with the GUN.")
		time.sleep(0.5)
		print("-----------------------------------------------------------")
		print(f"player: {p_s} , {ai_s} : ai")
	elif data == 'gun' and ai == options[1]:
		ai_s += 1
		print(F"the ai choose {ai}")
		time.sleep(0.5)
		print("the WATER is poured on the GUN.")
		time.sleep(0.5)
		print("-----------------------------------------------------------")
		print(f"player: {p_s} , {ai_s} : ai")
	elif data == 'gun' and ai == options[2]:
		print(F"the ai choose {ai}")
		time.sleep(0.5)
		print("nothing happens....")
		time.sleep(0.5)
		print("-----------------------------------------------------------")
		print(f"player: {p_s} , {ai_s} : ai")
	elif data == "onix404":
		pass
	else:
		print(" invalid Entry....!")
#winner Logic	
	if p_s == 3 or ai_s == 3:
		if p_s == 3:
			winner = "Player"
		else:
			winner = "AI"
		print(f"{winner} has won!")
		break
	if data not in options and not "iplays" :
		print("ErroR 404.")
	if data == "iplays":
		p_s = 3
		special_acces = True 
		print("Special_acces Granted.")
		time.sleep(1.2)
		print("Welcome Boss.")
		break