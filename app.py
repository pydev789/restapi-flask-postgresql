# app.py
# Purpose: Create a Flask app and define the necessary API routes

from flask import Flask, jsonify, request, abort, json
from flask_sqlalchemy import SQLAlchemy
from models import (User)
# Initialize Flask app with SQLAlchemy
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

@app.route('/')
def main_page():
    return "<html><head></head><body>A RESTful API in Flask using SQLAlchemy."

@app.route('/monsters/<id>')
def show_user(id):
    try:
        user = User.query.filter_by(number=id).first()
        return jsonify(user.serialize)
    except:
        return not_found("User does not exist")

@app.route('/monsters')
def show_user_all():
    try:
        users = User.query.all()
        return json.dumps(User.serialize_list(users))
    except:
        return not_found("User does not exist")

@app.route('/monsters/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user=db.session.query(User).filter(User.number==id).first()
        db.session.delete(user)
        db.session.commit()
        return success("User delete")
    except:
        return not_found("User does not exist")

@app.route('/monsters/<id>', methods=['PUT'])
def update_user(id):
    try:
        if not request.is_json or 'Name' not in request.get_json()  or 'Type_1' not in request.get_json():
            return bad_request('Missing required data')
        
        if not request.get_json(force=True):
            abort(400)
        data = request.get_json(force=True)

        user=db.session.query(User).filter(User.number==id).first()
        
        user.name = data['Name']
        user.type_1 = data['Type_1']

        if "Type_2" in data: user.type_2 = data['Type_2']
        else: user.type_2 = 'Unknown'
        
        if "Total" in data: user.total = data['Total']
        else: user.total = 0

        if "HP" in data: user.hp = data['HP']
        else: user.hp = 0

        if "Attack" in data: user.attack = data['Attack']
        else: user.attack = 0

        if "Defense" in data: user.defense = data['Defense']
        else: user.defense = 0

        if "Sp_Atk" in data: user.sp_atk = data['Sp_Atk']
        else: user.sp_atk = 0

        if "Sp_Def" in data: user.sp_def = data['Sp_Def']
        else: user.sp_def = 0

        if "Speed" in data: user.speed = data['Speed']
        else: user.speed = 0

        if "Generation" in data: user.generation = data['Generation']
        else: user.generation = 0

        if "isLegendary" in data: user.islegendary = data['isLegendary']
        else: user.islegendary = False
            
        if "color" in data: user.color = data['color']
        else: user.color = 'Unknown'

        if "hasGender" in data: user.hasgender = data['hasGender']
        else: user.hasgender = False

        if "Pr_Male" in data: user.pr_male = data['Pr_Male']
        else: user.pr_male = 0.0

        if "Egg_Group_1" in data: user.egg_group_1 = data['Egg_Group_1']
        else: user.egg_group_1 = 'Unknown'

        if "Egg_Group_2" in data: user.egg_group_2 = data['Egg_Group_2']
        else: user.egg_group_2 = 'Unknown'

        if "hasMegaEvolution" in data: user.hasmegaevolution = data['hasMegaEvolution']
        else: user.hasmegaevolution = False

        if "Height_m" in data: user.height_m = data['Height_m']
        else: user.height_m = 0.0

        if "Weight_kg" in data: user.weight_kg = data['Weight_kg']
        else: user.weight_kg = 0.0

        if "Catch_Rate" in data: user.catch_rate = data['Catch_Rate']
        else: user.catch_rate = 0

        if "Body_Style" in data: user.body_style = data['Body_Style']
        else: user.body_style = 'Unknown'

        db.session.commit()
        return success("User update")
    except:
        return not_found("User does not exist")

@app.route('/monsters', methods=['POST'])
def create_user():
    try:
        if not request.is_json or 'Number' not in request.get_json()  or 'Name' not in request.get_json():
            return bad_request('Missing required data')

        user = User(request.get_json()['Number'], request.get_json()['Name'])
        data = request.get_json(force=True)
        
        user.number = data['Number']
        user.name = data['Name']

        if "Type_1" in data: user.type_1 = data['Type_1']
        else: user.type_1 = 'Unknown'

        if "Type_2" in data: user.type_2 = data['Type_2']
        else: user.type_2 = 'Unknown'
        
        if "Total" in data: user.total = data['Total']
        else: user.total = 0

        if "HP" in data: user.hp = data['HP']
        else: user.hp = 0

        if "Attack" in data: user.attack = data['Attack']
        else: user.attack = 0

        if "Defense" in data: user.defense = data['Defense']
        else: user.defense = 0

        if "Sp_Atk" in data: user.sp_atk = data['Sp_Atk']
        else: user.sp_atk = 0

        if "Sp_Def" in data: user.sp_def = data['Sp_Def']
        else: user.sp_def = 0

        if "Speed" in data: user.speed = data['Speed']
        else: user.speed = 0

        if "Generation" in data: user.generation = data['Generation']
        else: user.generation = 0

        if "isLegendary" in data: user.islegendary = data['isLegendary']
        else: user.islegendary = False
            
        if "color" in data: user.color = data['color']
        else: user.color = 'Unknown'

        if "hasGender" in data: user.hasgender = data['hasGender']
        else: user.hasgender = False

        if "Pr_Male" in data: user.pr_male = data['Pr_Male']
        else: user.pr_male = 0.0

        if "Egg_Group_1" in data: user.egg_group_1 = data['Egg_Group_1']
        else: user.egg_group_1 = 'Unknown'

        if "Egg_Group_2" in data: user.egg_group_2 = data['Egg_Group_2']
        else: user.egg_group_2 = 'Unknown'

        if "hasMegaEvolution" in data: user.hasmegaevolution = data['hasMegaEvolution']
        else: user.hasmegaevolution = False

        if "Height_m" in data: user.height_m = data['Height_m']
        else: user.height_m = 0.0

        if "Weight_kg" in data: user.weight_kg = data['Weight_kg']
        else: user.weight_kg = 0.0

        if "Catch_Rate" in data: user.catch_rate = data['Catch_Rate']
        else: user.catch_rate = 0

        if "Body_Style" in data: user.body_style = data['Body_Style']
        else: user.body_style = 'Unknown'

        db.session.add(user)
        db.session.commit()
        return jsonify({'user': user.serialize}), 201
    except:
        return not_found("User already exist")
        
# Custom Error Helper Functions
def bad_request(message):
    response = jsonify({'error': message})
    response.status_code = 400
    return response

def not_found(message):
    response = jsonify({'error': message})
    response.status_code = 404
    return response

def success(message):
    response = jsonify({'success': message})
    response.status_code = 200
    return response
