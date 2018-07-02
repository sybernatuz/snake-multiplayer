from tkinter import *
from models.snake import Snake
from models.apple import Apple
 
def move():
    can.delete('all')
    move_snake(snake_player1, direction_player1)
    move_snake(snake_player2, direction_player2)
    if flag != 0:
        fen.after(60, move)

def move_snake(snake, direction):
    global flag
    snake.display_snake_body(can)
    snake.set_position(direction, dx, dy)
    snake.display_snake_head(can)
    flag = snake_player1.check_collision(snake_player2.snake, flag)
    if flag != 0:
        flag = snake_player2.check_collision(snake_player1.snake, flag)
    apple.add_apple(can, snake)
	
def new_game():
    global flag
    if flag == 0:
        flag = 1
    move()

def set_direction(event, player, direction):
    global direction_player1, direction_player2
    if (player == 1):
        direction_player1 = direction
    else:
        direction_player2 = direction
    
def initialize_movement(fen):
    fen.bind('<d>', lambda event : set_direction(event, 1, 'droite'))
    fen.bind('<q>', lambda event : set_direction(event, 1, 'gauche'))
    fen.bind('<z>', lambda event : set_direction(event, 1, 'haut'))
    fen.bind('<s>', lambda event : set_direction(event, 1, 'bas'))

    fen.bind('<l>', lambda event : set_direction(event, 2, 'droite'))
    fen.bind('<j>', lambda event : set_direction(event, 2, 'gauche'))
    fen.bind('<i>', lambda event : set_direction(event, 2, 'haut'))
    fen.bind('<k>', lambda event : set_direction(event, 2, 'bas'))

dx, dy = 10, 10
flag = 0
direction_player1 = 'bas'
direction_player2 = 'haut'
snake_player1 = Snake(245, 25, 1)
snake_player2 = Snake(245, 475, 2)
apple = Apple()

 
fen = Tk()
can = Canvas(fen, width=500, height=500, bg='black')
can.pack(side=TOP, padx=5, pady=5)

b1 = Button(fen, text='Lancer', command=new_game, bg='black' , fg='green')
b1.pack(side=LEFT, padx=5, pady=5)
 
b2 = Button(fen, text='Quitter', command=fen.destroy, bg='black' , fg='green')
b2.pack(side=RIGHT, padx=5, pady =5)
 
tex1 = Label(fen, text="Cliquez sur 'New Game' pour commencer le jeu.", 
			 bg='black' , fg='green')
tex1.pack(padx=0, pady=11)

apple.add_apple(can, None)

initialize_movement(fen)

fen.mainloop()


