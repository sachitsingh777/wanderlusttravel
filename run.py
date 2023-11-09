from app import create_app, db
from config import SQLALCHEMY_DATABASE_URI

app = create_app(SQLALCHEMY_DATABASE_URI)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
