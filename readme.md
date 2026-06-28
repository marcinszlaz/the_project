# commands in venv:

* `export FLASK_APP=mainproject.py` - adding variable (main file)
* `flask run --host=0.0.0.0 --port=5005 --debug` - launch  WSGI server
* `flask routes` - runs in venv, display available routes
* `flask shell` after that `app.config` - same but better xD
* `FLASK_RUN_HOST=0.0.0.0` `FLASK_RUN_PORT=5005` - put it inside .flaskenv file

# commands FLASK ALEMBIC
* explanation - this module handles db migration
* pip install flask-migrate
* from.flask_migrate.import.Migrate 
* after those actions above flask command  gets magic powers and can do this below
* ```flask db init` -  (in folder above app package, within venv not in flask shell)
* initialize database migrator,
* `````````flask db migrate -m "your comment"` - first migration with comment, it populates folder migrations/versions with database script
* `````````````flask db upgrade````` - upgrades database from script
* `flask db downgrade` - it can also downgrade it!
* `flask db upgrade/downgrade <revision_id>` - type explicitly rev_id to get desired version of db
*  `flask db upgrade head` - upgrade to the newest version
*  if you use sqlite you can make db.db file by using command flask db upgrade,
*  if you use MySQL or PostgreSQL you have to make database on server before upgrade it from Alembic script
* `flask downgrade base` oldest version (basicaly first version)

# some commands in vim

*.`:9,18norm i#`.-.this.way.you.can.handle.multiline.comments.in.vim
*.`:9,18norm x`.-.delete.one.char.(#),.you.can.use.visual.too
* `:9,21s/^#/`.-.this.also.remove.(substitiute).#.to.`.`
* `v.-.visual.:s/^#//` .equal.this.above
* `^` it means "first char" like in xpath / css selectors
* ctrl.-.y.means.YES.for.chosen.tips.from.plugins.in.vim

# commands in pip
* explanation - commands installing Python packages
*  pip freeze > requirements.txt - freezes project requirements/dependencies
*  pip install -r requirements.txt - install according requirements.txt file
*  pip install flask-login
* 
