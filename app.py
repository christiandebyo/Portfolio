from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # temp db details here (sqlite)
db = SQLAlchemy(app) # instance of db


posts = [
    {
    'title': 'Header One',
    'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit veritatis officiis officia at commodi magni quidem quaerat enim libero sed rem, nisi recusandae similique non ipsam praesentium quasi mollitia eos eligendi, odio vitae animi incidunt cumque. Distinctio ut voluptatibus error officia provident aliquam similique consectetur animi possimus. Harum, voluptatibus enim?',
    'author': 'Debyo Santos',
    'date_created': 'January 1, 2021'
    }
]



@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', posts=posts)

@app.route('/article')
def article():
    return render_template('article.html', posts=posts)

# @app.route('/editor')
# def editor():
#     return render_template('editor.html')

if __name__ == '__main__':
    app.run(debug=True)