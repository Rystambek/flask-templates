from core import app
from flask import request, render_template
from .db import get_db

@app.route('/<name>', methods=['GET'])
def index(name):

    context = ['Hello', 'World', 'From', 'Flask', 'App']

    return render_template('home.html', context=context, title='index')


@app.route('/grocery', methods=['GET'])
def grocery():
    
    context = get_db()

    return render_template('grocery.html', context=context, title='grocery')
