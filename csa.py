from flask import Flask
from flask import render_template, request
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_sqlalchemy import SQLAlchemy

import os

# from algorithm import *
from vegetables import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)
nav = Nav(app)

class UserEntry(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	preferences = db.Column(db.JSON)
	shares = db.Column(db.Integer)

	def __init__(self, name, preferences, shares):
		self.name = name
		self.preferences = preferences
		self.shares = shares

@nav.navigation()
def mynavbar():
    return Navbar(
        'CSA',
        View('Home', 'index'),
        View('Customers', 'customers'),
        View('Farmers', 'farmers')
    )

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/customers/preferences')
def customers():
	return render_template('customers.html')

@app.route('/customers/submit', methods=['POST'])
def submit_preferences():
	name = request.form['name']

	preferences = {}
	for vegetable in vegetableList:
		if request.form[vegetable]:
			preferences[vegetable] = request.form[vegetable]

	shares = request.form['shares']

	db.session.add(UserEntry(name, preferences, shares))
	db.session.commit()

	return render_template('thankyou.html')

@app.route('/farmers/yield')
def farmers():
	return render_template('farmers.html')

@app.route('/farmers/distribution', methods=['POST'])
def display_distribution():
	yield_dict = {}
	for vegetable in vegetableList:
		if request.form[vegetable]:
			yield_dict[vegetable] = request.form[vegetable]

	user_entry_list = UserEntry.query.all()
	user_list = []
	for user_entry in user_entry_list:
		user_list.append(User(user_entry.id, user_entry.preferences, user_entry.shares))

	box_list = get_distribution(user_list, yield_dict)
	display_list = []
	for box in box_list:
		display_list.append(box, UserEntry.query.get(box.userid).name)

	return render_template('displaydistribution.html', display_list=display_list)
