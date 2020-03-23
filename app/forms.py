#Ronaldo M. Reid 620109753
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField, TextAreaField
from wtforms.validators import Required, Regexp, Length, Email
from flask_wtf.file import FileRequired, FileAllowed, FileRequired
from wtforms import ValidationError
#from flask_uploads import UploadSet, IMAGES

class add_Profile(FlaskForm):
    Firstname = StringField("Firstname", validators = [Required(), Length(min=2, max=20), Regexp("^[/s A-Za-z /s]+$")])
    Lastname = StringField("Lastname", validators = [Required(),  Length(min=2, max=20), Regexp("^[/s A-Za-z /s]+$")])
    Gender = SelectField("Gender", choices = [("---","---"),("Male","Male"),("Female","Female"), ("O","Other")])
    Email = StringField("Email", validators = [Required(), Email(), Length(max =35)])
    Location = SelectField("Location", choices = [("---","---"),("Kings Jamaica","Kings JA"),("Linst JA", "Linst JA"),("Mont JA","Mont JA"),("SpnTwn JA","SpnTwn JA"),("Miami FL","Miami FL"),("Queens NY","Queens NY")])
    Biography = TextAreaField("Biography", validators = [Required(), Length(max =1000)])
    Photo = FileField("Photo", validators =[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg'], "Please only upload image files only!!!")]) 

#Photo = UploadSet("Photo", IMAGES)


