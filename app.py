
from flask import Flask,jsonify, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://spencer:password@localhost/db_learning'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80), unique=True, nullable=False)
    color = db.Column(db.String(120), nullable=False)

    def __init__(self, pname, color):
        self.pname = pname
        self.color = color

@app.route('/')
def home():
    return '<a href="/addperson"><button> Click here </button></a>'


@app.route("/personadd")
def personadd():
    # entry = People(pname='hola', color='red')
    # db.session.add(entry)
    # db.session.commit()
    person = People.query.filter_by(pname = 'hola').first()
    pname1 = person.pname
    return jsonify(pname=pname1)


if __name__ == '__main__':
    db.create_all()
    app.run(port=5001)