from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired(message = 'Pole jest wymagane, wprowadź nazwę użytkownika')])
    password = PasswordField('Hasło', validators=[DataRequired(message = 'Pole jest wymagane, wprowadź hasło')])
    remember_me = BooleanField('Zapamiętaj mnie')
    submit = SubmitField('Zaloguj Się')


class RegistrationForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators = [DataRequired(message = 'Pole jest wymagane, wprowadź nazwę użytkownika')])
    email = StringField('Email', validators = [DataRequired(message = 'Pole jest wymagane, wprowadź poprawny adres email')])
    password = PasswordField('Hasło', validators = [DataRequired(message = 'Pole jest wymagane, wprowadź hasło')])
    password2 = PasswordField(
        'Powtórz Hasło', validators = [DataRequired(message = 'Pole jest wymagane, wprowadź hasło'), EqualTo('password')])
    submit = SubmitField('Zarejestruj')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError('Proszę użyć innej nazwy użytkownika.')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationErro('Proszę użyć innego adresu email.')
