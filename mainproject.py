from app import app, db
#it works anyway in flask shell but explicit is better than implicit so..
import sqlalchemy as sa
import sqlalchemy.orm as so
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'sa': sa, 'so': so, 'User': User, 'Post': Post}

