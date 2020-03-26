from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from app import my_db

migrate = Migrate(app,my_db)
manager = Manager(app)
manager.add_command("my_db",MigrateCommand)

if __name__ == '__main__':
	manager.run()