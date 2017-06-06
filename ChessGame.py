import random
import pygame

pygame.init()
screen = pygame.display.set_mode((640,640))
done = False
height = 640
width = 640
grid = []
numberCore = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8}
letterCore = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H"}
letterList = ['A','B','C', 'D', 'E', 'F', 'G', 'H']
turn = 0

font = pygame.font.Font(None, 30)
font1 = pygame.font.Font(None, 25)

whiteObjects = []
blackObjects = []
chessObjects = []

def gridDevelopment():
	num = 0
	for i in range(0, 8):
		grid.append([])
		num += 1
		for k in range(0 , 8):
			if num % 2 == 0:
				if k % 2 == 0:
					grid[i].append([139,69,19])
				else:
					grid[i].append([210,180,140])
			else:
				if k % 2 == 0:
					grid[i].append([210,180,140])
				else:
					grid[i].append([139,69,19])

def landscape():
	for i in range(0, 8):
		for k in range(0, 8):
			pygame.draw.rect(screen, grid[i][k], pygame.Rect(i*80, k*80, 80, 80))
			screen.blit(font.render(letterCore.get(k+1) + str(i + 1), 1, (0,0,0)), (i*80 + 22, k*80 + 22))
			
class Pawn:
	gridLetter = ''
	gridNumber = 0
	color = ''
	numMoves = 0
	name = 'pawn'
	def __init__(self, letter, number, color):
		self.color = color
		self.gridLetter = letter
		self.gridNumber = number
		self.numMoves = 0
	def check(self):
		pass
	def redraw(self):
		if self.color == 'white':
			pygame.draw.rect(screen, (255, 255, 255) , pygame.Rect( (self.gridNumber-1)*80+16, (numberCore.get(self.gridLetter)-1)*80+16, 48, 48))
			screen.blit(font1.render("P", 1, (0,0,0)), ((self.gridNumber-1)*80 + 17, (numberCore.get(self.gridLetter)-1)*80 + 17))
			screen.blit(font1.render((self.gridLetter) + str(self.gridNumber), 1, (0,0,0)), ((self.gridNumber-1)*80 + 29, (numberCore.get(self.gridLetter)-1)*80 + 33))
		else:
			pygame.draw.rect(screen, (0, 0, 0) , pygame.Rect( (self.gridNumber-1)*80+16, (numberCore.get(self.gridLetter)-1)*80+16, 48, 48))
			screen.blit(font1.render("P", 1, (255,255,255)), ((self.gridNumber-1)*80 + 17, (numberCore.get(self.gridLetter)-1)*80 + 17))
			screen.blit(font1.render((self.gridLetter) + str(self.gridNumber), 1, (255,255,255)), ((self.gridNumber-1)*80 + 29, (numberCore.get(self.gridLetter)-1)*80 + 33))
		#PYGAME DRAW PAWN AND A NUMBER ON IT LIKE : WhitePawn1
	def movement(self, let, num, list):
		
		
		
	
		for j in list:
			for i in j:
				if i.getLocation() == (let + str(num)):
					print("Invalid Movement")
					return False
				if abs(num - self.gridNumber) == abs(numberCore.get(let)-numberCore.get(self.gridLetter)):
					if self.color == 'white' and num-self.gridNumber == 1:
						for i in list[1]:
							if i.getLocation() == (let + str(num)):
								i.death(list)
								self.gridLetter = let
								self.gridNumber = num
								self.numMoves += 1
								return True
					elif self.color == 'black' and self.gridNumber-num == 1:
						for i in list[0]:
							if i.getLocation() == (let + str(num)):
								i.death(list)
								self.gridLetter = let
								self.gridNumber = num
								self.numMoves += 1
								return True
		if self.color == 'white':
			if ((num - self.gridNumber) == 2 and self.numMoves == 0):
				pass
			elif ((num - self.gridNumber) != 1) or self.gridLetter != let and num < 9:
				print("Invalid Movement")
				return False
			self.gridLetter = let
			self.gridNumber = num
			self.numMoves += 1
			return True
		else:
			if ((num - self.gridNumber) == -2 and self.numMoves == 0):
				pass
			elif (num - self.gridNumber) != -1 or self.gridLetter != let and num > 0:
				print("Invalid Movement")
				return False
			self.gridLetter = let
			self.gridNumber = num
			self.numMoves += 1
			return True
			

	def getLocation(self):
		return (self.gridLetter + str(self.gridNumber))
	def death(self, list):
		if self.color == 'white':
			whiteObjects.remove(self)
		else:
			blackObjects.remove(self)

