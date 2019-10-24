from app import app
from flask import render_template
@app.route('/')#корень сайта,домен второго уровня
def index():
    name = 'Igor'
    return (render_template('index.html',n = name));