from app import app
import flask
@app.route('/')
@app.route('/index')
def index():
    return "<h1>Hello world<h1>"