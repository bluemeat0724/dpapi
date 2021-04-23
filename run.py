from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app.models import DictData

app = create_app('default')
manager = Manager(app)

Migrate(app,db)
manager.add_command('db',MigrateCommand)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db,DictData=DictData)

if __name__ == '__main__':
    manager.run()