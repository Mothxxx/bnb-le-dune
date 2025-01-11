
from flask import Flask, render_template, request, redirect, send_from_directory
import os
app = Flask(__name__)


    
@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/camere',  methods=["GET"])
def camere():
    return render_template('camere.html')

@app.route('/robots.txt', methods=["GET"])
def robots():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'robots.txt', mimetype='text/plain')


@app.route('/privacy_policy', methods=["GET"])
def privacy_policy():
    return render_template('privacy_policy.html')  # Assicurati che il file HTML sia salvato in templates/


if __name__ == '__main__':
    app.run(debug=True)
