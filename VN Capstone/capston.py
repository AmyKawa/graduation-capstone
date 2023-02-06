import pygame, random, sys, time, clock

screen = pygame.display.set_mode((1229, 922))
clock = pygame.time.Clock()
pygame.init()
RightClickInput = ''

pygame.display.set_caption('Capstone')

def text(message, x, y, fontsize, r, g, b):
	# Pre: Reads message, the coordinates, fontsize and colors through rgb values
	# Post: Displays text on the Pygame window according to the parameters above
	font = pygame.font.Font('OMORI_GAME2.ttf', int(fontsize))
	string = font.render(message, False, (r,g,b))
	screen.blit(string, (x, y))

def get_button_info():
	#Pre: This gives the player information on the move they want to use by right clicking a button
	#Post: Returns needed information
	#4 MAIN
	if RightClickInput == 'ATTACK':
		text(characters[char_index] + '\'s basic attack', 400, 50, 50, 255, 255, 255)
	if RightClickInput == 'SKILL':
		text(characters[char_index] + '\'s special attacks and more', 330, 50, 50, 255, 255, 255)
	if RightClickInput == 'SNACK':
		text('Heals, buffs and revives', 400, 50, 50, 255, 255, 255)
	if RightClickInput == 'ITEM':
		text('Enemy debuffs, damage and more', 330, 50, 50, 255, 255, 255)
	#SKILLS
	#SKYLER
	if RightClickInput == 'UPPERCUT':
		text('Deals damage, has a chance to stun opponent', 400, 50, 50, 255, 255, 255)
		text('Cost: 20 JUICE', 400, 100, 50, 255, 255, 255)
	if RightClickInput == 'HEADBUTT':
		text('Deals heavy damage, but SKYLER will be stunned for 1 turn', 400, 50, 50, 255, 255, 255)
		text('Cost: 30 JUICE', 400, 100, 50, 255, 255, 255)
	if RightClickInput == 'PREPARE':
		text('SKYLER\'s next attack does more damage', 330, 50, 50, 255, 255, 255)
		text('COST: 30 JUICE', 330, 100, 50, 255, 255, 255)
	#AXEL
	if RightClickInput == 'BASH':
		text('A powerful hit that deals extra damage', 330, 50, 50, 255, 255, 255)
		text('COST: 20 JUICE', 330, 100, 50, 255, 255, 255)
	if RightClickInput == 'POWER SWING':
		text('Axel swings his hammer, hitting the opponent 3 times', 330, 50, 50, 255, 255, 255)
		text('COST: 40 JUICE', 330, 100, 50, 255, 255, 255)
	if RightClickInput == 'TAUNT':
		text('The opponent targets AXEL for one turn', 330, 50, 50, 255, 255, 255)
		text('COST: 10 JUICE', 330, 100, 50, 255, 255, 255)
	#COEN
	if RightClickInput == 'QUICK SLASH':
		text('Coen sneaks up on the opponent and slashes them', 330, 50, 50, 255, 255, 255)
		text('Ignores enemy DEF', 330, 100, 50, 255, 255, 255)
		text('Cost: 20 JUICE', 330, 150, 50, 255, 255, 255)
	if RightClickInput == 'SACRIFICE':
		text('A very powerful attack, but Coen KO\'s himself afterward', 330, 50, 50, 255, 255, 255)
		text('and cannot be woken up for the rest of the battle', 330, 100, 50, 255, 255, 255)
		text('COST: 5 JUICE', 330, 150, 50, 255, 255, 255)
	if RightClickInput == 'BRAG':
		text('Coen brags about his greatness, making the target annoyed', 330, 50, 50, 255, 255, 255)
		text('Raises a friend\'s ATK but lowers their DEF', 330, 100, 50, 255, 255, 255)
		text('COST: 25 JUICE', 330, 150, 50, 255, 255, 255)
	#HAZEL
	if RightClickInput == 'FIRST AID':
		text('Heals a friend for 75% of their hearts', 330, 50, 50, 255, 255, 255)
		text('Cost: 30 JUICE', 330, 100, 50, 255, 255, 255)
	if RightClickInput == 'REFRESH':
		text('Heals a friend for 40% of their juice', 330, 50, 50, 255, 255, 255)
		text('COST: 30 HEARTS', 330, 100, 50, 255, 255, 255)
	if RightClickInput == 'GROUP HUG':
		text('Raises all friends stats', 330, 50, 50, 255, 255, 255)
		text('COST: 60 JUICE', 330, 150, 50, 255, 255, 255)
	#GUARD
	if RightClickInput == 'GUARD':
		text('Damage is reduced for one turn', 330, 50, 50, 255, 255, 255)
		text('COST: 0 JUICE', 330, 100, 50, 255, 255, 255)
	if RightClickInput == 'REFLECT':
		text('Some damage is reflected back at the opponent', 330, 50, 50, 255, 255, 255)
		text('COST: 0 JUICE', 330, 100, 50, 255, 255, 255)
	#SNACKS
	if RightClickInput == 'BREAD':
		text('Fresh from the bakery!', 400, 50, 50, 255, 255, 255)
		text('Heal 60 HEART', 400, 100, 50, 255, 255, 255)
		text('OWNED: '+ str(breadamount), 400, 150, 50, 255, 255, 255)
	if RightClickInput == 'GRAPE SODA':
		text('The only thing Vending Machines sell', 330, 50, 50, 255, 255, 255)
		text('Heal 40 JUICE', 330, 100, 50, 255, 255, 255)
		text('OWNED: '+ str(sodaamount), 330, 150, 50, 255, 255, 255)
	if RightClickInput == 'COFFEE':
		text('From Starbucks, wherever that is', 330, 50, 50, 255, 255, 255)
		text('Raises ATK and DEF of friend', 330, 100, 50, 255, 255, 255)
		text('heavily, but KO\'s them after 6 turns', 330, 150, 50, 255, 255, 255)
		text('OWNED: '+ str(coffeeamount), 330, 200, 50, 255, 255, 255)
	if RightClickInput == 'BLUE CHEESE':
		text('The smell is strong...', 310, 50, 50, 255, 255, 255)
		text('Wakes up a friend who\'s knocked out', 310, 100, 50, 255, 255, 255)
		text('OWNED: '+ str(cheeseamount), 310, 150, 50, 255, 255, 255)
	#ITEMS
	if RightClickInput == 'DYNAMITE':
		text('Is this even legal...?', 330, 50, 50, 255, 255, 255)
		text('Deals damage, and has 10% chance', 330, 100, 50, 255, 255, 255)
		text('to instantly KO opponent', 330, 150, 50, 255, 255, 255)
		text('OWNED: '+ str(breadamount), 330, 200, 50, 255, 255, 255)
	if RightClickInput == 'NAILS':
		text('My feet! It stings!', 330, 50, 50, 255, 255, 255)
		text('Prevents enemy from attacking you', 330, 100, 50, 255, 255, 255)
		text('for one turn', 330, 150, 50, 255, 255, 255)
		text('OWNED: '+ str(breadamount), 330, 200, 50, 255, 255, 255)
	if RightClickInput == 'BOXING GLOVE':
		text('Everything looks blurry...', 400, 50, 50, 255, 255, 255)
		text('Reduces the enemy\'s ATK', 400, 100, 50, 255, 255, 255)
		text('OWNED: '+ str(breadamount), 400, 150, 50, 255, 255, 255)
	if RightClickInput == 'FEATHER':
		text('Why do you even have this?', 400, 50, 50, 255, 255, 255)
		text('Reduces the enemy\'s DEF', 400, 100, 50, 255, 255, 255)
		text('OWNED: '+ str(breadamount), 400, 150, 50, 255, 255, 255)
		
	

