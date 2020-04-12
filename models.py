# models.py
# Purpose: Define models and relevant functions for the database with SQLAlchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'

    number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    type_1 = db.Column(db.String(50))
    type_2 = db.Column(db.String(50))
    total = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    sp_atk = db.Column(db.Integer)
    sp_def = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    generation = db.Column(db.Integer)
    islegendary = db.Column(db.Boolean)
    color = db.Column(db.String(50))
    hasgender = db.Column(db.Boolean)
    pr_male = db.Column(db.Float)
    egg_group_1 = db.Column(db.String(50))
    egg_group_2 = db.Column(db.String(50))
    hasmegaevolution = db.Column(db.Boolean)
    height_m = db.Column(db.Float)
    weight_kg = db.Column(db.Float)
    catch_rate = db.Column(db.Integer)
    body_style = db.Column(db.String(50))

    def __init__(self, number, name):
        self.number = number
        self.name = name

    # Gets dict with the User object and all of its associated reviews
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'Number': self.number,
            'Name': self.name,
            'Type_1': self.type_1,
            'Type_2': self.type_2,
            'Total': self.total,
            'HP': self.hp,
            'Attack': self.attack,
            'Defense': self.defense,
            'Sp_Atk': self.sp_atk,
            'Sp_Def': self.sp_def,
            'Speed': self.speed,
            'Generation': self.generation,
            'isLegendary': self.islegendary,
            'Color': self.color,
            'hasGender': self.hasgender,
            'Pr_Male': self.pr_male,
            'Egg_Group_1': self.egg_group_1,
            'Egg_Group_2': self.egg_group_2,
            'hasMegaEvolution': self.hasmegaevolution,
            'Height_m': self.height_m,
            'Weight_kg': self.weight_kg,
            'Catch_Rate': self.catch_rate,
            'Body_Style': self.body_style,
        }

    @staticmethod
    def serialize_list(users):
        return [user.serialize for user in users]
