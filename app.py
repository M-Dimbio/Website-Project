from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, Length
import smtplib


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
Bootstrap(app)
subscribers = []


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=20)])


@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/anime')
def anime():
    return render_template("anime.html")


@app.route('/rap')
def rap():
    return render_template("rap.html")


@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")


@app.route('/subscribe')
def subscribe():
    return render_template("subscribe.html")


@app.route('/thanks', methods=["POST"])
def thanks():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    message = "You have been suscribe to my email newsLetter"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("bootstrap.soen287@gmail.com", "SweetHeart@101")
    server.sendmail("bootstrap.soen287@gmail.com", email, message)

    if not first_name or not last_name or not email:
        error_statement = "All Form Fields Required..."
        return render_template("subscribe.html",
                               error_statement=error_statement,
                               first_name=first_name,
                               last_name=last_name, email=email)

    subscribers.append(f" {first_name} {last_name} ** {email}")

    message = "You have been suscribe to my email newsLetter"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("bootstrap.soen287@gmail.com", "SweetHeart@101")
    server.sendmail("bootstrap.soen287@gmail.com", email, message)
    title = "Thank You!"

    return render_template("thanks.html", subscribers=subscribers)


if __name__ == '__main__':
    app.run()
