from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # temp db details here (sqlite)
db = SQLAlchemy(app) # instance of db


posts = [
    {
    'title': 'Header One',
    'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit veritatis officiis officia at commodi magni quidem quaerat enim libero sed rem, nisi recusandae similique non ipsam praesentium quasi mollitia eos eligendi, odio vitae animi incidunt cumque. Distinctio ut voluptatibus error officia provident aliquam similique consectetur animi possimus. Harum, voluptatibus enim?',
    'author': 'Debyo Santos',
    'date_created': 'January 1, 2021'
    }
]


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    image_file = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text(500), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'{self.title}'


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', posts=posts)

@app.route('/article/<int:id>')
def article(id):
    posts = User.query.get(id=id).first_or_404()
    return render_template('article.html', posts=posts)

@app.route('/summernote')
def summernote():
    return render_template('summernote.html')

if __name__ == '__main__':
    app.run(debug=True)