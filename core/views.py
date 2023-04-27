from core import app
from flask import request, render_template


@app.route('/<name>', methods=['GET'])
def index(name):

    return render_template('home.html', name=name)
