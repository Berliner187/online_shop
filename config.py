from main import app, db


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db.create_all()
