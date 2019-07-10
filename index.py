from flask import Flask,render_template, url_for


app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1> Almost There </h1>'

if __name__ == '__main__':
    app.run(debug = True)