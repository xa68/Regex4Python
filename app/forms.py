from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    regex = StringField('Regex', validators=[DataRequired()])
    test_string = StringField('Test_string', validators=[DataRequired()])
    submit = SubmitField('Submit')

