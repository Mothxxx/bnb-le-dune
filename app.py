from re import X
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/camera1')
def camera1():
    return render_template('camera1.html')

@app.route('/camera2')
def camera2():
    return render_template('camera2.html')


if __name__ == '__main__':
    app.run(debug=True)
