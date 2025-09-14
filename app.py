from flask import Flask, render_template, url_for
import os
import json

app = Flask(__name__)

# Carica i dati delle camere da JSON esterno
with open('rooms_data.json', 'r', encoding='utf-8') as f:
    rooms_data = json.load(f)

def static_file(filename):
    """Genera URL statico con versioning basato su timestamp file per caching"""
    filepath = os.path.join(app.static_folder, filename)
    if os.path.exists(filepath):
        version = int(os.path.getmtime(filepath))
        return url_for('static', filename=filename) + f'?v={version}'
    return url_for('static', filename=filename)

def process_room_images(room):
    """Applica static_file a tutte le chiavi immagine di una camera"""
    for key in room:
        if isinstance(room[key], str) and 'image' in key:
            room[key] = static_file(room[key])
        elif isinstance(room[key], list) and key.endswith('_images'):
            room[key] = [static_file(img) for img in room[key]]
    return room

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/camere")
def camere():
    # Applica la funzione static_file a immagini per tutte le camere
    rooms = [process_room_images(room.copy()) for room in rooms_data.values()]
    return render_template("camere.html", rooms=rooms)

@app.route("/camera/<room_id>")
def camera_detail(room_id):
    camera = rooms_data.get(room_id)
    if not camera:
        return "Camera non trovata", 404
    # Applica versioning alle immagini della camera singola
    camera = process_room_images(camera.copy())
    return render_template("camera.html", camera=camera)

@app.route("/privacy")
def privacy():
    return render_template("privacy_policy.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)