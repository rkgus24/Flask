from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome'


@app.route('/create/')
def create():
    return 'Create'


@app.route('/read/1/')
def read():
    return 'Read 1'

app.run(debug=True)