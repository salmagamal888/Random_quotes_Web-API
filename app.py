# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 09:33:27 2023

@author: dell
"""
import random
import pandas as pd
from flask import Flask, request, make_response, jsonify, render_template
import jwt
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from functions import json_to_df
from data_analysis_storage import  db, app, Quotes
from decorators import Is_auth_route, token_required



@app.route("/")
def index():

    return render_template('index.html')


@app.route("/qoutes")

@Is_auth_route
def login():
    
    return 'congrats you are logged in please enter your token'

@app.route("/qoutes/API")
@token_required
def random_quote():
    
    rid=random.randint(1,102)
    
    with app.app_context():
        qoute=Quotes.query.get(rid)
    q= {"quote_id":qoute.q_id,'qoute': qoute.qoute, 'author':qoute.author}
    
    return  q



if __name__ =="__main__":
    
    
    app.run()


    

        