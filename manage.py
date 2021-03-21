from flask_script import Manager
from aplicacion.index  import app, db
from aplicacion.models import *

manager = Manager(app)
app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
#app.config['SECRET_KEY'] = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"

@manager.command
def create_tables():
    "Create relational database table"
    db.create_all()

@manager.command
def drop_tables():
    "drop relational database table"
    db.drop_all()
    
if __name__ == "__main__":
    manager.run()