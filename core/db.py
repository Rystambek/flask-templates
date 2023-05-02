from tinydb import TinyDB, Query


def get_db():
    db = TinyDB('db.json')
    return db.table('grocery').all()

def get_type(type: str) -> list:
    db = TinyDB('db.json')
    q = Query()
    return db.table('grocery').search(q.type == type)

def get_price(price: str) -> list:
    db = TinyDB('db.json')
    q = Query()
    return db.table('grocery').search(q.price == price)

def get_name(name: str) -> list:
    db = TinyDB('db.json')
    q = Query()
    return db.table('grocery').search(q.name == name)