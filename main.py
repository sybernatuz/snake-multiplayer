from tkinter import *
from random import randrange
 
def move():
    global x
    global y,pX,pY
    global snake1, snake2
    can.delete('all')
    moveSnake(snake1, 1)
    moveSnake(snake2, 2)
    if flag != 0:
        fen.after(60, move)

def moveSnake(snake, player):
    i=len(snake)-1
    j=0
    while i > 0:
        snake[i][0]=snake[i-1][0]
        snake[i][1]=snake[i-1][1]
        can.create_oval(snake[i][0], snake[i][1], snake[i][0] +10, snake[i][1]+10,outline='green', fill='black') 
        i=i-1
 
    can.create_rectangle(pX, pY, pX+5, pY+5, outline='green', fill='black')
     
    if direction  == 'gauche' + str(player):
        snake[0][0]  = snake[0][0] - dx
        if snake[0][0] < 0:
            snake[0][0] = 493
    elif direction  == 'droite' + str(player):
        snake[0][0]  = snake[0][0] + dx
        if snake[0][0] > 493:
            snake[0][0] = 0
    elif direction  == 'haut' + str(player):
        snake[0][1]  = snake[0][1] - dy
        if snake[0][1] < 0:
            snake[0][1] = 493
    elif direction  == 'bas' + str(player):
        snake[0][1]  = snake[0][1] + dy
        if snake[0][1] > 493:
            snake[0][1] = 0
    can.create_oval(snake[0][0], snake[0][1], snake[0][0]+10, snake[0][1]+10,outline='green', fill='blue')
    test(snake)
    test(snake)
    
def newGame():
    global pX,pY
    global flag
    if flag == 0:
        flag = 1
    move()
 

def test(snake):
    global pomme
    global x,y,pX,pY
    if snake[1][0]>pX-7 and  snake[1][0]<pX+7:        
        if snake[1][1]>pY-7 and snake[1][1]<pY+7:
            #On remet une pomme au hasard
            pX = randrange(5, 495)
            pY = randrange(5, 495)
            can.coords(pomme,pX, pY, pX+5, pY+5)
            #On joute un nouveau point au serpent
            snake.append([0,0])
            
def left(event, player):
    global direction
    direction = 'gauche' + str(player)
         
def right(event, player):
    global direction
    direction = 'droite' + str(player)
         
def up(event, player):
    global direction
    direction = 'haut' + str(player)
         
def down(event, player):
    global direction
    direction = 'bas' + str(player)
    
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
direction = 'haut'
snake1=[[x,y],[x+2.5,y+2.5],[x+5,y+5],[0,0]]
snake2=[[x,y],[x+2.5,y+2.5],[x+5,y+5],[0,0]]
 
pX = randrange(5, 495)
pY = randrange(5, 495)
 
fen = Tk()
can = Canvas(fen, width=500, height=500, bg='black')
can.pack(side=TOP, padx=5, pady=5) 
 
oval_snake_player1_head = can.create_oval(snake1[1][0], snake1[1][1], snake1[1][0] +10, snake1[1][1]+10, outline='green', fill='red')
oval_snake_palyer1  = can.create_oval(snake1[0][0], snake1[0][1], snake1[0][0]+10, snake1[0][1]+10, outline='green', fill='green')

oval_snake_player2_head = can.create_oval(snake2[1][0], snake2[1][1], snake2[1][0] +10, snake2[1][1]+10, outline='blue', fill='orange')
oval_snake_palyer2  = can.create_oval(snake2[0][0], snake2[0][1], snake2[0][0]+10, snake2[0][1]+10, outline='blue', fill='blue')

pomme = can.create_rectangle(pX, pY, pX+5, pY+5, outline='green', fill='black')
 
b1 = Button(fen, text='Lancer', command=newGame, bg='black' , fg='green')
b1.pack(side=LEFT, padx=5, pady=5)
 
b2 = Button(fen, text='Quitter', command=fen.destroy, bg='black' , fg='green')
b2.pack(side=RIGHT, padx=5, pady =5)
 
tex1 = Label(fen, text="Cliquez sur 'New Game' pour commencer le jeu.", bg='black' , fg='green')
tex1.pack(padx=0, pady=11)

initializeMovement(fen)

fen.mainloop()


