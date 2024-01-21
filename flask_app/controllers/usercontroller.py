from flask_app import app
from flask import render_template

from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.user_model import user

@app.route('/')
def read_all():

    user.get_all()

    return render_template('read_all.html')