class button:
	def __init__(self, text, x, y, w, h, size, x_offset, fontsize):
		# Pre: Reads the values that it's given in brackets
		# Post: Creates a button of those given values (position, size, text)
		self.rect = pygame.Rect(x, y, w, h)
		self.text = text
		self.size = size
		self.x_offset = x_offset
		self.mouse = False
		self.clicked = False
		self.font = pygame.font.Font('OMORI_GAME2.ttf', int(fontsize))

	def draw(self):
		# Pre: Reads created button size, position and text
		# Post: Draws the button on the Pygame screen, also deals with mouseover display to change color when hovered over
		if self.mouse == True:
			self.letter = self.font.render(self.text, True, (255,0,0))
			pygame.draw.rect(screen, (255, 255, 255), self.rect, 0, 15, 15)
			screen.blit(self.letter, (self.rect.x + self.x_offset, self.rect.y-2))
		else:
			self.letter = self.font.render(self.text, True, (0, 0, 0))
			pygame.draw.rect(screen, (255,255,255), self.rect, 0, 15, 15)
			screen.blit(self.letter, (self.rect.x + self.x_offset, self.rect.y-2))

	def mouseover(self):
		# Pre: Gets the x and y coordinates of the mouse cursor
		# Post: If the mouse is on a coordinate where a button is, tells the code that the button has been moused over
		x , y = pygame.mouse.get_pos()
		if x >= self.rect.x and x < self.rect.x + self.size and y > self.rect.y and y < self.rect.y + self.size:
			self.mouse = True
		else:
			self.mouse = False
	
	def buttonclicked(self):
		global keydelay
		# Pre: Determines if the mouse button is down and if it's over a button
		# Post: Adds the letter/word value it clicked on to the list of either guessed letters or another variable to detect word
		global sButtonInput
		global RightClickInput
		pos = pygame.mouse.get_pos()
		letterclicked = 'placeholder'
		if self.rect.collidepoint(pos):
			self.mouse = True
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and keydelay > 10:
				self.clicked = True
				sButtonInput = self.text
				keydelay = 0
				print (sButtonInput)
			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False
			if pygame.mouse.get_pressed()[2] == 1 and self.clicked == False and keydelay > 10:
				self.clicked = True
				RightClickInput = self.text
				get_button_info()
			if pygame.mouse.get_pressed()[2] == 0:
				self.clicked = False
				RightClickInput = ''
		else:
			self.mouse = False

