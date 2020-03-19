from . import my_db

class Users(my_db.Model):

	_tablename_ = "User_Profiles"

	id = my_db.Column(my_db.Integer,primary_key=True)
	firstname = my_db.Column(my_db.String(20))
	lastname = my_db.Column(my_db.String(20))
	gender = my_db.Column(my_db.String(10))
	email = my_db.Column(my_db.String(35))
	location = my_db.Column(my_db.String(200))
	biography = my_db.Column(my_db.String(1000))

	def __init__(self,firstname,lastname,gender,email,location,biography):
		self.firstname = firstname
		self.lastname = lastname
		self.gender = gender
		self.email = email
		self. location = location
		self. biography = biography

	def __repr__(self):
		return "<Users %r>" % self.firstname
