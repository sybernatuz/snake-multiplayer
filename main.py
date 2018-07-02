from tkinter import *
from models.snake import Snake
from models.apple import Apple
 
""" Make the snakes """
def move():
    can.delete('all')
    move_snake(snake_player1, direction_player1)
    move_snake(snake_player2, direction_player2)
    if flag != 0:
        window.after(60, move)

""" Move the snake according to the direction """
def move_snake(snake, direction):
    global flag
    snake.display_snake_body(can)
    snake.set_position(direction, dx, dy)
    snake.display_snake_head(can)
    flag = snake_player1.check_collision(snake_player2, flag)
    if flag != 0:
        flag = snake_player2.check_collision(snake_player1, flag)
    apple.add_apple(can, snake)

""" Start the game """
def new_game():
    global flag
    if flag == 0:
        flag = 1
    move()
	
""" Change the snake user direction when press a key """
def set_direction(event, player, direction):
    global direction_player1, direction_player2
    if (player == 1):
        direction_player1 = direction
    else:
        direction_player2 = direction

""" Initialize players key binding """
def initialize_movement(window):
    window.bind('<d>', lambda event : set_direction(event, 1, 'droite'))
    window.bind('<q>', lambda event : set_direction(event, 1, 'gauche'))
    window.bind('<z>', lambda event : set_direction(event, 1, 'haut'))
    window.bind('<s>', lambda event : set_direction(event, 1, 'bas'))

    window.bind('<l>', lambda event : set_direction(event, 2, 'droite'))
    window.bind('<j>', lambda event : set_direction(event, 2, 'gauche'))
    window.bind('<i>', lambda event : set_direction(event, 2, 'haut'))
    window.bind('<k>', lambda event : set_direction(event, 2, 'bas'))
	
""" create the window with buttons and text """
def initialize_window(window):
	can = Canvas(window, width=500, height=500, bg='black')
	can.pack(side=TOP, padx=5, pady=5)

	b1 = Button(window, text='Lancer', command=new_game, bg='black' , fg='green')
	b1.pack(side=LEFT, padx=5, pady=5)
	 
	b2 = Button(window, text='Quitter', command=window.destroy, bg='black' , fg='green')
	b2.pack(side=RIGHT, padx=5, pady =5)
	 
	tex1 = Label(window, text="Cliquez sur 'New Game' pour commencer le jeu.", 
				 bg='black' , fg='green')
	tex1.pack(padx=0, pady=11)
	return can

dx, dy = 10, 10
flag = 0
direction_player1 = 'bas'
direction_player2 = 'haut'
snake_player1 = Snake(245, 25, 1)
snake_player2 = Snake(245, 475, 2)
apple = Apple()

window = Tk()
can = initialize_window(window)

apple.add_apple(can, None)

initialize_movement(window)

window.mainloop()