class Rook:
	gridLetter = ''
	gridNumber = 0
	color = ''
	numMoves = 0
	name = 'rook'
	def __init__(self, letter, number, color):
		self.color = color
		self.gridLetter = letter
		self.gridNumber = number
	def check(self):
		pass
	def redraw(self):
		if self.color == 'white':
			pygame.draw.rect(screen, (255, 255, 255) , pygame.Rect( (self.gridNumber-1)*80+16, (numberCore.get(self.gridLetter)-1)*80+16, 48, 48))
			screen.blit(font1.render("R", 1, (0,0,0)), ((self.gridNumber-1)*80 + 17, (numberCore.get(self.gridLetter)-1)*80 + 17))
			screen.blit(font1.render((self.gridLetter) + str(self.gridNumber), 1, (0,0,0)), ((self.gridNumber-1)*80 + 29, (numberCore.get(self.gridLetter)-1)*80 + 33))
		else:
			pygame.draw.rect(screen, (0, 0, 0) , pygame.Rect( (self.gridNumber-1)*80+16, (numberCore.get(self.gridLetter)-1)*80+16, 48, 48))
			screen.blit(font1.render("R", 1, (255,255,255)), ((self.gridNumber-1)*80 + 17, (numberCore.get(self.gridLetter)-1)*80 + 17))
			screen.blit(font1.render((self.gridLetter) + str(self.gridNumber), 1, (255,255,255)), ((self.gridNumber-1)*80 + 29, (numberCore.get(self.gridLetter)-1)*80 + 33))
	def movement(self, let, num, list):
		#no color distinction needed for movement
		if not ((let == self.gridLetter) or (num == self.gridNumber)):
			print("Invalid Movement")
			return False
		if num > 8 or num < 1 or let not in letterList and pathClear(list):
			print('err')
			return False
		if True:#len(list[0]) > 1 and len(list[1]) > 1: 
			numb = 0
			if let != self.gridLetter:
				numb += 1
			for i in list:
				for k in i:
					if self.color == 'white':
						if i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'black':
							print(i.getLocation() +" Captured")
							i.death(list)
							self.gridLetter = let
							self.gridNumber = num
							self.numMoves += 1
							return True
						elif i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'white':
							i.death(list)
							self.gridLetter = let
							self.gridNumber = num
							self.numMoves += 1
							return True
					else:
						if i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'white':
							print(i.getLocation() +" Captured")
							i.death(list)
							return True
						elif i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'black':
							print("Invalid Movement")
							return False
					if numb > 0:#if moving in letter direction
						if numberCore.get(let) - numberCore.get(self.gridLetter) < 0:
							print(1)
							for p in range(numberCore.get(let), numberCore.get(self.gridLetter)):
								if k.getLocation()[0] == letterCore.get(p) and int(k.getLocation()[1]) == self.gridNumber:
									print("Invalid Movement") ##RETURN DO YOU WANT TO ATTACK??
									return False
						else:
							print(2)
							for p in range(numberCore.get(self.gridLetter)+1, numberCore.get(let)+1):
								if k.getLocation()[0] == letterCore.get(p) and int(k.getLocation()[1]) == self.gridNumber:
									print("Invalid Movement") ##RETURN DO YO UWANT TO ATTACK?
									return False
					else:#moving in number direction
						print("num")
						if num - self.gridNumber < 0:
							print(1)
							for p in range(num, self.gridNumber):
								if int(k.getLocation()[1]) == p and k.getLocation()[0] == self.gridLetter:
									print("Invalid Movement")
									return False
						else:
							print(2)
							for p in range(self.gridNumber+1, num+1):
								if int(k.getLocation()[1]) == p and k.getLocation()[0] == self.gridLetter:
									print("Invalid Movement")
									return False	
		self.gridLetter = let
		self.gridNumber = num
		return True

		
	def getLocation(self):
		return (self.gridLetter + str(self.gridNumber))

	def death(self, list):
		if self.color == 'white':
			whiteObjects.remove(self)
		else:
			blackObjects.remove(self)

