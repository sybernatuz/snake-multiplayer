from tkinter import *

class Window(Tk):

	""" initialize the new apple with random coordinates """
	def __init__(self, game):
		Tk.__init__(self)
		self.can = self.initialize_window(game)
		self.initialize_movement(game)

	""" Initialize players key binding """
	def initialize_movement(self, game):
		self.bind('<d>', lambda event : game.set_direction(event, 1, 'droite'))
		self.bind('<q>', lambda event : game.set_direction(event, 1, 'gauche'))
		self.bind('<z>', lambda event : game.set_direction(event, 1, 'haut'))
		self.bind('<s>', lambda event : game.set_direction(event, 1, 'bas'))

		self.bind('<m>', lambda event : game.set_direction(event, 2, 'droite'))
		self.bind('<k>', lambda event : game.set_direction(event, 2, 'gauche'))
		self.bind('<o>', lambda event : game.set_direction(event, 2, 'haut'))
		self.bind('<l>', lambda event : game.set_direction(event, 2, 'bas'))

		self.bind('<Right>', lambda event : game.set_direction(event, 3, 'droite'))
		self.bind('<Left>', lambda event : game.set_direction(event, 3, 'gauche'))
		self.bind('<Up>', lambda event : game.set_direction(event, 3, 'haut'))
		self.bind('<Down>', lambda event : game.set_direction(event, 3, 'bas'))

		self.bind('<j>', lambda event : game.set_direction(event, 4, 'droite'))
		self.bind('<g>', lambda event : game.set_direction(event, 4, 'gauche'))
		self.bind('<y>', lambda event : game.set_direction(event, 4, 'haut'))
		self.bind('<h>', lambda event : game.set_direction(event, 4, 'bas'))

	""" create the window with buttons and text """
	def initialize_window(self, game):
		can = Canvas(self, width=500, height=500, bg='black')
		can.pack(side=TOP, padx=5, pady=5)

		b1 = Button(self, text='Lancer', command=lambda: self.number_of_players(game),
	                bg='black' , fg='green')
		b1.pack(side=LEFT, padx=5, pady=5)
		 
		b2 = Button(self, text='Quitter', command=self.destroy, 
	                bg='black' , fg='green')
		b2.pack(side=RIGHT, padx=5, pady=5)
		 
		return can

	""" Display button to make the choise of the players number """
	def number_of_players(self, game):
		tex1 = Label(self, text="Nombre de joueurs", bg='black' , fg='green')
		tex1.pack(side=LEFT, padx=25, pady=5)
		for i in range(1, 5):
			Button(self, text=i, command=lambda i=i: game.new_game(i), 
                        bg='black' , fg='green').pack(side=LEFT, padx=5, pady=5)