class character:
	def __init__(self, heart, juice, atk, defence, name):
		# Creates a character
		self.heart = heart
		self.juice = juice
		self.atk = atk
		self.defence = defence
		self.name = name
	
	def attack(self):
		# Returns the attack value
		return self.atk
	
	def took_dmg(self, amount):
		# Removes heart, if it's smaller than 0, set to 0 (can't have negative health!)
		self.heart -= amount
		if self.heart == 0 or self.heart < 0:
			self.heart = 0
		
	def heal(self, method):
		# The many ways a person can heal themselves
		# Endure is limited to Skyler only.
		# Also prevents characters from going above their maximum health
		if method == 'BREAD':
			self.heart += 60
		
		if method == 'ENDURE':
			self.heart = 1
			
		if self.name == 'SKYLER':
			if self.heart > 105:
				self.heart = 105
		elif self.name == 'AXEL':
			if self.heart > 240:
				self.heart = 240
		elif self.name == 'COEN':
			if self.heart > 120:
				self.heart = 120
		elif self.name == 'HAZEL':
			if self.heart > 260:
				self.heart = 260
	
	def heal_juice(self, method):
		# Heals their juice, used for abilities
		# Make sure that it can't go over each character's max juice too
		if method == 'GRAPE SODA':
			self.juice += 40
	
	def buff(self, method):
		# Increases certain stats
		if method == 'COFFEE':
			self.atk += 45
			self.defence += 25

	def debuff(self, method):
		# Decreases certain stats
		if method == 'BOXING GLOVE':
			self.atk -= 20
		elif method == 'FEATHER':
			self.defence -= 20
	
	def revive(self):
		# Revive a player, gives them 50% of their total HP back upon revivial
		if self.heart == 0:
			if self.name == 'SKYLER':
				self.heart = 53
			elif self.name == 'AXEL':
				self.heart = 120
			elif self.name == 'COEN':
				self.heart = 60
			elif self.name == 'HAZEL':
				self.heart = 130
	
	def remove_juice(self, amount):
		# I don't think we need this? But it removed juice (much like a sad omori character)
		self.juice -= amountd

	def isdead(self):
		# Checks to see if a player is dead
		if self.heart == 0:
			return True
		else:
			return False
	
	def defend(self):
		# Returns defence value for the character
		return self.defence

	def gethearts(self):
		# Returns hearts for the character
		return self.heart

	def getjuice(self):
		# Returns juice value for the character
		return self.juice

def buttondisplay(button):
	# Pre: Reads button that user entered
	# Post: Draws the button on screen and adds its mouseover and buttonclicked properties
	button.draw()
	button.mouseover()
	button.buttonclicked()

def list_buttondisplay(buttonlist):
	# Pre: Reads list that user entered
	# Post: Draws all buttons in the list on screen and adds its mouseover and buttonclicked properties
	for button in range(len(buttonlist)):
		buttonlist[button].draw()
		buttonlist[button].mouseover()
		buttonlist[button].buttonclicked()

def listconfig(input_list, output_list):
	# Creates the list of skills and outputs it in the screen
	skill_x = 310
	skill_y = 643
	skillnumber = 0
	skill_character = 0
	width = 270
	height = 80
	fontsize = 80
	if input_list == snack_list or input_list == item_list or input_list == Askill_list or input_list == Hskill_list or input_list == Cskill_list:
		fontsize = 50
	for skill in input_list:
		currbutton = (button(skill, skill_x, skill_y, width, height, 150, 25, fontsize))
		skill_x += 300
		if skillnumber == 1:
			skill_x = 310
			skill_y = 743
		skillnumber += 1
		output_list.append(currbutton)
	
def display_stats():
	# Shows the names of the characters as well as their heart and juice. Updates real time
	text('SKYLER', 97, 576, 50, 255, 255, 255)
	text('AXEL', 117, 56, 50, 255, 255, 255)
	text('COEN', 1017, 576, 50, 255, 255, 255)
	text('HAZEL', 1017, 56, 50, 255, 255, 255)
	
	text('HEARTS: ' + str(int(Axel.gethearts())) + '/240', 69, 300, 30, 255, 255, 255)
	text('JUICE: ' + str(int(Axel.getjuice())) + '/110', 69, 334, 30, 255, 255, 255)
	
	text('HEARTS: ' + str(int(Hazel.gethearts())) + '/260', 977, 300, 30, 255, 255, 255)
	text('JUICE: ' + str(int(Hazel.getjuice())) + '/90', 977, 334, 30, 255, 255, 255)
	
	text('HEARTS: ' + str(int(Skyler.gethearts())) + '/105', 69, 822, 30, 255, 255, 255)
	text('JUICE: ' + str(int(Skyler.getjuice())) + '/75', 69, 856, 30, 255, 255, 255)
	
	text('HEARTS: ' + str(int(Coen.gethearts())) + '/120', 977, 822, 30, 255, 255, 255)
	text('JUICE: ' + str(int(Coen.getjuice())) + '/150', 977, 856, 30, 255, 255, 255)
	

# Initiating skills, snacks, and items, as well as resets variables
# Also inititates buttons	
rungame = True
stage = 'begin'
characters = ['SKYLER', 'AXEL', 'COEN', 'HAZEL', '']
snack_selection = ['SKYLER', 'AXEL', 'COEN', 'HAZEL']

Sskill_list = ['UPPERCUT', 'HEADBUTT', 'PREPARE', 'REFLECT'] 
Askill_list = ['BASH', 'POWER SWING', 'TAUNT', 'GUARD']
Hskill_list = ['FIRST AID', 'REFRESH', 'GROUP HUG', 'GUARD'] 
Cskill_list = ['QUICK SLASH', 'SACRIFICE', 'BRAG', 'GUARD']

snack_list = ['BREAD', 'GRAPE SODA', 'COFFEE', 'BLUE CHEESE']
item_list = ['DYNAMITE', 'NAILS', 'BOXING GLOVE', 'FEATHER']
current_skills = []
breadamount = 0
sodaamount = 0
coffeeamount = 0
cheeseamount = 0
Ssnack = ''
Asnack = ''
Hsnack = ''
Csnack = ''
sButtonInput = ''
delay = 0
char_index = 0
keydelay = 0
tick = 0
overall_turn = 0
character_move = ['', '', '', '', '']
movebuttons = []
enemy_stunned = False
skyler_canendure = True

