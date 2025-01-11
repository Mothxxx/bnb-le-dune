
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


    
@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/camera1', methods=["GET"])
def camera1():
    return render_template('camera1.html',  methods=["GET"])

@app.route('/camera2',  methods=["GET"])
def camera2():
    return render_template('camera2.html')

@app.route('/camere',  methods=["GET"])
def camere():
    return render_template('camere.html')

@app.route('/privacy_policy', methods=["GET"])
def privacy_policy():
    return render_template('privacy_policy.html')  # Assicurati che il file HTML sia salvato in templates/


if __name__ == '__main__':
    app.run(debug=True)
