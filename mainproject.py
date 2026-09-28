from app import app, db
#it works anyway in flask shell but explicit is better than implicit so..
import sqlalchemy as sa
import sqlalchemy.orm as so
from app.models import User, Post

# this decorator / function combo returns dictionary
# with objects right into flask shell
# so you don't have to worry about from app.models import
# User, Post; from sqlalchemy import * etc.
# it's not necessary but very convenient
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'sa': sa, 'so': so, 'User': User, 'Post': Post}

