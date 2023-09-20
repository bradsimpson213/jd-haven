from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired 
from wtforms import DateField, SubmitField
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    file = FileField("Data File", validators=[FileAllowed(["csv"])])
    date = DateField("Report Date", validators=[DataRequired()])
    submit = SubmitField("Submit Data")