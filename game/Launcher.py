from game.models.Snake import Snake
from game.models.Apple import Apple
from game.models.Window import Window
from game.database.SqlLiteManager import *

class Launcher:

    """ Initialize the game with all the snakes and their directions """
    def __init__(self):
        self.flag = 1
        self.one_player = False
        self.directions = {
            1 : 'down',
            2 : 'up',
            3 : 'right',
            4 : 'left'
        }
        self.snakes = {
            1 : Snake(245, 25, 1),
            2 : Snake(245, 475, 2),
            3 : Snake(25, 245, 3),
            4 : Snake(475, 245, 4)
        }
        self.apple = Apple()
        self.sqlManager = SqlLiteManager()
        self.window = Window(self)
        self.apple.add_apple(self.window.can, None, self.one_player)
        self.window.mainloop()


    """ Move every snakes who are alive """
    def move(self):
        self.window.can.delete('all')
        temp_snakes = self.snakes.copy()
        for key in self.snakes:
            self.move_snake(self.snakes[key], self.directions[key], self.snakes, temp_snakes)
        self.snakes = temp_snakes
        if self.flag == 1:
            self.window.after(60, self.move)
        else:
            winner_color = list(self.snakes.values())[0].get_head_color() if len(self.snakes) > 0 else None 
            self.game_over(winner_color)     

    """ Display the element when the game is over """
    def game_over(self, winner_color):
        self.window.add_play_again_button(self)
        if self.one_player != True:
            self.window.display_score_board(self.sqlManager.find_all())
            self.window.display_winner(winner_color)
            self.window.insert_winner_input(self)
        else :
            self.window.display_apples_tacked_number(self)

    """ Destroy the current window and make an ohter"""
    def reset_game(self):
        self.window.destroy()
        self.__init__()

    """ Move the snake according to the direction
    and add a the apple """
    def move_snake(self, snake, direction, snakes, temp_snakes):
        snake.display_snake_body(self.window.can)
        snake.set_position(direction)
        snake.display_snake_head(self.window.can)
        self.flag = snake.check_collision(self.snakes, self.flag, temp_snakes)
        self.apple.add_apple(self.window.can, snake, self.one_player)

    """ Start the game """
    def new_game(self, players_number):
        self.set_players_number(players_number)
        self.move()

    """ Set the players number by delete snakes according to the number"""
    def set_players_number(self, players_number):
        if players_number < 4:
            del self.snakes[4]
        if players_number < 3:
            del self.snakes[3]
        if players_number < 2:
            del self.snakes[2]
        if players_number == 1:
            self.one_player = True
    	
    """ Change the snake user direction when press a key """
    def set_direction(self, event, player, direction):
        self.directions[player] = direction

    """ Add the winner name to SQLLite"""
    def insert_win(self, player):
        self.sqlManager.insert(player)

