from flask import Flask, request, render_template, redirect, url_for 

from pymongo import MongoClient 
from dotenv import load_dotenv
import os

app = Flask(__name__) 

load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@mongodb.s4hmk.mongodb.net/?retryWrites=true&w=majority&appName=MongoDB"


client = MongoClient(MONGO_URI) 

db = client["DBNAME"] 

def obtenir_tasques(): 
    return list(db.tasques.find({}, {"_id": 0})) 

@app.route('/') 

def home(): 
    return render_template("index.html", tasques=obtenir_tasques()) 

@app.route('/tasques', methods=['POST']) 

def afegir_tasca(): 
    tasca = { 
        "titol": request.form['titol'], 
        "descripcio": request.form.get('descripcio', ''), 
        "completada": False 
    } 
    db.tasques.insert_one(tasca) 
    return redirect(url_for('home')) 

@app.route('/tasques/<titol>/completar', methods=['POST']) 

def completar_tasca(titol): 
    db.tasques.update_one({"titol": titol}, {"$set": {"completada": True}}) 
    return redirect(url_for('home')) 

@app.route('/tasques/<titol>/eliminar', methods=['POST']) 

def eliminar_tasca(titol): 
    db.tasques.delete_one({"titol": titol}) 
    return redirect(url_for('home')) 

if __name__ == '__main__': 
    app.run(debug=True) 