FightButton = (button('Fight!', 310, 643, 600, 80, 150, 100, 80))
RunButton = (button('Run...', 310, 743, 600, 80, 150, 100, 80))

AttackButton = (button('ATTACK', 310, 643, 270, 80, 150, 25, 80))
SkillButton = (button('SKILL', 610, 643, 270, 80, 150, 25, 80))
SnackButton = (button('SNACK', 310, 743, 270, 80, 150, 25, 80))
ItemButton = (button('ITEM', 610, 743, 270, 80, 150, 25, 80))
movebuttons.append(AttackButton)
movebuttons.append(SkillButton)
movebuttons.append(SnackButton)
movebuttons.append(ItemButton)

Sskill_buttons = []
Askill_buttons = []
Hskill_buttons = []
Cskill_buttons = []
snacks = []
items = []
party_buttons = []

listconfig(Sskill_list, Sskill_buttons)
listconfig(Askill_list, Askill_buttons)
listconfig(Hskill_list, Hskill_buttons)
listconfig(Cskill_list, Cskill_buttons)

listconfig(snack_list, snacks)
listconfig(item_list, items)

listconfig(snack_selection, party_buttons)

Skyler = (character(105, 75, 50, 50, 'SKYLER'))
Axel = (character(100, 110, 80, 40, 'AXEL')) 
Coen = (character(120, 150, 40, 40, 'COEN')) 
Hazel = (character(260, 90, 30, 65, 'HAZEL')) 

