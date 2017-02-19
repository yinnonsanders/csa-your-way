from flask import Flask
from flask import render_template, request, send_file
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View
from flask_sqlalchemy import SQLAlchemy

import os

from algorithm import *
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
	username = db.Column(db.String, unique=True)
	password = db.Column(db.String)
	preferences = db.Column(db.JSON)
	shares = db.Column(db.Integer)

	def __init__(self, name, username, password, preferences, shares):
		self.name = name
		self.username = username
		self.password = password
		self.preferences = preferences
		self.shares = shares

@nav.navigation()
def mynavbar():
    return Navbar(
        'CSA Your Way: Farm Sharing Made Easy',
        View('Home', 'index'),
        Subgroup('Customers',
        	View('New Customer', 'new_customer'),
        	View('Update Preferences', 'customer_login')),
        Subgroup('Farmers',
        	View('Calculate Distribution', 'submit_yield'),
        	View('Download User Dataset', 'download_dataset')),
        View('About', 'about')
    )

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/customers/new')
def new_customer():
	return render_template('newcustomer.html')

@app.route('/customers/new/submit', methods=['POST'])
def submit_preferences():
	name = request.form['name']
	username = request.form['username']
	password = request.form['password']

	if UserEntry.query.filter_by(username=username).first():
		return render_template('newcustomer.html', error="That username is already taken!")

	preferences = {}
	for vegetable in vegetableList:
		if request.form[vegetable]:
			preferences[vegetable] = request.form[vegetable]

	shares = request.form['shares']

	db.session.add(UserEntry(name, username, password, preferences, shares))
	db.session.commit()

	return render_template('thankyou.html')

@app.route('/customers/login')
def customer_login():
	return render_template('login.html')

@app.route('/customers/update', methods=['POST'])
def update_preferences():
	username = request.form['username']
	password = request.form['password']
	user = UserEntry.query.filter_by(username=username, password=password).first()

	if not user:
		return render_template('login.html', error="Wrong username or password")

	return render_template('update.html', user_id=user.id)

@app.route('/customers/update/submit', methods=['POST'])
def submit_preference_updates():
	user_id = request.form['user_id']

	user = UserEntry.query.get(user_id)

	preferences = {}
	for vegetable in vegetableList:
		if request.form[vegetable]:
			preferences[vegetable] = request.form[vegetable]

	shares = request.form['shares']

	user.preferences = preferences
	user.shares = shares
	db.session.commit()

	return render_template('thankyou.html')

@app.route('/farmers/yield')
def submit_yield():
	return render_template('farmers.html')

@app.route('/farmers/distribution', methods=['POST'])
def display_distribution():
	yield_dict = {}
	for vegetable in vegetableList:
		if request.form[vegetable]:
			yield_dict[vegetable] = int(request.form[vegetable])

	user_entry_list = UserEntry.query.all()
	user_list = []
	for user_entry in user_entry_list:
		preferences = {}
		for vegetable in vegetableList:
			if user_entry.preferences[vegetable]:
				preferences[vegetable] = int(user_entry.preferences[vegetable])
		user_list.append(User(user_entry.id, preferences, user_entry.shares))

	box_list = get_distribution(user_list, yield_dict)
	display_list = []
	for box in box_list:
		display_list.append((box, UserEntry.query.get(box.userid).name))

	return render_template('displaydistribution.html', display_list=display_list)

@app.route('/farmers/dataset')
def download_dataset():
	return send_file("http://csa-clover.herokuapp.com/launch/get_xlsx")
