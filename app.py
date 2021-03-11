from flask import Flask, render_template, url_for, request
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
    content = db.Column(db.Text(), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'{self.title}'


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', posts=posts)

@app.route('/article')
def article():
    return render_template('article.html', posts=posts)

@app.route('/summernote', methods = ['GET', 'POST'])
def summernote():
    if request.method == 'POST':
        posts = Posts(content = request.form['editordata'])
        db.session.add(posts)
        db.session.commit()
    return render_template('summernote.html')


if __name__ == '__main__':
    app.run(debug=True)