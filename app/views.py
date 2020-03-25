#Ronaldo M. Reid 620109753
"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from .forms import add_Profile
from datetime import date
from app import my_db
from app.models import my_users

###
# Routing for your application.
###

# Renders form as home directory.

@app.route('/', methods = ["GET", "POST"])
def home():
    form = add_Profile()
    if request.method == "POST" and form.validate_on_submit():
        Firstname = form.Firstname.data
        Lastname = form.Lastname.data
        Gender = form.Gender.data
        Email = form.Email.data
        Location = form.Location.data
        Biography = form.Biography.data
        Photo = form.Photo.data 
        filename = secure_filename(Photo.filename)
        Photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        Date = getDate()
        user = my_users(request.form["Firstname"], request.form["Lastname"], request.form["Gender"], request.form["Email"], request.form["Location"], request.form["Biography"], filename, Date)
        my_db.session.add(user)
        my_db.session.commit()            
        return render_template('result.html', form = form, Firstname = Firstname, Lastname = Lastname, Gender = Gender, Email = Email, Location = Location, Biography = Biography)

    else:
        flash_errors(form)
        return render_template('home.html', form = form)


@app.route('/profiles')
def profiles():
    users = my_users.query.all()
    return render_template("profiles_user.html", users = users)


@app.route('/profile')
def profile():
#@app.route('/profile/<user_id>')
#def profile(user_id):    
    profile_user = my_users.query.filter_by(user_id = "1")
    return render_template('profile.html', profile_user = profile_user)


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Lord Reginald")


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def getDate():
    today = date.today().strftime('%B/%w/%Y')
    return today

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
