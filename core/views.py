from core import app
from flask import request, render_template


@app.route('/<name>', methods=['GET'])
def index(name):

    context = ['Hello', 'World', 'From', 'Flask', 'App']

    return render_template('home.html', context=context, title='index')
