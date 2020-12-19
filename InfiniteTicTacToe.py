import tkinter as TK

fullLoop = True

while fullLoop:
	typeLoop = True
	while typeLoop:
		print('type a number and a grid will be generated based on it')
		while True:
			try:
				grid = int(input('> '))
			
			except ValueError:
				print("it can't contain letters nor decimal values")
			else:
				break
		
		if grid < 3:
			print ('you can not have a grid with fewer squares than 3x3')
			grid = 3
			break
			
		if grid >= 3 and grid < 20:
			break
		
		if grid >= 20:
			confirmLoop = True
			print('WARNING: big grids might have a hard time being created and will probably have performance issues')
			print('do you wish to proceed anyway?')
			while confirmLoop:
				proceed = input('> ')
				
				if proceed.lower() == 'yes' or proceed.lower() == 'y':
					typeLoop = False
					break
				
				elif proceed.lower() == 'no' or proceed.lower() == 'n' :
					break
				else:
					print('type "yes" or "no"')
	
	num = 0
	column = 0
	row = 0
	Playable = True
	won = False
	
	a = []
	playsX = []
	playsO = []
	totalPlays = 0

	root = TK.Tk()
	
	root.config(background = 'Grey')
	root.title('{}x{} Tic Tac Toe'.format(grid, grid))
	
	txt = '  '
	
	class LABEL:
		turn = 'X'
		def __init__ (self, num, column, row, txt, button, Playable, ):
			self.num = num
			self.column = column
			self.row = row
			self.txt = txt
			self.button = button
			self.Playable = Playable
		
		def myClick(self):
			global turnLabel, won, totalPlays, num
			if LABEL.turn == 'X' and self.Playable == True and won == False:
				totalPlays += 1
				self.button.config(text = 'X', fg = 'Blue', bg = 'Light Grey')
				LABEL.turn = 'O'
				turnLabel.config(text = "{}'s turn".format(LABEL.turn))
				playsX.append((self.row, self.column))
				self.Playable = False
				if (
					#Big Cross
					(self.row - 1, self.column) in playsX
					and (self.row - 2, self.column) in playsX) or (
					
					(self.row, self.column - 1) in playsX
					and (self.row, self.column - 2) in playsX) or (
					
					(self.row + 1, self.column) in playsX
					and (self.row + 2, self.column) in playsX) or (
					
					(self.row, self.column + 1) in playsX
					and (self.row, self.column + 2) in playsX) or (
					
					#Small Cross
					(self.row - 1, self.column) in playsX
					and (self.row + 1, self.column) in playsX) or (
					
					(self.row, self.column - 1) in playsX
					and (self.row, self.column + 1) in playsX) or (
					
					#Big X
					(self.row - 1, self.column - 1) in playsX
					and (self.row - 2, self.column - 2) in playsX) or (

					(self.row + 1, self.column + 1) in playsX
					and (self.row + 2, self.column + 2) in playsX) or (
					
					(self.row - 1, self.column + 1) in playsX
					and (self.row - 2, self.column + 2) in playsX) or (

					(self.row + 1, self.column - 1) in playsX
					and (self.row + 2, self.column - 2) in playsX) or (
					
					#Small X
					(self.row - 1, self.column - 1) in playsX
					and (self.row + 1, self.column + 1) in playsX) or (

					(self.row - 1, self.column + 1) in playsX
					and (self.row + 1, self.column - 1) in playsX) :
					
					won = True
					result = TK.Tk()
					xWinnerLabel = TK.Label(result, text = "X WINS",
									padx = 150/grid,
									pady = 150/grid,
									fg = 'Black',
									bg = 'Light Grey',
									font = 'verdana {} bold'.format(int(150/grid))).pack(expand = True)
					result.config(background = 'Light Grey')
					result.title('CONGRATULATIONS X')
					result.mainloop()
		
			elif LABEL.turn == 'O' and self.Playable == True and won == False:
				totalPlays += 1
				self.button.config(text = 'O', fg = 'Red', bg = 'Light Grey')
				LABEL.turn = 'X'
				turnLabel.config(text = "{}'s turn".format(LABEL.turn))
				playsO.append((self.row, self.column))
				self.Playable = False
				if (
					#Big Cross
					(self.row - 1, self.column) in playsO
					and (self.row - 2, self.column) in playsO) or (
					
					(self.row, self.column - 1) in playsO
					and (self.row, self.column - 2) in playsO) or (
					
					(self.row + 1, self.column) in playsO
					and (self.row + 2, self.column) in playsO) or (
					
					(self.row, self.column + 1) in playsO
					and (self.row, self.column + 2) in playsO) or (
					
					#Small Cross
					(self.row - 1, self.column) in playsO
					and (self.row + 1, self.column) in playsO) or (
					
					(self.row, self.column - 1) in playsO
					and (self.row, self.column + 1) in playsO) or (
					
					#Big X
					(self.row - 1, self.column - 1) in playsO
					and (self.row - 2, self.column - 2) in playsO) or (

					(self.row + 1, self.column + 1) in playsO
					and (self.row + 2, self.column + 2) in playsO) or (
					
					(self.row - 1, self.column + 1) in playsO
					and (self.row - 2, self.column + 2) in playsO) or (

					(self.row + 1, self.column - 1) in playsO
					and (self.row + 2, self.column - 2) in playsO) or (
					
					#Small X
					(self.row - 1, self.column - 1) in playsO
					and (self.row + 1, self.column + 1) in playsO) or (

					(self.row - 1, self.column + 1) in playsO
					and (self.row + 1, self.column - 1) in playsO) :
					
					won = True
					result = TK.Tk()
					oWinnerLabel = TK.Label(result, text = "O WINS",
									padx = 150/grid,
									pady = 150/grid,
									fg = 'Black',
									bg = 'Light Grey',
									font = 'verdana {} bold'.format(int(150/grid))).pack(expand = True)
					result.config(background = 'Light Grey')
					result.title('CONGRATULATIONS O')
					result.mainloop()
		
			if totalPlays == num:
				result = TK.Tk()
				BothLose = TK.Label(result, text = "YOU LOST",
									padx = 150/grid,
									pady = 150/grid,
									fg = 'Black',
									bg = 'Light Grey',
									font = 'verdana {} bold'.format(int(150/grid))).pack(expand = True)
				result.config(background = 'Light Grey')
				result.title("You're both terrible")
				result.mainloop()
				
		def myButton(self):
			self.num += 1
			self.button = TK.Button(
									root, text = self.txt, command = self.myClick,
									padx = 150/grid,
									pady = 150/grid,
									fg = 'Black',
									bg = 'Grey',
									font = 'verdana {} bold'.format(int(150/grid))
									)
			
			self.button.grid(row = self.row, column = self.column)

	
	for c in range (0, grid):
		row = 0
		for labeling in range(0, grid):
			a.append(num)
			a[num] = LABEL(num, column, row, txt, 0, Playable)
			a[num].myButton()
			num += 1
			row += 1
		column += 1
	
	def restart():
		global num, turnLabel, won, totalPlays
		num = 0
		won = False
		totalPlays = 0
		for items in a:
			a[num].button.config(text = a[num].txt, fg = 'Black', bg = 'Grey')
			a[num].Playable = True
			num += 1
		playsO.clear()
		playsX.clear()
		
		LABEL.turn = 'X'
		turnLabel.config(text = "{}'s turn".format(LABEL.turn))
		
	
	exitButton = TK.Button(root, text = '   exit   ', command = root.destroy,
									padx = 150/grid,
									pady = 150/grid,
									fg = 'Black',
									bg = 'Grey',
									font = 'verdana {} bold'.format(int(150/grid)))
	
	restartButton = TK.Button(root, text = 'restart', command = restart,
									padx = 150/grid,
									pady = 150/grid,
									fg = 'Black',
									bg = 'Grey',
									font = 'verdana {} bold'.format(int(150/grid)))
	
	turnLabel = TK.Label(root, text = "{}'s turn".format(LABEL.turn),
									padx = 150/grid,
									pady = 150/grid,
									fg = 'Black',
									bg = 'Grey',
									font = 'verdana {} bold'.format(int(150/grid)))
	
	turnLabel.grid(row = 0, column = column)
	exitButton.grid(row = row - 1, column = column)
	restartButton.grid(row = row - 2, column = column)
	
	root.mainloop()