class Knight:
	gridLetter = ''
	gridNumber = 0
	color = ''
	numMoves = 0
	name = 'knight'
	def __init__(self, letter, number, color):
		self.color = color
		self.gridLetter = letter
		self.gridNumber = number
	def check(self):
		pass
	def redraw(self):
		if self.color == 'white':
			pygame.draw.rect(screen, (255, 255, 255) , pygame.Rect( (self.gridNumber-1)*80+16, (numberCore.get(self.gridLetter)-1)*80+16, 48, 48))
			screen.blit(font1.render("KT", 1, (0,0,0)), ((self.gridNumber-1)*80 + 17, (numberCore.get(self.gridLetter)-1)*80 + 17))
			screen.blit(font1.render((self.gridLetter) + str(self.gridNumber), 1, (0,0,0)), ((self.gridNumber-1)*80 + 29, (numberCore.get(self.gridLetter)-1)*80 + 33))
		else:
			pygame.draw.rect(screen, (0, 0, 0) , pygame.Rect( (self.gridNumber-1)*80+16, (numberCore.get(self.gridLetter)-1)*80+16, 48, 48))
			screen.blit(font1.render("KT", 1, (255,255,255)), ((self.gridNumber-1)*80 + 17, (numberCore.get(self.gridLetter)-1)*80 + 17))
			screen.blit(font1.render((self.gridLetter) + str(self.gridNumber), 1, (255,255,255)), ((self.gridNumber-1)*80 + 29, (numberCore.get(self.gridLetter)-1)*80 + 33))
		#PYGAME DRAW PAWN AND A NUMBER ON IT LIKE : WhitePawn1
	def movement(self, let, num, list):
		for k in list:
			for i in k:
				if self.color == 'white':
					if i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'black':
						i.death(list)
						self.gridLetter = let
						self.gridNumber = num
						self.numMoves += 1
						return True
					elif i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'white':
						i.death(list)
						self.gridLetter = let
						self.gridNumber = num
						self.numMoves += 1
						return True
				else:
					if i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'white':
						print(i.getLocation() +" Captured")
						i.death(list)
						return True
					elif i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'black':
						print("Invalid Movement")
						return False
		#check is someone is in that spot and check if out of bounds ##########
		if let not in letterList or num < 1 or num > 8:
			print('Invalid Movement')
			return False
		
		if abs(numberCore.get(let) - numberCore.get(self.gridLetter)) == 2 and abs(num - self.gridNumber) == 1:
			self.gridNumber = num
			self.gridLetter = let
			return True
		elif abs(numberCore.get(let) - numberCore.get(self.gridLetter)) == 1 and abs(num - self.gridNumber) == 2:
			self.gridNumber = num
			self.gridLetter = let
			return True
		else:
			print("Invalid Movement")
			return False

	def getLocation(self):
		return (self.gridLetter + str(self.gridNumber))

	def death(self, list):
		if self.color == 'white':
			whiteObjects.remove(self)
		else:
			blackObjects.remove(self)
		
