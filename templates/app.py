
from flask import Flask, render_template

from templates.data import Blogs

Blogs= Blogs()


app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/author')
def author():
    return render_template('author.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html', blogs= Blogs)



if __name__== '__main__':
    app.run(debug= True)