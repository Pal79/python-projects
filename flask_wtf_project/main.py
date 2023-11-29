from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5

OWN_EMAIL = "pal.daniel.79@gmail.com"
OWN_PASSWORD = "abc123"

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log in")

app = Flask(__name__)
app.secret_key = "ez egy titok"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        #print(login_form.email.data)
        if login_form.email.data == OWN_EMAIL and login_form.password.data == OWN_PASSWORD:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template(
        "login.html",
        form=login_form
    )


if __name__ == '__main__':
    app.run(debug=True)
