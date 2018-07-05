from game.models.Snake import Snake
from game.models.Apple import Apple
from game.models.Window import Window

class Launcher:

    """ Initialize the game with all the snakes and their directions """
    def __init__(self):
        self.flag = 1
        self.directions = {
            1 : 'bas',
            2 : 'haut',
            3 : 'droite',
            4 : 'gauche'
        }
        self.snakes = {
            1 : Snake(245, 25, 1),
            2 : Snake(245, 475, 2),
            3 : Snake(25, 245, 3),
            4 : Snake(475, 245, 4)
        }
        self.apple = Apple()
        self.window = Window(self)
        self.apple.add_apple(self.window.can, None)
        self.window.mainloop()

    """ Move every snakes who are alive """
    def move(self):
        self.window.can.delete('all')
        temp_snakes = self.snakes.copy()
        for key in self.snakes:
            self.move_snake(self.snakes[key], self.directions[key], self.snakes, temp_snakes)
        self.snakes = temp_snakes
        if self.flag != 0:
            self.window.after(60, self.move)
        else:
            self.window.add_play_again_button(self)

    """ Move the snake according to the direction
    and add a the apple """
    def move_snake(self, snake, direction, snakes, temp_snakes):
        snake.display_snake_body(self.window.can)
        snake.set_position(direction)
        snake.display_snake_head(self.window.can)
        self.flag = snake.check_collision(self.snakes, self.flag, temp_snakes)
        self.apple.add_apple(self.window.can, snake)

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
    	
    """ Change the snake user direction when press a key """
    def set_direction(self, event, player, direction):
        self.directions[player] = direction

