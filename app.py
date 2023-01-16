# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 09:33:27 2023

@author: dell
"""
import random
import pandas as pd
from flask import Flask, request, make_response, jsonify
import jwt
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from functions import json_to_df
from data_analysis_storage import  db, app, Quotes
from decorators import Is_auth_route, token_required


#MAX_QOUTE_LENGTH= json file extract


@app.route("/")
def index():

    return "hello"


@app.route("/qoutes")
@Is_auth_route
#@token_required
def get_smth():
    
    rid=random.randint(1,102)
    
    with app.app_context():
        qoute=Quotes.query.get(rid)
    q= {"quote_id":qoute.q_id,'qoute': qoute.qoute, 'author':qoute.author}
    
    return  q



if __name__ =="__main__":
    
        
    #from app import db
    #db.init_app(app)
    #with app.app_context():
        #db.create_all()
        
        #add smth to db
        #db.session.add(Qoutes(qoute="saba7 el 5eer", author="ana"))
        #db.session.commit()
        
        #read
        #r=Qoutes.query.all()

    
    app.run()


    

        