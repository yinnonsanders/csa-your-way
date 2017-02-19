from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)
nav = Nav(app)

@nav.navigation()
def mynavbar():
    return Navbar(
        'CSA',
        View('Home', 'index')
    )

@app.route('/')
def index():
	return render_template('index.html')