class Bishop:
	gridLetter = ''
	gridNumber = 0
	color = ''
	numMoves = 0
	name = 'bishop'
	def __init__(self, letter, number, color):
		self.color = color
		self.gridLetter = letter
		self.gridNumber = number
	def check(self):
		pass
	def redraw(self):
		if self.color == 'white':
			pygame.draw.rect(screen, (255, 255, 255) , pygame.Rect( (self.gridNumber-1)*80+16, (numberCore.get(self.gridLetter)-1)*80+16, 48, 48))
			screen.blit(font1.render("B", 1, (0,0,0)), ((self.gridNumber-1)*80 + 17, (numberCore.get(self.gridLetter)-1)*80 + 17))
			screen.blit(font1.render((self.gridLetter) + str(self.gridNumber), 1, (0,0,0)), ((self.gridNumber-1)*80 + 29, (numberCore.get(self.gridLetter)-1)*80 + 33))
		else:
			pygame.draw.rect(screen, (0, 0, 0) , pygame.Rect( (self.gridNumber-1)*80+16, (numberCore.get(self.gridLetter)-1)*80+16, 48, 48))
			screen.blit(font1.render("B", 1, (255,255,255)), ((self.gridNumber-1)*80 + 17, (numberCore.get(self.gridLetter)-1)*80 + 17))
			screen.blit(font1.render((self.gridLetter) + str(self.gridNumber), 1, (255,255,255)), ((self.gridNumber-1)*80 + 29, (numberCore.get(self.gridLetter)-1)*80 + 33))
		#PYGAME DRAW PAWN AND A NUMBER ON IT LIKE : WhitePawn1
	def movement(self, let, num, list):
		number = 0
		for k in list:
			for i in k:
				#if someone is within diag pos
				if abs(int(i.getLocation()[1]) - int(self.getLocation()[1])) == abs(numberCore.get(i.getLocation()[0]) - numberCore.get(self.getLocation()[0])) and abs(numberCore.get(i.getLocation()[0]) - numberCore.get(self.getLocation()[0])) != 0:
					if self.color == 'white':
						if i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'black':
							i.death(list)
							self.gridLetter = let
							self.gridNumber = num
							self.numMoves += 1
							return True
						elif i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'white':
							i.death(list)
							self.gridLetter = let
							self.gridNumber = num
							self.numMoves += 1
							return True
					else:
						if i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'white':
							print(i.getLocation() +" Captured")
							i.death(list)
							return True
						elif i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'black':
							print("Invalid Movement")
							return False
					if self.gridNumber - num < 0:
						for n in range(self.gridNumber, num):
							if int(i.getLocation()[1]) == n:
								if numberCore.get(self.gridLetter) - numberCore.get(let) < 0:
									for m in range(numberCore.get(self.gridLetter), numberCore.get(let)):
										if letterCore.get(m) == i.getLocation()[0]:
											print("Invalid Movement")
											return False
								elif numberCore.get(self.gridLetter) - numberCore.get(let) > 0:
									for m in range(numberCore.get(let), numberCore.get(self.gridLetter)):
										if letterCore.get(m) == i.getLocation()[0]:
											print("Invalid Movement")
											return False
								else:
									print("Invalid Movement")
									return False
					elif self.gridNumber - num > 0:
						for n in range(num, self.gridNumber):
							if int(i.getLocation()[1]) == n:
								if numberCore.get(self.gridLetter) - numberCore.get(let) < 0:
									for m in range(numberCore.get(self.gridLetter), numberCore.get(let)):
										if letterCore.get(m) == i.getLocation()[0]:
											print("Invalid Movement")
											return False
								elif numberCore.get(self.gridLetter) - numberCore.get(let) > 0:
									for m in range(numberCore.get(let), numberCore.get(self.gridLetter)):
										if letterCore.get(m) == i.getLocation()[0]:
											print("Invalid Movement")
											return False
								else:
									print("Invalid Movement")
									return False
					else:
						print("Invalid Movement")
						return False
			#CHANGE TO SEE IF ANYONE IS IN PATH ^^^^^
		if let not in letterList or num < 1 or num > 8:
			print("Invalid Movement")
			return False
		if abs(numberCore.get(let) - numberCore.get(self.gridLetter)) == abs(num - self.gridNumber):
			self.gridNumber = num
			self.gridLetter = let
			return True
		else:
			print("Invalid Movement")
			return False

	def getLocation(self):
		return (self.gridLetter + str(self.gridNumber))
	def attack(self, attackPos):
		print("lol")

	def death(self, list):
		if self.color == 'white':
			whiteObjects.remove(self)
		else:
			blackObjects.remove(self)

