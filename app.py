from flask import Flask, render_template, request, redirect, Markup

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/hopoffhopon')
def hopoffhopon():
    return render_template('hopoffhopon.html')

@app.route('/substitutesearch')
def substitutesearch():
    return render_template('substitutesearch.html')

@app.route('/makingtheblog')
def makingtheblog():
    return render_template('makingtheblog.html')

@app.route('/instacart')
def instacart():
    return render_template('instacart.html')

if __name__ == '__main__':
    app.run(port=33507,debug=True)