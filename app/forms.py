from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class InputForm(FlaskForm):
    regex = StringField('Regex', validators=[DataRequired()])
    test_string = TextAreaField('Test_regex', 
                                validators=[DataRequired(), Length(min=1, max=400)])
    ## add check boxes for flags re.IGNORE re.MULTILINE re.DOTALLL
    submit = SubmitField('Submit')

