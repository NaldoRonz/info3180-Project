from . import my_db

class my_users(my_db.Model):

	_tablename_ = "user_profiles"

	user_id = my_db.Column(my_db.Integer, primary_key=True)
	firstname = my_db.Column(my_db.String(20), nullable=False)
	lastname = my_db.Column(my_db.String(20),nullable=False)
	gender = my_db.Column(my_db.String(10),nullable=False)
	email = my_db.Column(my_db.String(35),nullable=False, unique=True)
	location = my_db.Column(my_db.String(200),nullable=False)
	biography = my_db.Column(my_db.String(1000),nullable=False)

	def __init__(self,firstname,lastname,gender,email,location,biography):
		self.firstname = firstname
		self.lastname = lastname
		self.gender = gender
		self.email = email
		self. location = location
		self. biography = biography

	def __repr__(self):
		return f"my_users('{self.firstname}','{self.lastname}','{self.email}')"

my_db.create_all()