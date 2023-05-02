from core import app
from flask import request, render_template
from .db import get_db,get_type,get_name,get_price

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html', title='home')

@app.route('/grocery', methods=['GET'])
def grocery():
    
    context = get_db()

    return render_template('grocery.html', context=context, title='grocery')

@app.route('/grocery/type/<type>', methods=['GET'])

def type(type):
    
    context = get_type(type)


    return render_template('grocery.html', context=context, title=f'{type}')


@app.route('/grocery/name/<name>', methods=['GET'])
def name(name):
    
    context = get_name(name)


    return render_template('grocery.html', context=context, title=f'{name}')


@app.route('/grocery/price/<price>', methods=['GET'])
def price(price):
    
    context = get_price(price)


    return render_template('grocery.html', context=context, title=f'{price}')