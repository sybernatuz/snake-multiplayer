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
		self.bind('<d>', lambda event : game.set_direction(event, 1, 'right'))
		self.bind('<q>', lambda event : game.set_direction(event, 1, 'left'))
		self.bind('<z>', lambda event : game.set_direction(event, 1, 'up'))
		self.bind('<s>', lambda event : game.set_direction(event, 1, 'down'))

		self.bind('<m>', lambda event : game.set_direction(event, 2, 'right'))
		self.bind('<k>', lambda event : game.set_direction(event, 2, 'left'))
		self.bind('<o>', lambda event : game.set_direction(event, 2, 'up'))
		self.bind('<l>', lambda event : game.set_direction(event, 2, 'down'))

		self.bind('<Right>', lambda event : game.set_direction(event, 3, 'right'))
		self.bind('<Left>', lambda event : game.set_direction(event, 3, 'left'))
		self.bind('<Up>', lambda event : game.set_direction(event, 3, 'up'))
		self.bind('<Down>', lambda event : game.set_direction(event, 3, 'down'))

		self.bind('<j>', lambda event : game.set_direction(event, 4, 'right'))
		self.bind('<g>', lambda event : game.set_direction(event, 4, 'left'))
		self.bind('<y>', lambda event : game.set_direction(event, 4, 'up'))
		self.bind('<h>', lambda event : game.set_direction(event, 4, 'down'))

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
		self.b1.pack()
		self.b1.place(x=20, y=545)

		self.b2 = Button(self, text='Quitter', command=self.destroy, 
	                bg='black' , fg='green')
		self.b2.pack()
		self.b2.place(x=430, y=545)

	""" set the window options """
	def initialize_window_options(self):
		self.resizable(0, 0)
		self.geometry("500x600")
		self.pack_propagate(0)

	""" Display button to make the choise of the players number """
	def number_of_players(self, game):
		self.text = Label(self, text="Nombre de joueurs", fg='green')
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

	""" Add the elements to permit at the user to add a winner """
	def insert_winner_input(self, game):
		self.winner_text = Label(self, text="Nom du vainqeur" , fg='green')
		self.winner_text.pack(side=LEFT, padx=5, pady=5)
		self.winner_text.place(x=100, y=300)

		self.winner_input = Entry(self, width=10)
		self.winner_input.pack()
		self.winner_input.place(x=200, y=300)
		self.winner_button = Button(self, text='Valider', 
									command=lambda: [
														game.insert_win(self.winner_input.get()),
														self.destroy_winner_elements_on_click()
													],
					                bg='black' , fg='green')
		self.winner_button.pack()
		self.winner_button.place(x=270, y=295)

	""" Destroy the elements on references with the number of player when the button is clicked """
	def destroy_number_of_players_elements_on_click(self):
		for button in self.buttons:
			button.destroy()
		self.text.destroy()

	""" Destroy the elements on references with the winner when the button is clicked """
	def destroy_winner_elements_on_click(self):
		self.winner_input.destroy()
		self.winner_button.destroy()
		self.winner_text.destroy()

	""" Add a button to play again """
	def add_play_again_button(self, game):
		button = Button(self, text='Relancer', 
					command=lambda: game.reset_game(),
	                bg='black' , fg='green')
		button.pack(side=LEFT, padx=5, pady=5)
		button.place(x=20, y=545)

	""" Display the score board with the players and theirs vicotries"""
	def display_score_board(self, players):
		self.can.destroy()
		text_board = Label(self, text="Tableau des scores" , fg='green')
		text_board.pack(side=TOP, padx=5, pady=5)
		board = ttk.Treeview(self, columns=("win"))
		board.column("win", width=100)
		board.heading("win", text="Victoires")

		for player, win in players:
			board.insert("", 0, text=player, values=(win))

		board.pack(side=TOP, padx=5, pady=5)

	""" Display the winner color"""
	def display_winner(self, winner_color):
		text_board = Label(self, text=winner_color + " gagne" , fg='green', font=("Arial", 20))
		text_board.pack()
		text_board.place(x=180, y=400)
	
	""" Display the number of apples tacked when only one player"""
	def display_apples_tacked_number(self, game):
		text_board = Label(self, text=str(game.apple.count) + " apples tacked" , fg='green', font=("Arial", 20))
		text_board.pack()
		text_board.place(x=150, y=540)
