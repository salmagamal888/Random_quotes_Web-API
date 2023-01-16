# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 19:03:45 2023

@author: dell
"""

import pandas as pd
from flask import Flask, request, make_response, jsonify
import jwt
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from functions import json_to_df

app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY']='Mysecret'

db =SQLAlchemy(app)

authors_df=json_to_df('authors.json')
qs_df=json_to_df('quotes.json')

authors_df=authors_df.explode('quoteIds')
data_df=pd.merge(qs_df, authors_df, how='inner', left_on='id',right_on='quoteIds')
data_df=data_df.drop(['id_x','id_y'],axis=1)


#data exploration
'''
print(authors_df.head())
print(authors_df.info())
print(qs_df.head())
print(qs_df.info())
'''

class Quotes(db.Model):
    
    __tablename__="quotes"
    __table_args__ = {'extend_existing': True}
    id = db.Column( db.Integer , primary_key =True)
    qoute= db.Column(db.String(50), nullable=False)
    author =db.Column(db.String(20), nullable =False)
    q_id=db.Column(db.Integer, nullable=False)
    

    def __repr__(self):
        #return f'["id":{self.id} , "quote":{self.qoute} , "author":{self.author}]'
        return f'["q_id":{self.id} , "qoute":{self.qoute},"author":{self.author}]'
 

with app.app_context():
    db.create_all()
    for i,item in data_df.iterrows():
        #add smth to db
        db.session.add(Quotes(qoute=item.quote, author=item.author, q_id=item.quoteIds))
        db.session.commit()
        
        #read
    '''print(Quotes.query.all())
    print(len(Quotes.query.all()))'''