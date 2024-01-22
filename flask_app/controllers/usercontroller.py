from flask_app import app
from flask import render_template, request, redirect

from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.user_model import User

@app.route('/')
def read_all():
    return render_template('read_all.html', full_user_list = User.get_all())

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/create_new_user", methods = ["POST"])
def create_new_user():
    User.create_user(request.form)
    return redirect('/')

@app.route("/delete_user/<int:id>")
def delete_user(id):
    User.delete(id)
    return redirect('/') 

@app.route("/update_page/<int:id>")
def update_page(id):
    return render_template("update.html", user = User.get_one(id))

@app.route("/save", methods = ["POST"])
def save_user():
    User.update(request.form)
    return redirect("/")
