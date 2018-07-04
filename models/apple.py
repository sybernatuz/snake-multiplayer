from random import randrange

class Apple:
	
	""" initialize the new apple with random coordinates """
	def __init__(self):
		self.x = randrange(5, 495)
		self.y = randrange(5, 495)
	
	""" Add an apple at the same place if she isn't tacked. 
	Else move the apple and add part to the snake """
	def add_apple(self, can, snake):
		if snake is None or not self.is_apple_tacked(snake.snake):
			return can.create_rectangle(
										self.x, self.y, 
										self.x + 5, self.y + 5, 
										outline='green', fill='black')
		snake.increase_body_length()
		self.move_apple(can)
	
	""" create new coordinate for the apple """
	def move_apple(self, can):
		self.x = randrange(5, 495)
		self.y = randrange(5, 495)
		can.coords(self, self.x, self.y, self.x + 5, self.y + 5)
	
	""" Check if the apple has been tacked by a snake """
	def is_apple_tacked(self, snake):
		if snake[1][0] > self.x - 7 and snake[1][0] < self.x + 7:        
			if snake[1][1] > self.y - 7 and snake[1][1] < self.y + 7:
				return True
		return False

		