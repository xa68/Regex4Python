from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp

class InputForm(FlaskForm):
    regex = StringField('Regex', validators=[DataRequired()])
    flag_ignorecase = BooleanField('IGNORECASE')
    flag_multiline = BooleanField('MULTILINE')
    flag_dotall = BooleanField('DOTALL')
    test_string = TextAreaField('Test_regex', 
                                validators=[DataRequired(), Length(min=1, max=250)])
    submit = SubmitField('Submit')