class Queen:
	gridLetter = ''
	gridNumber = 0
	color = ''
	numMoves = 0
	name = 'queen'
	def __init__(self, letter, number, color):
		self.color = color
		self.gridLetter = letter
		self.gridNumber = number
	def check(self):
		pass
	def redraw(self):
		if self.color == 'white':
			pygame.draw.rect(screen, (255, 255, 255) , pygame.Rect( (self.gridNumber-1)*80+16, (numberCore.get(self.gridLetter)-1)*80+16, 48, 48))
			screen.blit(font1.render("Q", 1, (0,0,0)), ((self.gridNumber-1)*80 + 17, (numberCore.get(self.gridLetter)-1)*80 + 17))
			screen.blit(font1.render((self.gridLetter) + str(self.gridNumber), 1, (0,0,0)), ((self.gridNumber-1)*80 + 29, (numberCore.get(self.gridLetter)-1)*80 + 33))
		else:
			pygame.draw.rect(screen, (0, 0, 0) , pygame.Rect( (self.gridNumber-1)*80+16, (numberCore.get(self.gridLetter)-1)*80+16, 48, 48))
			screen.blit(font1.render("Q", 1, (255,255,255)), ((self.gridNumber-1)*80 + 17, (numberCore.get(self.gridLetter)-1)*80 + 17))
			screen.blit(font1.render((self.gridLetter) + str(self.gridNumber), 1, (255,255,255)), ((self.gridNumber-1)*80 + 29, (numberCore.get(self.gridLetter)-1)*80 + 33))
		#PYGAME DRAW PAWN AND A NUMBER ON IT LIKE : WhitePawn1

	def movement(self, let, num, list):
		if abs(num-self.gridNumber) == abs(numberCore.get(let) - numberCore.get(self.gridLetter)):
			diag = True
		else:
			diag = False
			
		if diag == True:
			number = 0
			for k in list:
				for i in k:
					#if someone is within diag pos
					if abs(int(i.getLocation()[1]) - int(self.getLocation()[1])) == abs(numberCore.get(i.getLocation()[0]) - numberCore.get(self.getLocation()[0])) and abs(numberCore.get(i.getLocation()[0]) - numberCore.get(self.getLocation()[0])) != 0:
						if self.color == 'white':
							if i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'black':
								print(i.getLocation() +" Captured")
								i.death(list)
								self.gridLetter = let
								self.gridNumber = num
								self.numMoves += 1
								return True
							elif i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'white':
								print("Invalid Movement")
								return False
						else:
							if i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'white':
								print(i.getLocation() +" Captured")
								i.death(list)
								self.gridLetter = let
								self.gridNumber = num
								self.numMoves += 1
								return True
							elif i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'black':
								print("Invalid Movement")
								return False
						if self.gridNumber - num < 0:
							for n in range(self.gridNumber, num):
								if int(i.getLocation()[1]) == n:
									if numberCore.get(self.gridLetter) - numberCore.get(let) < 0:
										for m in range(numberCore.get(self.gridLetter), numberCore.get(let)):
											if letterCore.get(m) == i.getLocation()[0]:
												print("Invalid Movement")
												return False
									elif numberCore.get(self.gridLetter) - numberCore.get(let) > 0:
										for m in range(numberCore.get(let), numberCore.get(self.gridLetter)):
											if letterCore.get(m) == i.getLocation()[0]:
												print("Invalid Movement")
												return False
									else:
										print("Invalid Movement")
										return False
						elif self.gridNumber - num > 0:
							for n in range(num, self.gridNumber):
								if int(i.getLocation()[1]) == n:
									if numberCore.get(self.gridLetter) - numberCore.get(let) < 0:
										for m in range(numberCore.get(self.gridLetter), numberCore.get(let)):
											if letterCore.get(m) == i.getLocation()[0]:
												print("Invalid Movement")
												return False
									elif numberCore.get(self.gridLetter) - numberCore.get(let) > 0:
										for m in range(numberCore.get(let), numberCore.get(self.gridLetter)):
											if letterCore.get(m) == i.getLocation()[0]:
												print("Invalid Movement")
												return False
									else:
										print("Invalid Movement")
										return False
						else:
							print("Invalid Movement")
							return False
				#CHANGE TO SEE IF ANYONE IS IN PATH ^^^^^
			if let not in letterList or num < 1 or num > 8:
				print("Invalid Movement")
				return False
			if abs(numberCore.get(let) - numberCore.get(self.gridLetter)) == abs(num - self.gridNumber):
				self.gridNumber = num
				self.gridLetter = let
				return True
			else:
				print("Invalid Movement")
				return False
		
		else:
			if not ((let == self.gridLetter) or (num == self.gridNumber)):
				print("Invalid Movement")
				return False
			if num > 8 or num < 1 or let not in letterList and pathClear(list):
				print("Invalid Movement")
				return False
			if True:#len(list[0]) > 1 and len(list[1]) > 1: 
				numb = 0
				if let != self.gridLetter:
					numb += 1
			for i in list:
				for k in i:
					if self.color == 'white':
						if i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'black':
							print(i.getLocation() +" Captured")
							i.death(list)
							self.gridLetter = let
							self.gridNumber = num
							self.numMoves += 1
							return True
						elif i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'white':
							print("Invalid Movement")
							return False
					else:
						if i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'white':
							print(i.getLocation() +" Captured")
							i.death(list)
							self.gridLetter = let
							self.gridNumber = num
							self.numMoves += 1
							return True
						elif i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'black':
							print("Invalid Movement")
							return False
					if numb > 0:#if moving in letter direction
						print("Invalid Movement")
						if numberCore.get(let) - numberCore.get(self.gridLetter) < 0:
							for p in range(numberCore.get(let), numberCore.get(self.gridLetter)):
								if k.getLocation()[0] == letterCore.get(p) and int(k.getLocation()[1]) == self.gridNumber:
									print("Invalid Movement") ##RETURN DO YOU WANT TO ATTACK??
									return False
						else:
							for p in range(numberCore.get(self.gridLetter)+1, numberCore.get(let)+1):
								if k.getLocation()[0] == letterCore.get(p) and int(k.getLocation()[1]) == self.gridNumber:
									print("Invalid Movement") ##RETURN DO YO UWANT TO ATTACK?
									return False
					else:#moving in number direction
						if num - self.gridNumber < 0:
							for p in range(num, self.gridNumber):
								if int(k.getLocation()[1]) == p and k.getLocation()[0] == self.gridLetter:
									print("Invalid Movement")
									return False
						else:
							for p in range(self.gridNumber+1, num+1):
								if int(k.getLocation()[1]) == p and k.getLocation()[0] == self.gridLetter:
									print("Invalid Movement")
									return False	
			self.gridLetter = let
			self.gridNumber = num
			return True
		print("Invalid Movement")
		return False
	def getLocation(self):
		return (self.gridLetter + str(self.gridNumber))
		
	def attack(self, attackPos):
		print("lol")

	def death(self, list):
		if self.color == 'white':
			whiteObjects.remove(self)
		else:
			blackObjects.remove(self)

