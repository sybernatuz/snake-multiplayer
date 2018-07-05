from sqlite3 import *

class SqlLiteManager:

	def __init__(self):
		self.con = connect('game/database/snake.db')
		self.c = self.con.cursor()
		self.create_table()

	def find_all(self):
		self.c.execute("SELECT * FROM snake")
		return self.c.fetchall()

	def create_table(self):
		self.c.execute("""CREATE TABLE IF NOT EXISTS snake(
			player TEXT PRIMARY KEY UNIQUE, 
			win INTEGER
		)""")
		self.con.commit()

	def insert(self, player_name):
		self.c.execute("""
			SELECT * FROM snake 
			WHERE player = ?""", 
			[player_name])

		if len(self.c.fetchall()) == 0:
			self.c.execute("""
				INSERT INTO snake(player, win) 
				VALUES(?,1)""", 
				[player_name])
		else:
			self.c.execute("""
				UPDATE snake 
				SET win = win + 1 
				WHERE player = ?""", 
				[player_name])
		self.con.commit()
