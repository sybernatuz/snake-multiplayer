from tkinter import *
from tkinter import ttk

class Window(Tk):

	""" initialize the new apple with random coordinates """
	def __init__(self, game):
		Tk.__init__(self)
		self.initialize_window_options()
		self.initialize_window_elements(game)
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
	def initialize_window_elements(self, game):
		self.can = Canvas(self, width=500, height=500, bg='black')
		self.can.pack(side=TOP, padx=5, pady=5)

		self.b1 = Button(self, text='Lancer', 
					command=lambda: [
										self.number_of_players(game), 
										self.b1.destroy()
									],
	                bg='black', fg='green')
		self.b1.pack(side=LEFT, padx=5, pady=5)
		 
		self.b2 = Button(self, text='Quitter', command=self.destroy, 
	                bg='black' , fg='green')
		self.b2.pack(side=RIGHT, padx=5, pady=5)

	""" set the window options """
	def initialize_window_options(self):
		self.resizable(0, 0)
		self.geometry("500x600")
		self.pack_propagate(0)

	""" Display button to make the choise of the players number """
	def number_of_players(self, game):
		self.text = Label(self, text="Nombre de joueurs", bg='black' , fg='green')
		self.text.pack(side=LEFT, padx=5, pady=5)
		self.buttons = []
		for i in range(1, 5):
			b = Button(self, text=i, 
						command=lambda i=i: [
												game.new_game(i), 
												self.destroy_number_of_players_elements_on_click()
											], 
                        bg='black' , fg='green')
			b.pack(side=LEFT, padx=5, pady=5)
			self.buttons.append(b)

	def insert_winner_input(self, game):
		self.can.destroy()
		self.winner_input = Entry(self, width=10)
		self.winner_input.pack(side=TOP, padx=5, pady=5)
		self.winner_button = Button(self, text='Valider', 
									command=lambda: [
														game.insert_win(self.winner_input.get()),
														self.destroy_winner_elements_on_click()
													],
					                bg='black' , fg='green')
		self.winner_button.pack(side=TOP, padx=5, pady=5)


	def destroy_number_of_players_elements_on_click(self):
		for button in self.buttons:
			button.destroy()
		self.text.destroy()

	def destroy_winner_elements_on_click(self):
		self.winner_input.destroy()
		self.winner_button.destroy()

	def add_play_again_button(self, game):
		button = Button(self, text='Relancer', 
					command=lambda: self.reset_game(game),
	                bg='black' , fg='green')
		button.pack(side=LEFT, padx=5, pady=5)

	def reset_game(self, game):
		self.destroy()
		game.__init__()

	def display_score_board(self, players):
		self.board = ttk.Treeview(self, columns=("win"))
		self.board.column("win", width=100)
		self.board.heading("win", text="Victoires")

		for player, win in players:
			self.board.insert("", 0, text=player, values=(win))

		self.board.pack(side=TOP, padx=5, pady=5)