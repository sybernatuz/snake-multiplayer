from tkinter import *
from models.snake import Snake
from models.apple import Apple
 
""" Make the snakes """
def move():
    global snakes
    can.delete('all')
    temp_snakes = snakes.copy()
    for key in snakes:
        move_snake(snakes[key], directions[key], snakes, temp_snakes)
    snakes = temp_snakes
    if flag != 0:
        window.after(60, move)

""" Move the snake according to the direction """
def move_snake(snake, direction, snakes, temp_snakes):
    global flag
    snake.display_snake_body(can)
    snake.set_position(direction, dx, dy)
    snake.display_snake_head(can)
    flag = snake.check_collision(snakes, flag, temp_snakes)
    apple.add_apple(can, snake)

""" Start the game """
def new_game(players_number):
    global flag
    set_players_number(players_number)
    initialize_movement(window, players_number)
    if flag == 0:
        flag = 1
    move()

def set_players_number(players_number):
    global directions, snakes
    if players_number < 4:
        del directions[4]
        del snakes[4]
    if players_number < 3:
        del directions[3]
        del snakes[3]
    if players_number < 2:
        del directions[2]
        del snakes[2]

def number_of_players(window):
    tex1 = Label(window, text="Nombre de joueurs", bg='black' , fg='green')
    tex1.pack(side=LEFT, padx=25, pady=5)

    b1 = Button(window, text='1', command=lambda: new_game(1), 
                bg='black' , fg='green')
    b1.pack(side=LEFT, padx=5, pady=5)

    b2 = Button(window, text='2', command=lambda: new_game(2), 
                bg='black' , fg='green')
    b2.pack(side=LEFT, padx=5, pady=5)

    b3 = Button(window, text='3', command=lambda: new_game(3),
                bg='black' , fg='green')
    b3.pack(side=LEFT, padx=5, pady=5)

    b4 = Button(window, text='4', command=lambda: new_game(4), 
                bg='black' , fg='green')
    b4.pack(side=LEFT, padx=5, pady=5)
	
""" Change the snake user direction when press a key """
def set_direction(event, player, direction):
    global directions
    directions[player] = direction

""" Initialize players key binding """
def initialize_movement(window, players_number):
    window.bind('<d>', lambda event : set_direction(event, 1, 'droite'))
    window.bind('<q>', lambda event : set_direction(event, 1, 'gauche'))
    window.bind('<z>', lambda event : set_direction(event, 1, 'haut'))
    window.bind('<s>', lambda event : set_direction(event, 1, 'bas'))

    if players_number >= 2:
        window.bind('<m>', lambda event : set_direction(event, 2, 'droite'))
        window.bind('<k>', lambda event : set_direction(event, 2, 'gauche'))
        window.bind('<o>', lambda event : set_direction(event, 2, 'haut'))
        window.bind('<l>', lambda event : set_direction(event, 2, 'bas'))

    if players_number >= 3:
        window.bind('<Right>', lambda event : set_direction(event, 3, 'droite'))
        window.bind('<Left>', lambda event : set_direction(event, 3, 'gauche'))
        window.bind('<Up>', lambda event : set_direction(event, 3, 'haut'))
        window.bind('<Down>', lambda event : set_direction(event, 3, 'bas'))

    if players_number >= 4:
        window.bind('<j>', lambda event : set_direction(event, 4, 'droite'))
        window.bind('<g>', lambda event : set_direction(event, 4, 'gauche'))
        window.bind('<y>', lambda event : set_direction(event, 4, 'haut'))
        window.bind('<h>', lambda event : set_direction(event, 4, 'bas'))
	
""" create the window with buttons and text """
def initialize_window(window):
	can = Canvas(window, width=500, height=500, bg='black')
	can.pack(side=TOP, padx=5, pady=5)

	b1 = Button(window, text='Lancer', command=lambda: number_of_players(window),
                bg='black' , fg='green')
	b1.pack(side=LEFT, padx=5, pady=5)
	 
	b2 = Button(window, text='Quitter', command=window.destroy, 
                bg='black' , fg='green')
	b2.pack(side=RIGHT, padx=5, pady=5)
	 
	return can

dx, dy = 10, 10
flag = 0
directions = {
    1 : 'bas',
    2 : 'haut',
    3 : 'droite',
    4 : 'gauche'
}
snakes = {
    1 : Snake(245, 25, 1),
    2 : Snake(245, 475, 2),
    3 : Snake(25, 245, 3),
    4 : Snake(475, 245, 4)
}
apple = Apple()

window = Tk()
can = initialize_window(window)

apple.add_apple(can, None)

window.mainloop()