Penelope = (character(4000, 2000, 80, 40, 'PENELOPE'))
active_char = 'SKYLER'
while rungame:

	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			rungame = False
	
	display_stats()
	text('PENELOPE HEART:' + str(int(Penelope.gethearts())), 350, 450, 50, 255, 255, 255)
	text('PENELOPE JUICE:' + str(int(Penelope.getjuice())), 350, 500, 50, 255, 255, 255)
	
	pygame.draw.rect(screen, (255, 255, 255), (50, 50, 230, 320), 5)
	pygame.draw.rect(screen, (255, 255, 255), (50, 572, 230, 320), 5)
	pygame.draw.rect(screen, (255, 255, 255), (949, 50, 230, 320), 5)
	pygame.draw.rect(screen, (255, 255, 255), (949, 572, 230, 320), 5)
	#Axel
	pygame.draw.line(screen, (255,255,255), (49 , 115), (280, 115), 4)
	pygame.draw.line(screen, (255,255,255), (49 , 300), (280, 300), 4)
	pygame.draw.line(screen, (255,255,255), (49 , 333), (280, 333), 4)
	#Hazel
	pygame.draw.line(screen, (255,255,255), (948 , 115), (1179, 115), 4)
	pygame.draw.line(screen, (255,255,255), (948 , 300), (1179, 300), 4)
	pygame.draw.line(screen, (255,255,255), (948 , 333), (1179, 333), 4)
	#Skyler
	pygame.draw.line(screen, (255,255,255), (49 , 637), (280, 637), 4)
	pygame.draw.line(screen, (255,255,255), (49 , 822), (280, 822), 4)
	pygame.draw.line(screen, (255,255,255), (49 , 855), (280, 855), 4)
	#Coen
	pygame.draw.line(screen, (255,255,255), (948 , 637), (1179, 637), 4)
	pygame.draw.line(screen, (255,255,255), (948 , 822), (1179, 822), 4)
	pygame.draw.line(screen, (255,255,255), (948 , 855), (1179, 855), 4)
	
	# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-MOVE SELECTION~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
	
	if stage == 'begin':
		if sButtonInput == '':
			text('What will SKYLER and friends do?', 350, 50, 50, 255, 255, 255)
		buttondisplay(FightButton)
		buttondisplay(RunButton)
		
		if sButtonInput == 'Fight!':
			stage = 'move'
		if sButtonInput == 'Run...':
			text(active_char+"'s party tried to run...", 400, 50, 50, 255, 255, 255)
			text("But couldn't get away.", 400, 100, 50, 255, 255, 255)
			if delay == 200:
				sButtonInput = ''
				delay = 0
			delay += 1
	
	# Individual move selection

	if stage == 'move':
		if RightClickInput == '':
			text('What will '+ characters[char_index] + ' do?', 400, 50, 50, 255, 255, 255)
			text("Hold right click on a button for info", 330, 100, 50, 255, 255, 255)
		if sButtonInput == '' or sButtonInput == 'Fight!':
			list_buttondisplay(movebuttons)
		
		if sButtonInput == 'ATTACK':
			character_move[char_index] = 'ATTACK'
			char_index += 1
			print (character_move)
			sButtonInput = ''
		if sButtonInput == 'SKILL':
			if characters[char_index] == 'SKYLER':
				list_buttondisplay(Sskill_buttons)
			elif characters[char_index] == 'AXEL':
				list_buttondisplay(Askill_buttons)
			elif characters[char_index] == 'HAZEL':
				list_buttondisplay(Hskill_buttons)
			elif characters[char_index] == 'COEN':
				list_buttondisplay(Cskill_buttons)

			if sButtonInput != 'SKILL':
				character_move[char_index] = sButtonInput
				char_index += 1
				print (character_move)
				sButtonInput = ''
		if sButtonInput == 'SNACK':
			list_buttondisplay(snacks)
			if sButtonInput != 'SNACK' and sButtonInput != 'Back':
				character_move[char_index] = sButtonInput
				sButtonInput = 'snack'
				stage = 'snacktarget'
		if sButtonInput == 'ITEM':
			list_buttondisplay(items)
			if sButtonInput != 'ITEM':
				character_move[char_index] = sButtonInput
				dyna_KO = random.randint(1,10)
				print (dyna_KO)
				char_index += 1
				print (character_move)
				sButtonInput = ''	
		
		if Skyler.gethearts() == 0 and characters[char_index] == 'SKYLER' or Axel.gethearts() == 0 and characters[char_index] == 'AXEL' or Coen.gethearts() == 0 and characters[char_index] == 'COEN' or Hazel.gethearts() == 0 and characters[char_index] == 'HAZEL':
			char_index += 1
	
	if stage == 'snacktarget':
		text('On who?', 530, 50, 50, 255, 255, 255)
		list_buttondisplay(party_buttons)
		if sButtonInput != 'snack':
			if characters[char_index] == 'SKYLER':
				Ssnack = sButtonInput
			elif characters[char_index] == 'AXEL':
				Asnack = sButtonInput
			elif characters[char_index] == 'HAZEL':
				Hsnack = sButtonInput
			elif characters[char_index] == 'COEN':
				Csnack = sButtonInput
			char_index += 1
			print (character_move)
			sButtonInput = ''
			stage = 'move'
		
	if char_index == 4:
		turn_index = 0
		tick = 0
		turn = 'skyler'
		stage = 'players_move'
	
	# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-MOVE EXECUTION~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

	if stage == 'players_move':
		char_index = 'placeholder'
		
		# Attack
		if character_move[turn_index] == 'ATTACK':
			if turn_index == 0:
				text('SKYLER attacks PENELOPE', 400, 50, 50, 255, 255, 255)
				text('PENELOPE took '+ str(int(Skyler.attack() - (Penelope.defend() / 3))) +' damage!', 400, 100, 50, 255, 255, 255)
				if tick < 1:
					Penelope.took_dmg(Skyler.attack() - (Penelope.defend() / 3))
			elif turn_index == 1:
				text('AXEL attacks PENELOPE', 400, 50, 50, 255, 255, 255)
				text('PENELOPE took '+ str(int(Axel.attack() - (Penelope.defend() / 3))) +' damage!', 400, 100, 50, 255, 255, 255)
				if tick < 1:
					Penelope.took_dmg(Axel.attack()  - (Penelope.defend() / 3))
			elif turn_index == 2:
				text('COEN attacks PENELOPE', 400, 50, 50, 255, 255, 255)
				text('PENELOPE took '+ str(int(Coen.attack() - (Penelope.defend() / 3))) +' damage!', 400, 100, 50, 255, 255, 255)
				if tick < 1:
					Penelope.took_dmg(Coen.attack() - (Penelope.defend() / 3))
			elif turn_index == 3:
				text('HAZEL attacks PENELOPE', 400, 50, 50, 255, 255, 255)
				text('PENELOPE took '+ str(int(Hazel.attack() - (Penelope.defend() / 3))) +' damage!', 400, 100, 50, 255, 255, 255)
				if tick < 1:
					Penelope.took_dmg(Hazel.attack() - (Penelope.defend() / 3))
				
		# Skills
		if character_move[turn_index] == 'UPPERCUT':
			text('SKYLER punches PENELOPE in the jaw!', 330, 50, 50, 255, 255, 255)
			text('PENELOPE took ' + str(int(Skyler.attack() * 1.2 - (Penelope.defend() / 3))) + ' damage!', 330, 100, 50, 255, 255, 255)
			if tick < 1:
				Penelope.took_dmg(Skyler.attack() * 1.2 - (Penelope.defend() / 3))
				Skyler.remove_juice(20)
			
		# Snacks
		if character_move[turn_index] == 'BREAD':
			if turn_index == 0:
				text('SKYLER uses BREAD!', 400, 50, 50, 255, 255, 255)
				text(Ssnack + ' gains 60 HEARTS!', 400, 100, 50, 255, 255, 255)
				if tick < 1:
					if Ssnack == 'SKYLER':
						Skyler.heal('BREAD')
					elif Ssnack == 'AXEL':
						Axel.heal('BREAD')
					elif Ssnack == 'COEN':
						Coen.heal('BREAD')
					elif Ssnack == 'HAZEL':
						Hazel.heal('BREAD')
			elif turn_index == 1:
				text('AXEL uses BREAD!', 400, 50, 50, 255, 255, 255)
				text(Asnack + ' gains 60 HEARTS!', 400, 100, 50, 255, 255, 255)
				if tick < 1:
					if Asnack == 'SKYLER':
						Skyler.heal('BREAD')
					elif Asnack == 'AXEL':
						Axel.heal('BREAD')
					elif Asnack == 'COEN':
						Coen.heal('BREAD')
					elif Asnack == 'HAZEL':
						Hazel.heal('BREAD')
			elif turn_index == 2:
				text('COEN uses BREAD!', 400, 50, 50, 255, 255, 255)
				text(Csnack + ' gains 60 HEARTS!', 400, 100, 50, 255, 255, 255)
				if tick < 1:
					if Csnack == 'SKYLER':
						Skyler.heal('BREAD')
					elif Csnack == 'AXEL':
						Axel.heal('BREAD')
					elif Csnack == 'COEN':
						Coen.heal('BREAD')
					elif Csnack == 'HAZEL':
						Hazel.heal('BREAD')
			elif turn_index == 3:
				text('HAZEL uses BREAD!', 400, 50, 50, 255, 255, 255)
				text(Hsnack + ' gains 60 HEARTS!', 400, 100, 50, 255, 255, 255)
				if tick < 1:
					if Hsnack == 'SKYLER':
						Skyler.heal('BREAD')
					elif Hsnack == 'AXEL':
						Axel.heal('BREAD')
					elif Hsnack == 'COEN':
						Coen.heal('BREAD')
					elif Hsnack == 'HAZEL':
						Hazel.heal('BREAD')
				
		if character_move[turn_index] == 'GRAPE SODA':
			if turn_index == 0:
				text('SKYLER uses GRAPE SODA!', 400, 50, 50, 255, 255, 255)
				text(Ssnack + ' gains 40 JUICE!', 400, 100, 50, 255, 255, 255)
				if tick < 1:
					if Ssnack == 'SKYLER':
						Skyler.heal_juice('GRAPE SODA')
					elif Ssnack == 'AXEL':
						Axel.heal_juice('GRAPE SODA')
					elif Ssnack == 'COEN':
						Coen.heal_juice('GRAPE SODA')
					elif Ssnack == 'HAZEL':
						Hazel.heal_juice('GRAPE SODA')
			elif turn_index == 1:
				text('AXEL uses GRAPE SODA!', 400, 50, 50, 255, 255, 255)
				text(Asnack + ' gains 40 JUICE!', 400, 100, 50, 255, 255, 255)
				if tick < 1:
					if Asnack == 'SKYLER':
						Skyler.heal_juice('GRAPE SODA')
					elif Asnack == 'AXEL':
						Axel.heal_juice('GRAPE SODA')
					elif Asnack == 'COEN':
						Coen.heal_juice('GRAPE SODA')
					elif Asnack == 'HAZEL':
						Hazel.heal_juice('GRAPE SODA')
			elif turn_index == 2:
				text('COEN uses GRAPE SODA!', 400, 50, 50, 255, 255, 255)
				text(Csnack + ' gains 40 JUICE!', 400, 100, 50, 255, 255, 255)
				if tick < 1:
					if Csnack == 'SKYLER':
						Skyler.heal_juice('GRAPE SODA')
					elif Csnack == 'AXEL':
						Axel.heal_juice('GRAPE SODA')
					elif Csnack == 'COEN':
						Coen.heal_juice('GRAPE SODA')
					elif Csnack == 'HAZEL':
						Hazel.heal_juice('GRAPE SODA')
			elif turn_index == 3:
				text('HAZEL uses GRAPE SODA!', 400, 50, 50, 255, 255, 255)
				text(Hsnack + ' gains 40 JUICE!', 400, 100, 50, 255, 255, 255)
				if tick < 1:
					if Hsnack == 'SKYLER':
						Skyler.heal_juice('GRAPE SODA')
					elif Hsnack == 'AXEL':
						Axel.heal_juice('GRAPE SODA')
					elif Hsnack == 'COEN':
						Coen.heal_juice('GRAPE SODA')
					elif Hsnack == 'HAZEL':
						Hazel.heal_juice('GRAPE SODA')
		if character_move[turn_index] == 'COFFEE':
			if turn_index == 0:
				text('SKYLER uses COFFEE!', 400, 50, 50, 255, 255, 255)
				text(Ssnack + ' ATK rose!', 400, 100, 50, 255, 255, 255)
				text(Ssnack + ' DEF rose!', 400, 150, 50, 255, 255, 255)
				if tick < 1:
					coffeeturn_1 = overall_turn
					if Ssnack == 'SKYLER':
						Skyler.buff('COFFEE')
					elif Ssnack == 'AXEL':
						Axel.buff('COFFEE')
					elif Ssnack == 'COEN':
						Coen.buff('COFFEE')
					elif Ssnack == 'HAZEL':
						Hazel.buff('COFFEE')
			elif turn_index == 1:
				text('AXEL uses COFFEE!', 400, 50, 50, 255, 255, 255)
				text(Asnack + ' ATK rose!', 400, 100, 50, 255, 255, 255)
				text(Asnack + ' DEF rose!', 400, 150, 50, 255, 255, 255)
				if tick < 1:
					coffeeturn_1 = overall_turn
					if Asnack == 'SKYLER':
						Skyler.buff('COFFEE')
					elif Asnack == 'AXEL':
						Axel.buff('COFFEE')
					elif Asnack == 'COEN':
						Coen.buff('COFFEE')
					elif Asnack == 'HAZEL':
						Hazel.buff('COFFEE')
			elif turn_index == 2:
				text('COEN uses COFFEE!', 400, 50, 50, 255, 255, 255)
				text(Csnack + ' ATK rose!', 400, 100, 50, 255, 255, 255)
				text(Csnack + ' DEF rose!', 400, 150, 50, 255, 255, 255)
				if tick < 1:
					coffeeturn_1 = overall_turn
					if Csnack == 'SKYLER':
						Skyler.buff('COFFEE')
					elif Csnack == 'AXEL':
						Axel.buff('COFFEE')
					elif Csnack == 'COEN':
						Coen.buff('COFFEE')
					elif Csnack == 'HAZEL':
						Hazel.buff('COFFEE')
			elif turn_index == 3:
				text('HAZEL uses COFFEE!', 400, 50, 50, 255, 255, 255)
				text(Hsnack + ' ATK rose!', 400, 100, 50, 255, 255, 255)
				text(Hsnack + ' DEF rose!', 400, 150, 50, 255, 255, 255)
				if tick < 1:
					coffeeturn_1 = overall_turn
					if Hsnack == 'SKYLER':
						Skyler.buff('COFFEE')
					elif Hsnack == 'AXEL':
						Axel.buff('COFFEE')
					elif Hsnack == 'COEN':
						Coen.buff('COFFEE')
					elif Hsnack == 'HAZEL':
						Hazel.buff('COFFEE')
		if character_move[turn_index] == 'BLUE CHEESE':
			if turn_index == 0:
				text('SKYLER uses BLUE CHEESE!', 400, 50, 50, 255, 255, 255)
				if Ssnack == 'SKYLER' and Skyler.isdead() == True or Ssnack == 'AXEL' and Axel.isdead() == True or Ssnack == 'COEN' and Coen.isdead() == True or Ssnack == 'HAZEL' and Hazel.isdead() == True:
					text(Ssnack + 'woke up!', 400, 100, 50, 255, 255, 255)
				else:
					text(Ssnack + ' wrinkles their nose...', 400, 100, 50, 255, 255, 255)
					text('The smell is not very pleasant', 400, 150, 50, 255, 255, 255)
				if tick < 1:
					if Ssnack == 'SKYLER' and Skyler.isdead() == True:
						Skyler.revive()
					elif Ssnack == 'AXEL' and Axel.isdead() == True:
						Axel.revive()
					elif Ssnack == 'COEN' and Coen.isdead() == True:
						Coen.revive()
					elif Ssnack == 'HAZEL' and Hazel.isdead() == True:
						Hazel.revive()
			elif turn_index == 1:
				text('AXEL uses BLUE CHEESE!', 400, 50, 50, 255, 255, 255)
				if Asnack == 'SKYLER' and Skyler.isdead() == True or Ssnack == 'AXEL' and Axel.isdead() == True or Ssnack == 'COEN' and Coen.isdead() == True or Ssnack == 'HAZEL' and Hazel.isdead() == True:
					text(Asnack + 'woke up!', 400, 100, 50, 255, 255, 255)
				else:
					text(Asnack + ' wrinkles their nose...', 400, 100, 50, 255, 255, 255)
					text('The smell is not very pleasant', 400, 150, 50, 255, 255, 255)
				if tick < 1:
					if Asnack == 'SKYLER' and Skyler.isdead() == True:
						Skyler.revive()
					elif Asnack == 'AXEL' and Axel.isdead() == True:
						Axel.revive()
					elif Asnack == 'COEN' and Coen.isdead() == True:
						Coen.revive()
					elif Asnack == 'HAZEL' and Hazel.isdead() == True:
						Hazel.revive()
			elif turn_index == 2:
				text('COEN uses BLUE CHEESE!', 400, 50, 50, 255, 255, 255)
				if Csnack == 'SKYLER' and Skyler.isdead() == True or Ssnack == 'AXEL' and Axel.isdead() == True or Ssnack == 'COEN' and Coen.isdead() == True or Ssnack == 'HAZEL' and Hazel.isdead() == True:
					text(Csnack + 'woke up!', 400, 100, 50, 255, 255, 255)
				else:
					text(Csnack + ' wrinkles their nose...', 400, 100, 50, 255, 255, 255)
					text('The smell is not very pleasant', 400, 150, 50, 255, 255, 255)
				if tick < 1:
					if Csnack == 'SKYLER' and Skyler.isdead() == True:
						Skyler.revive()
					elif Csnack == 'AXEL' and Axel.isdead() == True:
						Axel.revive()
					elif Csnack == 'COEN' and Coen.isdead() == True:
						Coen.revive()
					elif Csnack == 'HAZEL' and Hazel.isdead() == True:
						Hazel.revive()
			elif turn_index == 3:
				text('HAZEL uses BLUE CHEESE!', 400, 50, 50, 255, 255, 255)
				if Hsnack == 'SKYLER' and Skyler.isdead() == True or Ssnack == 'AXEL' and Axel.isdead() == True or Ssnack == 'COEN' and Coen.isdead() == True or Ssnack == 'HAZEL' and Hazel.isdead() == True:
					text(Hsnack + 'woke up!', 400, 100, 50, 255, 255, 255)
				else:
					text(Hsnack + ' wrinkles their nose...', 400, 100, 50, 255, 255, 255)
					text('The smell is not very pleasant', 400, 150, 50, 255, 255, 255)
				if tick < 1:
					if Hsnack == 'SKYLER' and Skyler.isdead() == True:
						Skyler.revive()
					elif Hsnack == 'AXEL' and Axel.isdead() == True:
						Axel.revive()
					elif Hsnack == 'COEN' and Coen.isdead() == True:
						Coen.revive()
					elif Hsnack == 'HAZEL' and Hazel.isdead() == True:
						Hazel.revive()

		# Items
		if character_move[turn_index] == 'NAILS':
			if turn_index == 0:
				text('SKYLER throws NAILS everywhere!', 330, 50, 50, 255, 255, 255)
			elif turn_index == 1:
				text('AXEL throws NAILS everywhere!', 330, 50, 50, 255, 255, 255)
			elif turn_index == 2:
				text('COEN throws NAILS everywhere!', 330, 50, 50, 255, 255, 255)
			elif turn_index == 3:
				text('HAZEL throws NAILS everywhere!', 330, 50, 50, 255, 255, 255)
			text('PENELOPE steps on some of them!', 330, 100, 50, 255, 255, 255)
			text('PENELOPE is stunned!', 330, 150, 50, 255, 255, 255)
			enemy_stunned = True
		if character_move[turn_index] == 'DYNAMITE':
			if turn_index == 0:
				text('SKYLER throws DYNAMITE!', 400, 50, 50, 255, 255, 255)
			elif turn_index == 1:
				text('AXEL throws DYNAMITE!', 400, 50, 50, 255, 255, 255)
			elif turn_index == 2:
				text('COEN throws DYNAMITE!', 400, 50, 50, 255, 255, 255)
			elif turn_index == 3:
				text('HAZEL throws DYNAMITE!', 400, 50, 50, 255, 255, 255)
			if tick < 1:
				if dyna_KO == 5:
					phearts = Penelope.gethearts()
					Penelope.took_dmg(Penelope.gethearts())
				else:
					Penelope.took_dmg(50)
			if dyna_KO == 5:
				text('It was a critical hit!', 400, 100, 50, 255, 255, 255)
				text('PENELOPE took '+ str(int(phearts)) +' damage!', 400, 150, 50, 255, 255, 255)
			else:
				text('It was a little off...', 400, 100, 50, 255, 255, 255)
				text('PENELOPE took 50 damage!', 400, 150, 50, 255, 255, 255)
		if character_move[turn_index] == 'BOXING GLOVE':
			text('SKYLER punches PENELOPE!', 400, 50, 50, 255, 255, 255)
			text('PENELOPE\'s ATK fell...', 400, 100, 50, 255, 255, 255)
			if tick < 1:
				Penelope.debuff('BOXING GLOVE')
		if character_move[turn_index] == 'FEATHER':
			text('SKYLER tickles PENELOPE with', 330, 50, 50, 255, 255, 255)
			text('the FEATHER!', 330, 100, 50, 255, 255, 255)
			text('PENELOPE\'s DEF fell...', 330, 150, 50, 255, 255, 255)
			if tick < 1:
				Penelope.debuff('FEATHER')
			
		if Skyler.isdead() == True and turn_index == 0 or Axel.isdead() == True and turn_index == 1 or Coen.isdead() == True and turn_index == 2:
			turn_index += 1
			tick = 0
		elif Hazel.isdead() and turn_index == 3:
			tick = 0
			e_move = 1#random.randint(1,5)
			e_target = random.choice(snack_selection)
			stage = 'enemy_move'
		else:
			pass
	
		if tick > 100:
			if turn_index == 3:
				tick = 0
				e_move = 1#random.randint(1,5)
				e_target = random.choice(snack_selection)
				print (e_target)
				stage = 'enemy_move'
				tick = 0
			else:
				turn_index += 1
				tick = 0
			
		tick += 1
				
			

	if stage == 'enemy_move':
		if enemy_stunned == True:
			text('PENELOPE is too busy dealing with', 330, 50, 50, 255, 255, 255)
			text('the NAILS to make a move...', 330, 100, 50, 255, 255, 255)
		else:
			if e_move == 1:
				text('PENELOPE slaps ' + e_target+'!', 400, 50, 50, 255, 255, 255)
				if e_target == 'SKYLER':
					text(e_target + ' took '+ str(int(Penelope.attack() - (Skyler.defend() / 2))) +' damage!', 400, 100, 50, 255, 255, 255)
					if tick < 1:
						Skyler.took_dmg(Penelope.attack() - (Skyler.defend() / 2))
					if skyler_canendure == True and Skyler.gethearts() <= 1:
						text('SKYLER endured the hit...', 400, 150, 50, 255, 255, 255)
				elif e_target == 'AXEL':
					text(e_target + ' took '+ str(int(Penelope.attack() - (Axel.defend() / 2))) +' damage!', 400, 100, 50, 255, 255, 255)
					if tick < 1:
						Axel.took_dmg(Penelope.attack() - (Axel.defend() / 2))
				elif e_target == 'COEN':
					text(e_target + ' took '+ str(int(Penelope.attack() - (Coen.defend() / 2))) +' damage!', 400, 100, 50, 255, 255, 255)
					if tick < 1:
						Coen.took_dmg(Penelope.attack() - (Coen.defend() / 2))
				elif e_target == 'HAZEL':
					text(e_target + ' took '+ str(int(Penelope.attack() - (Hazel.defend() / 2))) +' damage!', 400, 100, 50, 255, 255, 255)
					if tick < 1:
						Hazel.took_dmg(Penelope.attack() - (Hazel.defend() / 2))
			# ~ elif e_move == 2:
				# ~ text('Penelope barks', 330, 50, 50, 255, 255, 255)
			# ~ elif e_move == 3:
				# ~ text('Penelope barks', 330, 50, 50, 255, 255, 255)
			# ~ elif e_move == 4:
				# ~ text('Penelope barks', 330, 50, 50, 255, 255, 255)
			# ~ elif e_move == 5:
				# ~ text('Penelope barks', 330, 50, 50, 255, 255, 255)
			
			if skyler_canendure == True:
				if Skyler.gethearts() == 0:
					Skyler.heal('ENDURE')
					skyler_canendure = False
		
		
			if tick > 100:
				tick = 0
				char_index = 0
				character_move = ['','','','','']
				enemy_stunned = False
				stage = 'begin'
			
		#if tick < 1:
	
		tick += 1
	
	# ~ cursorX, cursorY = pygame.mouse.get_pos()
	# ~ if pygame.mouse.get_pressed()[0] == 1:
		# ~ print (cursorX, cursorY)

	keydelay += 1
	
	pygame.display.update()
	clock.tick(60)
pygame.quit()
