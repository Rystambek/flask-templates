from tinydb import TinyDB, Query


def get_db():
    db = TinyDB('db.json')
    return db.table('grocery').all()
