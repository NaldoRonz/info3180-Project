#Ronaldo M. Reid 620109753
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField, TextAreaField
from wtforms.validators import Required, Regexp, Length, Email
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import ValidationError
#from flask_uploads import UploadSet, IMAGES

#images = UploadSet("images", IMAGES)

class add_Profile(FlaskForm):
    Firstname = StringField("Firstname", validators = [Required(), Length(min=2, max=20), Regexp("^[A-Za-z]+$")])
    Lastname = StringField("Lastname", validators = [Required(),  Length(min=2, max=20), Regexp("^[A-Za-z]+$")])
    Gender = SelectField("Gender", choices = [("M","Male"),("F","Female"), ("O","Other")])
    Email = StringField("Email", validators = [Required(), Email(), Length(max =35)])
    Location = StringField("Location", validators = [Required(), Regexp("^[/s A-Za-z0-9 /s]+$"), Length(max =200)])
    Biography = TextAreaField("Biography", validators = [Required(), Length(max =1000)])
    #Browse = FileField("images", validators =[FileRequired(), FileAllowed(images, "Please only upload image files only!!!")])
