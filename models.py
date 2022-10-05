from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """User Model"""
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    fullname = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    username = db.Column(db.String(25),unique=True,nullable=False)
    password = db.Column(db.String(),nullable=False)

class Inventory(db.Model):
    """Inventory"""
    __tablename__ = "inventory"
    id = db.Column(db.Integer,primary_key=True) #product_id
    product_code = db.Column(db.String(10),nullable=False)
    product_name = db.Column(db.String(100),nullable=False)
    category = db.Column(db.String(50),nullable=False)
    count_of_product = db.Column(db.Integer,nullable=False)
    price_of_product = db.Column(db.Integer,nullable=False)

class InventChanges(db.Model):
    """Changes in amount of Items in Inventory"""
    __tablename__ = "inventchanges"
    id = db.Column(db.Integer,primary_key=True) #transact_id
    date = db.Column(db.DateTime,default=datetime.utcnow)
    transact_type = db.Column(db.String(10),nullable=False)
    product_id =  db.Column(db.Integer,nullable=False)
    product_name = db.Column(db.String(100),nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    price_of_product = db.Column(db.Integer,nullable=False)