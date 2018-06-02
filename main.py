from tkinter import *
from random import randrange
 
def move():
    global x
    global y,pX,pY
    global snake_player1, snake_player2
    can.delete('all')
    moveSnake(snake_player1, 1, direction_player1)
    moveSnake(snake_player2, 2, direction_player2)
    if flag != 0:
        fen.after(60, move)

def moveSnake(snake, player, direction):
    i=len(snake)-1
    j=0
    while i > 0:
        snake[i][0]=snake[i-1][0]
        snake[i][1]=snake[i-1][1]
        can.create_oval(snake[i][0], snake[i][1], snake[i][0] +10, snake[i][1]+10,outline='green', fill='black') 
        i=i-1
 
    can.create_rectangle(pX, pY, pX+5, pY+5, outline='green', fill='black')
     
    if direction  == 'gauche':
        snake[0][0]  = snake[0][0] - dx
        if snake[0][0] < 0:
            snake[0][0] = 493
    elif direction  == 'droite':
        snake[0][0]  = snake[0][0] + dx
        if snake[0][0] > 493:
            snake[0][0] = 0
    elif direction  == 'haut':
        snake[0][1]  = snake[0][1] - dy
        if snake[0][1] < 0:
            snake[0][1] = 493
    elif direction  == 'bas':
        snake[0][1]  = snake[0][1] + dy
        if snake[0][1] > 493:
            snake[0][1] = 0
    can.create_oval(snake[0][0], snake[0][1], snake[0][0]+10, snake[0][1]+10,outline='green', fill= 'red' if player==1 else 'blue')
    isApleTacked(snake)
    
def newGame():
    global pX,pY
    global flag
    if flag == 0:
        flag = 1
    move()
 

def isApleTacked(snake):
    global pomme
    global x,y,pX,pY
    if snake[1][0]>pX-7 and snake[1][0]<pX+7:        
        if snake[1][1]>pY-7 and snake[1][1]<pY+7:
            #On remet une pomme au hasard
            pX = randrange(5, 495)
            pY = randrange(5, 495)
            can.coords(pomme,pX , pY, pX+5, pY+5)
            #On ajoute un nouveau point au serpent
            snake.append([0,0])
            
def left(event, player):
    global direction_player1, direction_player2
    if (player == 1):
        direction_player1 = 'gauche'
    else:
        direction_player2 = 'gauche'
         
def right(event, player):
    global direction_player1, direction_player2
    if (player == 1):
        direction_player1 = 'droite'
    else:
        direction_player2 = 'droite'
         
def up(event, player):
    global direction_player1, direction_player2
    if (player == 1):
        direction_player1 = 'haut'
    else:
        direction_player2 = 'haut'
         
def down(event, player):
    global direction_player1, direction_player2
    if (player == 1):
        direction_player1 = 'bas'
    else:
        direction_player2 = 'bas'
    
def initializeMovement(fen):
    fen.bind('<d>', lambda event : right(event, 1))
    fen.bind('<q>', lambda event : left(event, 1))
    fen.bind('<z>', lambda event : up(event, 1))
    fen.bind('<s>', lambda event : down(event, 1))

    fen.bind('<l>', lambda event : right(event, 2))
    fen.bind('<j>', lambda event : left(event, 2))
    fen.bind('<i>', lambda event : up(event, 2))
    fen.bind('<k>', lambda event : down(event, 2))

x = 245
y = 24        
dx, dy = 10, 10
flag = 0
direction_player1 = 'haut'
direction_player2 = 'bas'
snake_player1=[[x,y],[x+2.5,y+2.5],[x+5,y+5],[0,0]]
snake_player2=[[x,y],[x+2.5,y+2.5],[x+5,y+5],[0,0]]
 
pX = randrange(5, 495)
pY = randrange(5, 495)
 
fen = Tk()
can = Canvas(fen, width=500, height=500, bg='black')
can.pack(side=TOP, padx=5, pady=5)

pomme = can.create_rectangle(pX, pY, pX+5, pY+5, outline='green', fill='black')
 
b1 = Button(fen, text='Lancer', command=newGame, bg='black' , fg='green')
b1.pack(side=LEFT, padx=5, pady=5)
 
b2 = Button(fen, text='Quitter', command=fen.destroy, bg='black' , fg='green')
b2.pack(side=RIGHT, padx=5, pady =5)
 
tex1 = Label(fen, text="Cliquez sur 'New Game' pour commencer le jeu.", bg='black' , fg='green')
tex1.pack(padx=0, pady=11)

initializeMovement(fen)

fen.mainloop()


