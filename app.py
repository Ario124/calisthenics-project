import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'calisthenics-project'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')


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
    
@app.route('/edit_program/<program_id>')
def edit_program(program_id):
    _program = mongo.db.training_programs.find_one({"_id": ObjectId(program_id)})
    _categories = mongo.db.categories.find()
    _difficulty = mongo.db.difficulty.find()
    category_list = [category for category in _categories]
    difficulty_list = [difficult for difficult in _difficulty]
    return render_template('edit_program.html', program = _program, categories = category_list, difficulties = difficulty_list)
    
    
@app.route('/update_program/<program_id>', methods=['POST'])
def update_program(program_id):
    training_programs = mongo.db.training_programs
    training_programs.update({'_id': ObjectId(program_id)},
    {
        'category_name':request.form.get('category_name'),
        'difficulty_level':request.form.get('difficulty_level'),
        'program_name':request.form.get('program_name'),
        'exercise':request.form.get('exercise'),
        'exercise2':request.form.get('exercise2'),
        'exercise3':request.form.get('exercise3'),
        'sets_amount':request.form.get('sets_amount'),
        'sets_amount2':request.form.get('sets_amount2'),
        'sets_amount3':request.form.get('sets_amount3'),
        'reps_amount':request.form.get('reps_amount'),
        'reps_amount2':request.form.get('reps_amount2'),
         'reps_amount3':request.form.get('reps_amount3'),
        'equipment_required':request.form.get('equipment_required'),
        'description':request.form.get('description')
    })
    return redirect(url_for('get_programs'))
    
@app.route('/add_exercise')
def add_exercise():
    return render_template('add_exercise.html')
    

@app.route('/delete_program/<program_id>')
def delete_program(program_id):
    mongo.db.training_programs.remove({'_id': ObjectId(program_id)})
    return redirect(url_for('get_programs'))
    

@app.route('/exercises')
def exercises():
    return render_template('exercises.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)