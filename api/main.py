from flask import Flask
from flask_bcrypt import Bcrypt
from database.db import db

app = Flask(__name__)
app.config.from_pyfile("config.py")
db.init_app(app)

bcrypt = Bcrypt(app)

from views_game import *

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0")
