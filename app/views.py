from flask import render_template
from app import app
from forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
            title="Home")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid_data + '", 
                remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', 
            title= 'Sign in',
            form = form)
