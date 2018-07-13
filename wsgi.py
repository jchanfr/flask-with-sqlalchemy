# wsgi.py
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass # Heroku does not use .env

#import os
#import logging
# logging.warn(os.environ["DUMMY"])


from flask import Flask
from config import Config
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
app = Flask(__name__)
app.config.from_object(Config)


from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow # Order is important here!
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import Product
from schemas import products_schema,product_schema

@app.route('/')
def hello():
    return render_template('login.html')

@app.route('/api/v1/products',methods=['GET','POST'])
def use_products():
    if (request.method=='GET'):
        products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
        return render_template('bootstrap.html',products=products)
    elif (request.method=='POST'):
        products = db.session.query(Product).all()
        data=request.json
        product=Product(name=data["name"])
        db.session.add(product)
        db.session.commit()
        render_template('prod.html',products=products)



@app.route('/api/v1/products/<id>',methods=['GET','DELETE','PATCH'])
def manage_products(id):
    if (request.method=='GET'):
        product=db.session.query(Product).filter_by(id=int(id)).first()
#        return product_schema.jsonify(product)
        render_template('prod.html',products=product)

    elif (request.method=='DELETE'):
        product=db.session.query(Product).filter_by(id=int(id)).first()
        db.session.delete(product)
        db.session.commit()
        products = db.session.query(Product).all()
        render_template('prod.html',products=products)
#        return products_schema.jsonify(products)

    elif (request.method=='PATCH'):
        data=request.json
        product=db.session.query(Product).filter_by(id=int(id)).first()
        product.name=data["name"]
        db.session.commit()
        products = db.session.query(Product).all()
#        return products_schema.jsonify(products)
        render_template('prod.html',products=products)
