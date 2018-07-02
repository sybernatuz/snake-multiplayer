from random import randrange

class Apple:
	
	def __init__(self):
		self.x = randrange(5, 495)
		self.y = randrange(5, 495)
	
	def add_apple(self, can, snake):
		if snake == None or not self.is_apple_tacked(snake.snake):
			return can.create_rectangle(
										self.x, self.y, 
										self.x + 5, self.y + 5, 
										outline='green', fill='black')
		snake.increase_body_length()
		self.move_apple(can)

	def move_apple(self, can):
		self.x = randrange(5, 495)
		self.y = randrange(5, 495)
		can.coords(self, self.x, self.y, self.x + 5, self.y + 5)
	
	def is_apple_tacked(self, snake):
		if snake[1][0] > self.x - 7 and snake[1][0] < self.x + 7:        
			if snake[1][1] > self.y - 7 and snake[1][1] < self.y + 7:
				return True
		return False

		