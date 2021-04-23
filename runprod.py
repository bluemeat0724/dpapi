from app import create_app, db
from app.models import DictData

app = create_app('production')

@app.shell_context_processor
def make_shell_context():
    return dict(db=db,DictData=DictData)

if __name__ == '__main__':
    app.run(port=8889,host='0.0.0.0')