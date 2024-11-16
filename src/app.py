import os
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
from dotenv import load_dotenv

load_dotenv()
PATH = os.path.abspath('instance')
app = Flask(__name__, instance_path=PATH)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

db.init_app(app)

Migrate(app, db)

CORS(app)

if __name__ == '__main__':
	app.run()