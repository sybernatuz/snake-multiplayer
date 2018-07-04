class Snake:
	
	""" Initialize a new snake with his head position and the player """
	def __init__(self, x1, y1, player):
		head = [x1,y1]
		self.snake = [
			head,
			[0,0],
			[0,0],
			[0,0]
		]
		self.player = player
		
	""" For each snake part print a circle to represent the body """
	def display_snake_body(self, can):
		for i in range(len(self.snake)-1, 0, -1):
			self.snake[i][0] = self.snake[i-1][0]
			self.snake[i][1] = self.snake[i-1][1]
			can.create_oval(
				self.snake[i][0], self.snake[i][1],
				self.snake[i][0]+10, self.snake[i][1]+10,
				outline='green', fill='black')
	
	""" Display the snake head """
	def display_snake_head(self, can):
		headColor = 'red' if self.player == 1 else 'blue'
		x = self.snake[0][0]
		y = self.snake[0][1]
		can.create_oval(x, y, x+10, y+10, outline='green', fill=headColor)
	
	""" Set the position of the snake to the border that is in 
	front when he exceeds the window size """
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
	
	""" Verify if the snake touch the second snake. 
	If he does it end the game by returning flag to 0 """
	def check_collision(self, snake2, flag):
		collision_with_other_snake = self.is_collision_with_snake_body(snake2.snake)
		collision_with_himself = self.is_collision_with_snake_body(self.snake)
		if flag == 0 or collision_with_other_snake or collision_with_himself:
			if flag != 0:
				print(str(snake2.player) + 'gagne')
			return 0
		return 1

	""" Check the collision between the self snake head and the 
	parameter wich is a snake body"""
	def is_collision_with_snake_body(self, snake):
		for i in range(1, len(snake)):
			check_x = (self.snake[0][0] > snake[i][0] - 7 
						and self.snake[0][0] < snake[i][0] + 7)
			check_y = (self.snake[0][1] > snake[i][1] - 7
						and self.snake[0][1] < snake[i][1] + 7)
			if check_x and check_y:
				return True
	
	""" Add one part to the snake body """
	def increase_body_length(self):
		self.snake.append([0,0])