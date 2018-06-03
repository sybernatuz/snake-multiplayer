from tkinter import *
from random import randrange
 
def move():
    can.delete('all')
    moveSnake(snake_player1, 1, direction_player1)
    moveSnake(snake_player2, 2, direction_player2)
    if flag != 0:
        fen.after(60, move)

def moveSnake(snake, player, direction):
    createSnakeBody(snake)
    setSnakePosition(snake, direction, dx, dy)
    createSnakeHead(snake, player)
    checkCollision(snake_player1, snake_player2, player)
    checkCollision(snake_player2, snake_player1, player)
    addApple(can, snake)

def createSnakeHead(snake, player):
    headColor = 'red' if player==1 else 'blue'
    can.create_oval(snake[0][0], snake[0][1], snake[0][0]+10, snake[0][1]+10, outline='green', fill=headColor)
    
def createSnakeBody(snake):
    for i in range(len(snake)-1, 0, -1):
        snake[i][0]=snake[i-1][0]
        snake[i][1]=snake[i-1][1]
        can.create_oval(snake[i][0], snake[i][1], snake[i][0]+10, snake[i][1]+10,outline='green', fill='black')
    
def setSnakePosition(snake, direction, dx, dy):
    if direction  == 'gauche':
        snake[0][0]  = snake[0][0] - dx
        if snake[0][0] < 0:
            snake[0][0] = 495
    elif direction  == 'droite':
        snake[0][0]  = snake[0][0] + dx
        if snake[0][0] > 495:
            snake[0][0] = 0
    elif direction  == 'haut':
        snake[0][1]  = snake[0][1] - dy
        if snake[0][1] < 0:
            snake[0][1] = 495
    elif direction  == 'bas':
        snake[0][1]  = snake[0][1] + dy
        if snake[0][1] > 495:
            snake[0][1] = 0

def newGame():
    global flag
    if flag == 0:
        flag = 1
    move()

def checkCollision(snake1, snake2, player):
    global flag
    for i in range(len(snake2)):
        check_x = snake1[0][0]>snake2[i][0]-7 and snake1[0][0]<snake2[i][0]+7
        check_y = snake1[0][1]>snake2[i][1]-7 and snake1[0][1]<snake2[i][1]+7
        if flag != 0 and check_x and check_y:
            print(str(player) + 'gagne')
            flag = 0
    
def isAppleTacked(snake):
    if snake[1][0]>pX-7 and snake[1][0]<pX+7:        
        if snake[1][1]>pY-7 and snake[1][1]<pY+7:
            #On ajoute un nouveau point au serpent
            snake.append([0,0])
            return True
    return False

def addApple(can, snake):
    if snake == None or not isAppleTacked(snake):
    	return can.create_rectangle(pX, pY, pX+5, pY+5, outline='green', fill='black')
    moveApple()

def moveApple():
    global pX,pY
    pX = randrange(5, 495)
    pY = randrange(5, 495)
    can.coords(apple, pX, pY, pX+5, pY+5)

def setDirection(event, player, direction):
    global direction_player1, direction_player2
    if (player == 1):
        direction_player1 = direction
    else:
        direction_player2 = direction
    
def initializeMovement(fen):
    fen.bind('<d>', lambda event : setDirection(event, 1, 'droite'))
    fen.bind('<q>', lambda event : setDirection(event, 1, 'gauche'))
    fen.bind('<z>', lambda event : setDirection(event, 1, 'haut'))
    fen.bind('<s>', lambda event : setDirection(event, 1, 'bas'))

    fen.bind('<l>', lambda event : setDirection(event, 2, 'droite'))
    fen.bind('<j>', lambda event : setDirection(event, 2, 'gauche'))
    fen.bind('<i>', lambda event : setDirection(event, 2, 'haut'))
    fen.bind('<k>', lambda event : setDirection(event, 2, 'bas'))

x1 = 245
y1 = 25
x2 = 245
y2 = 475
dx, dy = 10, 10
flag = 0
pX = randrange(5, 495)
pY = randrange(5, 495)
direction_player1 = 'bas'
direction_player2 = 'haut'
snake_player1=[[x1,y1],[0,0],[0,0],[0,0]]
snake_player2=[[x2,y2],[0,0],[0,0],[0,0]]
 
fen = Tk()
can = Canvas(fen, width=500, height=500, bg='black')
can.pack(side=TOP, padx=5, pady=5)

b1 = Button(fen, text='Lancer', command=newGame, bg='black' , fg='green')
b1.pack(side=LEFT, padx=5, pady=5)
 
b2 = Button(fen, text='Quitter', command=fen.destroy, bg='black' , fg='green')
b2.pack(side=RIGHT, padx=5, pady =5)
 
tex1 = Label(fen, text="Cliquez sur 'New Game' pour commencer le jeu.", bg='black' , fg='green')
tex1.pack(padx=0, pady=11)

apple = addApple(can, None)

initializeMovement(fen)

fen.mainloop()


