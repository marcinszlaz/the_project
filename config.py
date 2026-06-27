import os
import pathlib
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = pathlib.Path.cwd() / '.env'
#print(dotenv_path) output => /home/xxx/praca/python/VirtualEnvironments/the_project/.env
#this command doesn't treat package (namespace) app as folder!
load_dotenv(dotenv_path = dotenv_path)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URL') or 
                               'sqlite:///' + os.path.join(basedir,'database.db'))
