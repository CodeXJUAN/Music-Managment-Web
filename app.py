from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
CLUSTERNAME = os.getenv("CLUSTERNAME")
DBNAME = os.getenv("DATABASE")

MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@mongodb.s4hmk.mongodb.net/?retryWrites=true&w=majority&appName={CLUSTERNAME}"

client = MongoClient(MONGO_URI)

db = client[f"{DBNAME}"]

def obtener_music():
    return list(db.Musics.find({}, {"_id": 0}))

@app.route('/')
def home():
    return render_template("index.html", Musics=obtener_music())

@app.route('/Musics', methods=['POST'])
def añadir_music():
    music = {
        "titulo": request.form['titulo'],
        "artista": request.form.get('artista', ''),
        "ano": request.form.get('ano', ''),
        "album": request.form.get('album', ''),
        "foto": request.form.get('foto', ''),
        "completada": False
    }
    db.Musics.insert_one(music)
    return redirect(url_for('home'))

@app.route('/Musics/<titulo>/completar', methods=['POST'])
def completar_music(titulo):
    db.Musics.update_one({"titulo": titulo}, {"$set": {"completada": True}})
    return redirect(url_for('home'))

@app.route('/Musics/<titulo>/eliminar', methods=['POST'])
def eliminar_music(titulo):
    db.Musics.delete_one({"titulo": titulo})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)