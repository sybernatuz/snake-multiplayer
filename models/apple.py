from random import randrange

class Apple:
	
	def __init__(self):
		self.x = randrange(5, 495)
		self.y = randrange(5, 495)
	
	def addApple(self, can, snake):
		if snake == None or not self.isAppleTacked(snake.snake):
			return can.create_rectangle(self.x, self.y, self.x + 5, self.y + 5, outline='green', fill='black')
		snake.increase_body_length()
		self.moveApple(can)

	def moveApple(self, can):
		self.x = randrange(5, 495)
		self.y = randrange(5, 495)
		can.coords(self, self.x, self.y, self.x + 5, self.y + 5)
	
	def isAppleTacked(self, snake):
		if snake[1][0] > self.x-7 and snake[1][0] < self.x+7:        
			if snake[1][1] > self.y-7 and snake[1][1] < self.y+7:
				return True
		return False

		