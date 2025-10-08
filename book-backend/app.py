from flask import Flask
from extension import db
from models import Book


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app) 


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    Book.init_db()


if __name__ == '__main__':
    # 开发模式运行，自动重载代码
    app.run(debug=True)