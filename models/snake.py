class Snake:
	
	def __init__(self, x1, y1, player):
		head = [x1,y1]
		self.snake = [
			head,
			[0,0],
			[0,0],
			[0,0]
		]
		self.player = player
		
		
	def display_snake_body(self, can):
		for i in range(len(self.snake)-1, 0, -1):
			self.snake[i][0] = self.snake[i-1][0]
			self.snake[i][1] = self.snake[i-1][1]
			can.create_oval(
				self.snake[i][0], self.snake[i][1],
				self.snake[i][0]+10, self.snake[i][1]+10,
				outline='green', fill='black')
			
	def display_snake_head(self, can):
		headColor = 'red' if self.player == 1 else 'blue'
		x = self.snake[0][0]
		y = self.snake[0][1]
		can.create_oval(x, y, x+10, y+10, outline='green', fill=headColor)
		
	def set_position(self, direction, dx, dy):
		if direction == 'gauche':
			self.snake[0][0] = self.snake[0][0] - dx
			if self.snake[0][0] < 0:
				self.snake[0][0] = 495
		elif direction == 'droite':
			self.snake[0][0] = self.snake[0][0] + dx
			if self.snake[0][0] > 495:
				self.snake[0][0] = 0
		elif direction == 'haut':
			self.snake[0][1] = self.snake[0][1] - dy
			if self.snake[0][1] < 0:
				self.snake[0][1] = 495
		elif direction == 'bas':
			self.snake[0][1] = self.snake[0][1] + dy
			if self.snake[0][1] > 495:
				self.snake[0][1] = 0
	
	def check_collision(self, snake2, flag):
		for i in range(len(snake2)):
			check_x = (self.snake[0][0] > snake2[i][0] - 7 
						and self.snake[0][0] < snake2[i][0] + 7)
			check_y = (self.snake[0][1] > snake2[i][1] - 7
						and self.snake[0][1] < snake2[i][1] + 7)
			if flag != 0 and check_x and check_y:
				print(str(self.player) + 'gagne')
				return 0
		return 1
				
	def increase_body_length(self):
		self.snake.append([0,0])