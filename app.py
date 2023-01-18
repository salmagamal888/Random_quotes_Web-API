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
from multiprocessing import Value
from datetime import datetime

counter = Value('i', 0)

@app.route("/")
def index():

    return render_template('index.html')

@app.route("/login")
@Is_auth_route
def login():
    
    token=jwt.encode({'user':"my user"}, app.config['SECRET_KEY'], algorithm="HS256")
    
    return 'congrats you are logged in. Navigate to http://127.0.0.1:5000/quotes/API?token={}'.format(token)



ids={"id":[]}
@app.route("/quotes/API")
@token_required
def random_quote():
    
    rid=random.randint(1,102)
    ids["id"].append(rid)
    
    #count api calls
    with counter.get_lock():
        counter.value += 1
        if counter.value >2:
            counts=pd.DataFrame(ids).id.value_counts()
            count_df=counts.rename_axis('quote_id').to_frame("counts")
            count_df.to_csv('Quotes_report_{}.csv'.format(datetime.now().date()))
            
    
    
    with app.app_context():
        qoute=Quotes.query.get(rid)
    q= {"quote_id":qoute.q_id,'qoute': qoute.qoute, 'author':qoute.author}
    
    return  q



if __name__ =="__main__":
    
    
    app.run()


    

        