import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'calisthenics-project'
app.config["MONGO_URI"] = 'mongodb+srv://root:pasol005@myfirstcluster-qno2b.mongodb.net/calisthenics?retryWrites=true&w=majority'


mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', training_programs=mongo.db.training_programs.find())
    
@app.route('/add_program')
def add_program():
    return render_template('add_program.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)