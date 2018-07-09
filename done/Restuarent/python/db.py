import sqlite3

class dataaccess():
	def __init__(self):
		self.DB_connect()
		self.create_Account()
		self.id()

	def DB_connect(self):
		self.conn=sqlite3.connect("data.db")
		self.con=self.conn.cursor()

	def create_Account(self):
		self.con.execute(''' CREATE TABLE IF NOT EXISTS ACCOUNT(ID INTEGER PRIMARY KEY,
			NAME TEXT,
			BALANCE INTEGER)''')
		self.con.execute("SELECT COUNT (*) FROM ACCOUNT")
		if self.con.fetchone()[0]==0:
			self.con.execute("INSERT INTO ACCOUNT VALUES(1,'Shafeeq',99999)")
			self.con.execute("INSERT INTO ACCOUNT VALUES(2,'Sharanya',89999)") 
			self.con.execute("INSERT INTO ACCOUNT VALUES(3,'aiswarya',70000)")
			self.con.execute("INSERT INTO ACCOUNT VALUES(4,'athira',65000)")

		self.conn.commit()

	def id(self):
		self.con.execute('''CREATE TABLE IF NOT EXIST ID(SINO INTEGER PRIMARY KEY,NUM INTEGER)''')
		self.con.execute("SELECT COUNT (*) FROM ID")
		if self.con.fetchone()[0]==0:
			self.con.execute("INSERT INTO ID VALUES(1,0)")
		self.conn.commit()