class King:
	gridLetter = ''
	gridNumber = 0
	color = ''
	numMoves = 0
	name = 'king'
	def __init__(self, letter, number, color):
		self.color = color
		self.gridLetter = letter
		self.gridNumber = number
	def redraw(self):
		if self.color == 'white':
			pygame.draw.rect(screen, (255, 255, 255) , pygame.Rect( (self.gridNumber-1)*80+16, (numberCore.get(self.gridLetter)-1)*80+16, 48, 48))
			screen.blit(font1.render("KG", 1, (0,0,0)), ((self.gridNumber-1)*80 + 17, (numberCore.get(self.gridLetter)-1)*80 + 17))
			screen.blit(font1.render((self.gridLetter) + str(self.gridNumber), 1, (0,0,0)), ((self.gridNumber-1)*80 + 29, (numberCore.get(self.gridLetter)-1)*80 + 33))
		else:
			pygame.draw.rect(screen, (0, 0, 0) , pygame.Rect( (self.gridNumber-1)*80+16, (numberCore.get(self.gridLetter)-1)*80+16, 48, 48))
			screen.blit(font1.render("KG", 1, (255,255,255)), ((self.gridNumber-1)*80 + 17, (numberCore.get(self.gridLetter)-1)*80 + 17))
			screen.blit(font1.render((self.gridLetter) + str(self.gridNumber), 1, (255,255,255)), ((self.gridNumber-1)*80 + 29, (numberCore.get(self.gridLetter)-1)*80 + 33))
		#PYGAME DRAW PAWN AND A NUMBER ON IT LIKE : WhitePawn1
	def movement(self, let, num, list): # CHECK
		for k in list:
			for i in k:
				if self.color == 'white':
					if i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'black':
						print(i.getLocation() +" Captured")
						i.death(list)
						self.gridLetter = let
						self.gridNumber = num
						self.numMoves += 1
						return True
					elif i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'white':
						print("Invalid Movement")
						return False
				else:
					if i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'white':
						print(i.getLocation() +" Captured")
						i.death(list)
						self.gridLetter = let
						self.gridNumber = num
						self.numMoves += 1
						return True
					elif i.getLocation()[0] == let and int(i.getLocation()[1]) == num and i.color == 'black':
						print("Invalid Movement")
						return False
		if let not in letterList or num < 1 or num > 8:
			print("Invalid Movement")
			return False
		if abs(numberCore.get(let) - numberCore.get(self.gridLetter)) == 1 or abs(num - self.gridNumber) == 1:
			self.gridNumber = num
			self.gridLetter = let
			return True
		else:
			print("Invalid Movement" )
			return False

	def getLocation(self):
		return (self.gridLetter + str(self.gridNumber))
		
	def check(self):
		#CHECK PROXIMITY OF OPPOSING PIECES OF ALL GENRES FOR A CHECK
		if self.color == 'white':
			for i in chessObjects[1]:
				if i.name ==    'rook':
					pass
				elif i.name ==  'pawn':
					if (i.gridNumber - self.gridNumber == 1) and (numberCore.get(i.gridLetter) - numberCore.get(self.gridLetter) == 1 or numberCore.get(i.gridLetter) - numberCore.get(self.gridLetter) == -1):
						print('white check')
						return True
				elif i.name ==  'bishop':
					pass
				elif i.name ==  'queen':
					pass
				elif i.name ==  'knight':
					if abs(self.gridNumber - i.gridNumber) == 2 and abs(numberCore.get(self.gridLetter) - numberCore.get(i.gridLetter)) == 1 or abs(self.gridNumber - i.gridNumber) == 1 and abs(numberCore.get(self.gridLetter) - numberCore.get(i.gridLetter)) == 2:
						print('white check')
						return True
				return False
		elif self.color == 'black':
			for i in chessObjects[0]:
				if i.name ==    'rook':
					pass
				elif i.name ==  'pawn':
					if (i.gridNumber - self.gridNumber == -1) and (numberCore.get(i.gridLetter) - numberCore.get(self.gridLetter) == 1 or numberCore.get(i.gridLetter) - numberCore.get(self.gridLetter) == -1):
						print('black check')
						return True
				elif i.name ==  'bishop':
					pass
				elif i.name ==  'queen':
					pass
				elif i.name ==  'knight':
					if abs(self.gridNumber - i.gridNumber) == 2 and abs(numberCore.get(self.gridLetter) - numberCore.get(i.gridLetter)) == 1 or abs(self.gridNumber - i.gridNumber) == 1 and abs(numberCore.get(self.gridLetter) - numberCore.get(i.gridLetter)) == 2:
						print('black check')
						return True
				return False
		return False
	def death(self, list):
		#do some form of check bc death and check should be SAME
		pass

