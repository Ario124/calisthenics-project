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
    return render_template('index.html')
    
@app.route('/add_program')
def add_program():
    return render_template('add_program.html', categories =mongo.db.categories.find(), difficulty =mongo.db.difficulty.find())
    
    
@app.route('/categories')
def categories():
    return render_template('categories.html')
    
@app.route('/contact')
def contact():
    return render_template('contact.html')    

@app.route('/get_programs')
def get_programs():
    return render_template('programs.html', 
        training_programs=mongo.db.training_programs.find(), description =mongo.db.description.find())
        
        
@app.route('/insert_program', methods=['POST'])
def insert_program():
    training_programs = mongo.db.training_programs
    training_programs.insert_one(request.form.to_dict())
    return redirect(url_for('get_programs'))
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)