# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 09:33:27 2023

@author: dell
"""

from flask import Flask, request, make_response, jsonify
import jwt
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app =Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db =SQLAlchemy(app)


def Is_auth_route(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        auth=request.authorization
        if auth and auth.username =="my user" and auth.passwoard=="pass" :
            #generate the token
            #token=jwt.encode({'user':auth.username})
            return f(*args,**kwargs)
        
        else:
            return make_response("Not authorized",401,{'WWW-Authenticate':'Basic realm= "login requierd"'})
        
    return decorated


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        
        token=request.args.get('token')
        if token==True:
            return jsonify({'token': token.decode('UTF-8')})


#MAX_QOUTE_LENGTH= json file extract

class Qoutes(db.Model):
    
    
    id = db.Column( db.Integer , primary_key =True)
    qoute= db.Column(db.String(50), nullable=False)
    author =db.Column(db.String(20), nullable =False)
    
    
    def __repr__(self):
        #return f'["id":{self.id} , "quote":{self.qoute} , "author":{self.author}]'
        return jsonify({"id":self.id,"qoute":self.qoute,"author":self.author})
 

@app.route("/")
def index():

    return "hello"


@app.route("/qoutes")
@Is_auth_route
def get_smth():
    
    qoutes=Qoutes.query.all()
    out=[]
    for qoute in qoutes:
        q= {'qoute': qoute.qoute, 'author':qoute.author}
        out.append(q)
    
    return  {'Qs':out}



if __name__ =="__main__":
    
        
    #from app import db
    db.init_app(app)
    #with app.app_context():
        #db.create_all()
        
        #add smth to db
        #db.session.add(Qoutes(qoute="saba7 el 5eer", author="ana"))
        #db.session.commit()
        
        #read
        #r=Qoutes.query.all()

    
    app.run()


    

        