def inititation():
	#__________________________________
	whitePawn1 = Pawn('A', 2, 'white')
	whitePawn2 = Pawn('B', 2, 'white')
	whitePawn3 = Pawn('C', 2, 'white')
	whitePawn4 = Pawn('D', 2, 'white')
	whitePawn5 = Pawn('E', 2, 'white')
	whitePawn6 = Pawn('F', 2, 'white')
	whitePawn7 = Pawn('G', 2, 'white')
	whitePawn8 = Pawn('H', 2, 'white')
	whiteKnight1 = Knight('B', 1, 'white')
	whiteKnight2 = Knight('G', 1, 'white')
	whiteRook1 = Rook('A', 1, 'white')
	whiteRook2 = Rook('H', 1, 'white')
	whiteBishop1 = Bishop('C', 1, 'white')
	whiteBishop2 = Bishop('F', 1, 'white')
	whiteKing1 = King('E', 1, 'white')
	whiteQueen1 = Queen('D', 1, 'white')
	#---------------------------------------
	whiteObjects.append(whitePawn1)
	whiteObjects.append(whitePawn2)
	whiteObjects.append(whitePawn3)
	whiteObjects.append(whitePawn4)
	whiteObjects.append(whitePawn5)
	whiteObjects.append(whitePawn6)
	whiteObjects.append(whitePawn7)
	whiteObjects.append(whitePawn8)
	whiteObjects.append(whiteKnight1)
	whiteObjects.append(whiteKnight2)
	whiteObjects.append(whiteKing1)
	whiteObjects.append(whiteQueen1)
	whiteObjects.append(whiteRook1)
	whiteObjects.append(whiteRook2)
	whiteObjects.append(whiteBishop1)
	whiteObjects.append(whiteBishop2)
	#______________________________________

	#_____________________________________
	blackPawn1 = Pawn('A', 7, 'black')
	blackPawn2 = Pawn('B', 7, 'black')
	blackPawn3 = Pawn('C', 7, 'black')
	blackPawn4 = Pawn('D', 7, 'black')
	blackPawn5 = Pawn('E', 7, 'black')
	blackPawn6 = Pawn('F', 7, 'black')
	blackPawn7 = Pawn('G', 7, 'black')
	blackPawn8 = Pawn('H', 7, 'black')
	blackRook1 = Rook('H', 8, 'black')
	blackRook2 = Rook('A', 8, 'black')
	blackBishop1 = Bishop('C', 8, 'black')
	blackBishop2 = Bishop('F', 8, 'black')
	blackQueen1 = Queen('D', 8, 'black')
	blackKing1 = King('E', 8, 'black')
	blackKnight1 = Knight('B', 8, 'black')
	blackKnight2 = Knight('G', 8, 'black')
	#------------------------------------
	blackObjects.append(blackPawn1)
	blackObjects.append(blackPawn2)
	blackObjects.append(blackPawn3)
	blackObjects.append(blackPawn4)
	blackObjects.append(blackPawn5)
	blackObjects.append(blackPawn6)
	blackObjects.append(blackPawn7)
	blackObjects.append(blackPawn8)
	blackObjects.append(blackQueen1)
	blackObjects.append(blackKing1)
	blackObjects.append(blackBishop2)
	blackObjects.append(blackBishop1)
	blackObjects.append(blackRook1)
	blackObjects.append(blackRook2)
	blackObjects.append(blackKnight1)
	blackObjects.append(blackKnight2)
	#____________________________________`

	chessObjects.append(whiteObjects)
	chessObjects.append(blackObjects)

