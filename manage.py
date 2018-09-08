from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app.models import User
from app import create_app,db

app = create_app('development')

# Initializing extensions
manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)    

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User = User)

def test():
    # Run the unit test   
        import unittest
    
        tests= unittest.TestLoader().discover('tests')
        unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()

