from tinydb import TinyDB, Query
db = TinyDB('flask-templates/db.json')

def get_db():
    
    return db.table('grocery').all()

def get_type(type: str) -> list:
    
    q = Query()
    return db.table('grocery').search(q.type == type)

def get_price(price: str) -> list:
    
    q = Query()
    return db.table('grocery').search(q.price == price)

def get_name(name: str) -> list:
    
    q = Query()
    return db.table('grocery').search(q.name == name)