def essentialMovement(num):
	if num%2 == 0:
	#if True:
		print("______________WHITE_______________")
		move = input("LOCATION TO MOVE: \n")
		for i in whiteObjects:
			if i.getLocation() == move:
				while(True):
					movement = input("MOVE TO WHERE: \n")
					if len(movement) == 2 or movement == 'change':
						if movement == 'change':
							essentialMovement(num)
							return False
						elif i.movement(movement[0], int(movement[1]), chessObjects):
							return True
		essentialMovement(num)
	else:
		print("______________BLACK_______________")
		move = input("LOCATION TO MOVE: \n")
		for i in blackObjects:
			if i.getLocation() == move:
				while(True):
					movement = input("MOVE TO WHERE: \n")
					if len(movement) == 2 or movement == 'change':
						if movement == 'change':
							essentialMovement(num)
							return True
						elif i.movement(movement[0], int(movement[1]), chessObjects):
							return True
		essentialMovement(num)


class AI:
	color = ''
	
	def __init__(self, color):
		self.color = color
		
	def movement(self):
		pass

gridDevelopment()
inititation()
mun = 0

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill((0,0,0))
	landscape()
	for i in whiteObjects:
		i.redraw()
		if i.check():
			done = True
	for i in blackObjects:
		i.redraw()
		if i.check():
			done = True
	pygame.display.flip()
	essentialMovement(mun)
	mun+=1

	
	
