from flask import Flask
from flask import request
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_sqlalchemy import SQLAlchemy

from vegetables import vegetableList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)
nav = Nav(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	preferences = db.Column(db.JSON)
	shares = db.Column(db.Integer)

	def __init__(self, preferences, shares):
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
	pass

@app.route('/customers/submit', methods=['POST'])
def submit_preferences():
	preferences = {}
	for vegetable in vegetableList:
		if request.form[vegetable]:
			preferences[vegetable] = request.form[vegetable]

	shares = request.form['shares']

	db.session.add(User(preferences, shares))
	db.commit()

	return render_template('thankyou.html')

@app.route('/farmers/yield')
def farmers():
	pass

@app.route('/farmers/distribution', methods=['POST'])
def display_distribution():
	
	return render_template('displaydistribution.html')
