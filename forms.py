from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, FloatField, IntegerField
from wtforms.validators import DataRequired

class PrekeForm(FlaskForm):
    pavadinimas = StringField('Pavadinimas', [DataRequired()])
    kaina = FloatField('Kaina', [DataRequired()])
    kiekis = IntegerField('Kiekis', [DataRequired()])
    submit = SubmitField('Įvesti')


